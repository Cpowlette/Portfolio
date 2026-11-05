"""Guard the publishable portfolio against common information disclosures.

Run from the repository root. New media needs a human review before its digest
is added to the approved inventory. This does not inspect old Git history.
"""
from collections import Counter
from hashlib import sha256
from html.parser import HTMLParser
from pathlib import Path
import json
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {".html", ".js", ".css", ".md", ".json", ".svg", ".txt"}
MEDIA_SUFFIXES = {".jpg", ".jpeg", ".png", ".webp", ".mp4"}
PRIVATE_PARTS = {".private-originals", "tmp", ".git"}
RETIRED_MEDIA = re.compile(
    r"^(?:nas-|durham-|cisco-(?:etherchannel|spanning-tree)-|"
    r"drabpe-(?:directory-database-metrics|linux-domain-lookup)|"
    r"ontario-tech-(?:network-lab|wifi-site-survey)|tablet-mdm-support|christian-professional-|"
    r"signature-aluminum-canada-aerial|linkedin-memory-(?:0[1-8]|1[123])(?:[.-]))",
    re.I,
)


def sensitive_text(text):
    """Return categories only, so validation never echoes private values."""
    rules = {
        "IP address": r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
        "email address": r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b",
        "private key": r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----",
        "credential token": r"\b(?:gh[pousr]_[A-Za-z0-9]{30,}|AKIA[A-Z0-9]{16})\b",
        "equipment model": r"\b(?:model|appliance|device|hardware)\s*(?:model)?\s*[:=]?\s+[A-Z]{2,8}-\d{3,6}\b",
        "technical version": r"\b(?:firmware|hypervisor|release|version)\s*(?:version|v)?\s*\d+(?:\.\d+)+",
        "hardware address": r"\b(?:[A-F0-9]{2}:){5}[A-F0-9]{2}\b",
    }
    return [name for name, pattern in rules.items() if re.search(pattern, text, re.I)]


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.refs = []
        self.labels = []
        self.h1 = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.append(attrs["id"])
        self.h1 += tag == "h1"
        self.labels.extend(attrs.get("aria-labelledby", "").split())
        for key in ("href", "src"):
            if attrs.get(key):
                self.refs.append(attrs[key])
        self.refs.extend(part.strip().split()[0] for part in attrs.get("srcset", "").split(",") if part.strip())


def main():
    names = subprocess.check_output(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        cwd=ROOT,
    ).decode("utf-8").split("\0")
    paths = sorted({ROOT / name for name in names if name and (ROOT / name).is_file()})
    errors = []
    pages = {}
    media = {}
    for path in paths:
        rel = path.relative_to(ROOT)
        if PRIVATE_PARTS.intersection(rel.parts):
            errors.append(f"Private path is tracked: {rel}")
            continue
        if path.suffix.lower() in {".pdf", ".docx", ".xlsx"} or path.name.startswith(".env"):
            errors.append(f"Private/unreviewed document is publishable: {rel}")
        if path.suffix.lower() in TEXT_SUFFIXES:
            text = path.read_text(encoding="utf-8-sig")
            for category in sensitive_text(text):
                errors.append(f"{category}: {rel}")
            if path.suffix == ".html":
                page = Page()
                page.feed(text)
                pages[path.resolve()] = page
                if page.h1 != 1:
                    errors.append(f"Expected one main heading: {rel}")
                if any(count > 1 for count in Counter(page.ids).values()):
                    errors.append(f"Duplicate anchor: {rel}")
                if set(page.labels) - set(page.ids):
                    errors.append(f"Invalid accessible section label: {rel}")
        if path.suffix.lower() in MEDIA_SUFFIXES:
            if RETIRED_MEDIA.search(path.name):
                errors.append(f"Retired operational media is publishable: {rel}")
            media[rel.as_posix()] = sha256(path.read_bytes()).hexdigest()
    approved = json.loads((ROOT / "tools/public-media-allowlist.json").read_text(encoding="utf-8"))
    for name, digest in media.items():
        if approved.get(name) != digest:
            errors.append(f"New or changed media requires confidentiality/metadata review: {name}")
    for name in approved.keys() - media.keys():
        errors.append(f"Approved media entry has no public file: {name}")
    for path, page in pages.items():
        for ref in page.refs:
            url = urlsplit(ref)
            if url.scheme or url.netloc:
                continue
            target = (path.parent / unquote(url.path)).resolve() if url.path else path
            if not target.is_relative_to(ROOT) or not target.is_file():
                errors.append(f"Broken local file reference: {path.relative_to(ROOT)}")
                continue
            if PRIVATE_PARTS.intersection(target.relative_to(ROOT).parts):
                errors.append(f"Public page links to private storage: {path.relative_to(ROOT)}")
            if target in pages and url.fragment and unquote(url.fragment) not in pages[target].ids:
                errors.append(f"Broken local anchor: {path.relative_to(ROOT)}")
    if errors:
        print("FAIL\n" + "\n".join(sorted(set(errors))))
        return 1
    print(f"PASS: {len(pages)} pages; public links, identifiers, and {len(media)} approved media files.")
    print("Scope: current public files only; Git history and external copies are not covered.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
