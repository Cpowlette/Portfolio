# Christian Powlette Portfolio

Two connected experiences: enterprise IT and learning, and cultural West African drumming.

- `index.html`: choose a portfolio.
- `it.html`: career history, general capabilities, project summaries, and education.
- `drumming.html`: music, training, performances, schools, and community memories.
- `drumming-resume.html`: digital musician resume with browser printing.
- `projects.html` and `case-studies/`: contributions, outcomes, and lessons learned.

Built with editable HTML, CSS, and JavaScript. No installation or build step is required. Open `index.html` locally.

See [EDITING_GUIDE.md](EDITING_GUIDE.md) for page ownership and editing instructions.

## Public disclosure rules

Professional summaries describe responsibilities and results without revealing real infrastructure inventories, exact versions/models, management endpoints, internal identifiers, configuration captures, or workplace security layouts. Coursework is clearly distinguished from professional deployments.

Private documents and retired operational media are excluded from the public tree. Do not publish ignored local backup or temporary folders. Removing a file in a new commit does not remove earlier versions from Git history.

Before publishing, run:

```text
python tools/check-public-disclosure.py
node --check assets/js/main.js
node --check assets/js/portfolio.js
node --check assets/js/drumming-resume.js
git diff --check
```

Review new images visually and check metadata before updating the approved public-media inventory. Automated checks do not replace that review.

Contact uses the public social links in the portfolio. No personal email or home address is provided here.

## License

Original portfolio content belongs to Christian Powlette unless otherwise credited. Third-party images retain their stated licensing and attribution. Code may be reused for educational and personal portfolio purposes with attribution.
