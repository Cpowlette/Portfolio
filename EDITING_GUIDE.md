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


## University of Guelph event program

`drumming.html#guelph-improvlab-2026` includes the Guelph Dance program for the March 26, 2026 double bill. It summarizes Coco Collective's work and credits, identifies Guelph Dance and IICSI as co-presenters, and records the IBPOC tour initiative separately. Venue context includes Room 108 / ARC wing, the full public event address, and archived accessibility/footwear/parking notes. The official event page and existing Instagram announcement are linked. The Guelph schedule row follows the organizer's event-specific credits: Christian Powlette is credited for musical composition/performance; Keith Pascall is the guest artist; Whitney Charles and Nicole Powlette are explicitly marked in absentia. These credits remain separate from the earlier tour-reel caption. No historical ticket sales or contact details are copied. Source: https://guelphdance.ca/performance/sashar-zarif-dance-theatre-and-coco-collective/ . The supplied Henry Chan promotional photograph is used for Guelph, with credit; the related shared-bill poster is omitted.


## Supplied Facebook drumming photos

Five supplied Facebook CDN images were downloaded locally at their provided 206 x 206 resolution. Four appear once in `#gallery`: `drumming-shared-rhythm.jpg`, `drumming-sunlit-djembe.jpg`, `drumming-djembe-memory.jpg`, and `drumming-drum-collection.jpg`. `.supplied-drumming-thumb` caps their display at native size. The fifth, `afiwi-childhood-square.jpg`, is the supplied square crop of the existing Afiwi childhood portrait; it replaces that entry's thumbnail while the link still opens the original full portrait. No duplicate portrait entry is added. All downloaded images were visually reviewed, contain no EXIF metadata, and were added to the approved public-media inventory. No location, date, event, or photographer was inferred. The signed CDN URLs are not stored in public source; images are served locally.


## Drumming category placement

Detailed university/college records, including `#guelph-improvlab-2026`, are direct child sections of `#universities-colleges`. Guelph retains its complete program and original anchor, with a main venue heading and subordinate work headings. `#public-institutions` groups CECC and TTC; the Freedom Train video and story share one entry. The WULA retreat recording sits in Training & companies. Arts Etobicoke's Albion festival and Nia Centre details sit in Community arts. DanceWeekend 25, Dance Together, Dragon Boat, Muhtadi, and wedding/anniversary performances sit in Events & performances. The performance history is a cross-venue link index; the schedule and photo archives remain aggregate collections. The complete memory index groups links by their destination's actual category. Existing entry IDs, media, source links, program credits, and public privacy safeguards remain.


For the correctional-centre performance entry, omit organizer identities, committee details, staff titles, and organizer contact information. Retain the public event title, date, venue context, and program description.


## Drumming duplicate cleanup

The page displays one of the near-identical outdoor group views (memory 02). The tour-launch collage and Ontario/Quebec promotional graphic are omitted because they reuse performance photos already shown. Original assets remain available for editing. The redundant performance-history link list is removed; `#performance-record` is retained as a compatibility anchor at the single Calabash schedule. The tour reel is shown once inside the University of Guelph entry, with a link to the event-specific program above instead of another event description and repeated credits. Distinct photos, actual event entries, source links, and embedded recordings are retained.


## Ensemble-focused performance content

Performance write-ups focus on Coco Collective and Friday Night Drummers / Yere Wolon, their credited members/contributors, and the event itself. Unrelated co-billed company biographies, separate production credits, panel guest rosters, presenter biographies, and storyteller rosters are omitted. Event co-presenters and source/photo acknowledgements remain for context and attribution. Training teachers and educational history remain intact. Guelph's own-group credits still distinguish the guest artist and contributors credited in absentia. The Guelph Dance photo supplied by URL is saved as `guelph-coco-collective-henry-chan.jpg`, with responsive previews. It replaces the matching lower-resolution photo elsewhere on the page, so the scene appears once. Caption: Henry Chan / promotional image published by Guelph Dance; it is not described as documentation of the Guelph event. Camera/time metadata is stripped losslessly while orientation and public author/copyright tags remain. The shared-bill Montreal poster is omitted; that tour date remains in the schedule.


## Waterloo symposium and facility reference imagery

`#waterloo-pair-2026` is a direct child of Universities & colleges. It covers Coco Collective's listed participation in the November 4, 2026 Black and Free keynote session at the PAIR symposium (November 3-5), using the official Waterloo program and banner. The 11:15 a.m.-1 p.m. interval is identified as the keynote session window, not an inferred individual set time. Venue: Needles Hall, third floor, NH3407. No other guest roster, meeting ID, registration action, or staff contact is reproduced. The university entry includes the official banner and a Needles Hall North exterior reference view. It is not added to Christian's personal resume because the listing names the ensemble, not individual members.

Campus/venue views are added to the Ontario Tech, Humber Lakeshore, Hart House, York, George Brown, Guelph, Notre Dame Ajax, National Ballet School, and Winston Churchill entries. They are labeled reference views rather than event documentation. George Brown's photograph identifies St James campus as general college context; the original performance campus is not inferred. Afiwi and the early-learning program retain existing school/performance imagery because a distinct fixed facility for those memories has not been established.

The user confirmed St Patrick and St James are Ajax schools in DCDSB, and Notre Dame is the Ajax secondary school. The official board pages verify their identities and public addresses. The elementary-school entry provides public aerial views for those confirmed addresses rather than unrelated school photos. `venue-image-sources.json` records credits and licenses for downloaded images; Commons license links are visible in captions. WebP derivatives are proportionally resized and stripped of metadata. Raw downloads, including any camera metadata, remain in ignored temporary storage. No operational/network equipment or security diagrams are added. Facility UI styles are at the end of `assets/css/experiences.css`.
