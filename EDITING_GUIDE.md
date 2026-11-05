# Editing the portfolio

This is a static HTML, CSS, and JavaScript site. Open `index.html` to choose between the technology and drumming portfolios. No build is required.

## Page ownership

| Page | Content | Styles | Behavior |
| --- | --- | --- | --- |
| `index.html` | Two-portfolio entrance | `assets/css/entrance.css`, `assets/css/experiences.css` | `assets/js/experiences.js` |
| `it.html` | Professional profile, skills, work timeline, education, community memories, public contact links | `assets/css/portfolio.css`, `assets/css/earth-palette.css`, `assets/css/work-record.css`, `assets/css/photos.css`, `assets/css/experience.css` | `assets/js/portfolio.js`, `assets/js/memory-navigation.js` |
| `drumming.html` | Musician profile, training, companies, institution memories, performances, media, public social links | `assets/css/experiences.css` | `assets/js/memory-navigation.js` |
| `drumming-resume.html` | Digital musician resume | `assets/css/drumming-resume.css` | `assets/js/drumming-resume.js` |
| `projects.html` | Professional project index | `assets/css/styles.css`, `assets/css/case-study-theme.css`, `assets/css/earth-palette.css` | `assets/js/main.js` |
| `case-studies/*.html` | Responsibilities, outcomes, and lessons learned | `assets/css/styles.css`, `assets/css/case-study-theme.css`, `assets/css/earth-palette.css`, `assets/css/photos.css` | `assets/js/main.js` |

## IT content

The public project records are `secure-nas-deployment.html`, `collaboration-migration-planning.html`, `drabpe-business-directory.html`, `hr-attendance-agent.html`, and `cisco-switching-lab.html` under `case-studies/`.

Describe the problem, personal contribution, outcome, and lessons learned. Keep actual role dates, current/completed status, and measured achievements accurate. Migration planning must remain described as planning. Coursework must remain identified as a controlled learning exercise.

Do not publish real infrastructure inventories, software or firmware versions, exact equipment models, management endpoints, internal names, asset identifiers, serial numbers, network/control layouts, workplace security products, operational incidents, or configuration screenshots. Avoid connecting specific products or internal workflows to named employers. Public career history and general skills can remain.

This rule applies to raw HTML, metadata, alt text, scripts, diagrams, filenames, public documentation, source manifests, full-size images, previews, and unlinked files. Removing an image from a page does not remove it from the repository. Existing operational captures are kept only in ignored local storage.

## Drumming content

Institution and venue entries use bold `.venue-heading` headings with `.venue-event` descriptions. Keep event-specific performers separate from credits attributed to a particular source post. Preserve supplied dates and locations; do not invent exact performance times from schedule blocks.

The Calabash schedule is at `#calabash-schedule`. The training and company records are under `#musical-background`. School entries are under `#schools`; university and college entries are under `#universities-colleges`. Venue addresses describe public events and are distinct from personal contact information.

The St Patrick / St James memory uses the local video `assets/videos/st-patrick-st-james-drumming.mp4`. Other local videos are under `assets/videos/`. Keep controls, inline playback, and correct proportions; do not autoplay. External social embeds can require sign-in. Always retain an original-post link as a fallback.

The musician resume is editable directly in its HTML. Its button opens the browser print dialog. Print pagination depends on browser settings and should be visually reviewed after content changes.

## Media and privacy

Keep home addresses, private email addresses, phone numbers, personal relationship details, and private documents out of public files. Use the existing public social profiles for contact. Never place credentials or private configuration in frontend source or Git.

New media requires a visual confidentiality review and metadata review. Exclude operational screenshots and identifiable internal equipment. Preserve proportions, descriptive alt text, credit/licensing information, and author permissions. Files under `.private-originals/` and `tmp/` are local only and ignored by Git; do not publish or upload those folders.

`tools/check-public-disclosure.py` checks common disclosure regressions and the approved public-media inventory. When intentionally adding reviewed media, update `tools/public-media-allowlist.json` with its SHA-256 after reviewing the pixels and metadata. An automated check cannot judge every detail visible inside a photograph.

## Validation and publication

Run `python tools/check-public-disclosure.py` and `node --check` for changed JavaScript. Check local links, fragments, media files, and responsive behavior. Use `git diff --check` before committing. A successful Git push does not establish GitHub Pages deployment or rendered-browser verification.

A cleanup commit removes data from the current tree only. Older commits, existing clones, forks, cached views, or other public profiles may retain earlier information. History removal requires a deliberate rewrite and coordination; never force-push history casually.
