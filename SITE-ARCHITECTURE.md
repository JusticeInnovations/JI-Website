# Justice Innovations Website — Site Architecture Guide

**Last updated:** April 17, 2026
**File:** `index.html` (single-file site, 2608 lines)
**Live URL:** https://justiceinnovations.github.io/JI-Website/
**Repo:** https://github.com/JusticeInnovations/JI-Website

---

## What This Document Is

This is the reference guide for anyone making changes to the Justice Innovations website. Read this before touching anything. It tells you what every section is, where it lives, what is safe to change, and what is fragile.

For build tooling, testing commands, and CSS custom properties, see `README.md` — this guide does not duplicate that material. This guide covers **how to change the site safely**, not how to set it up.

---

## How the Site Works

This is a **single-file website**. Everything — all content, all styling, all behavior — lives in one file: `index.html`. There is one supporting asset: `JI-Security-Compliance-White-Paper.pdf`.

There is no database, no CMS, no build process. You edit `index.html`, push to GitHub, and GitHub Pages publishes the site within 1–2 minutes. A CI pipeline (Black, Ruff, pytest — 88 tests) runs on every push; if tests fail, the push is flagged but the site still deploys.

Contact form submissions POST to Formspree (`https://formspree.io/f/xbdzzwqo`) and are emailed to `kb@justiceinnovations.us` and `sd@justiceinnovations.us`. Nothing runs server-side on our infrastructure.

---

## File Structure

```
JI-Website/
├── index.html                              # Entire site — HTML, CSS, JS in one file
├── index_BACKUP_before_Sasha_edit.html     # Manual backup (created before hero edit)
├── ARCHIVE_index.html                      # Older archived version
├── JI-Security-Compliance-White-Paper.pdf  # Linked from #white-paper section
├── social-preview.svg                      # Open Graph image
├── CNAME                                   # Custom domain config for GitHub Pages
├── README.md                               # Build/test/deploy reference
├── SITE-ARCHITECTURE.md                    # This file
├── pyproject.toml                          # pytest / black / ruff config
├── requirements-test.txt                   # Python test deps
├── .github/workflows/ci.yaml               # CI pipeline
└── tests/                                  # 88 tests enforcing copy, a11y, structure
```

---

## Section Map

Line numbers are approximate and drift when content is added. Section IDs are stable (changing them breaks tests and navigation).

| Line | ID | Section |
|---:|---|---|
| 1361 | — | `<nav>` desktop navigation |
| 1444 | `mobileNav` | Mobile nav drawer |
| 1465 | `top` | Hero (tagline + primary CTA) |
| 1484 | — | Trust strip |
| 1499 | `what-is-intake` | Product overview, officer quote, $4.6M stat |
| 1532 | `why-prosecutor` | Methodology rationale |
| 1561 | `how-it-works` | 4-step walkthrough + case status flow |
| 1660 | `features` | Feature card grid |
| 1716 | — | Platform mockup |
| 1753 | `implementation` | 3-phase deployment package |
| 1819 | `what-we-measure` | Metrics & outcomes |
| 1840 | `research` | Harris County Model |
| 1883 | `research-data` | "Cost of Doing Nothing" stats |
| 1926 | `research-papers` | Published papers + `#white-paper` |
| 2015 | `solutions` | Role-based overview |
| 2051 | `solutions-da` | For District Attorneys |
| 2086 | `solutions-le` | For Law Enforcement |
| 2117 | `solutions-courts` | For Courts & Judges |
| 2147 | `solutions-policy` | For Legislators & Policy |
| 2180 | `about` | Company mission |
| 2199 | `about-scilaw` | SciLaw research partnership |
| 2228 | `about-pilot` | Cameron County pilot |
| 2255 | `cta` | Final "Request a Demo" CTA |
| 2268 | — | `<footer>` |
| 2334 | `legalModal` | Privacy / Terms modal |
| 2342 | `contactModal` | Demo request form |

---

## What Is Safe to Change

- **Body copy** within a section, *provided* it doesn't remove a phrase the test suite enforces (see "What Is Fragile" below).
- **Adding new feature cards, list items, or stat blocks** inside an existing section.
- **Updating dates, names, quotes** — so long as required facts (see below) remain on the page.
- **Swapping images / SVGs** inside a section.
- **Styling tweaks** via the CSS custom properties at the top of the `<style>` block (`--blue`, `--electric`, `--gold`, spacing, max-width).
- **Adding a new paper** to the `#research-papers` section — follow the pattern of existing entries.

---

## What Is Fragile

These things are enforced by the test suite in `tests/`. Changing them will fail CI.

### Required section IDs — do not rename or remove
`what-is-intake`, `why-prosecutor`, `features`, `implementation`, `what-we-measure`, `research`, `solutions`, `about`, `contactModal`

### Required facts that must appear somewhere on the page
- `$4.6M` — Cameron County savings
- `25%` — pretrial reduction
- `90` — average call length (seconds)
- `36` — average nights in jail
- `1977` — Harris County baseline year
- `Cameron County`, `Brownsville`
- `DUI`, `Domestic Violence`
- `Woman-Owned` (or `WOSB`)
- `Public Benefit`

### Required exact phrases
- `indicates that this process` (NOT "suggests that this process")
- `They run the most efficient prosecution office`
- `Justice Innovations has built the software`
- `(someone who should never have been arrested)` — parentheses required
- `from day one, not retrofitted` — comma required, not em-dash
- `results of over four decades in Harris County are unambiguous`
- `Harris County is near zero`
- `structured as a rigorously designed evaluation`
- `The science.` — must appear as an `<h2>`

### Forbidden phrases (removed in prior editorial pass — do not reintroduce)
- `is not a theory`
- `not a new idea`
- `science is not a footnote`
- `Not just software`
- `not running a proof-of-concept`
- `— not retrofitted` (use a comma instead)
- `there — standing side by side`
- `suggests that this process` (use "indicates")
- `field-proven processes`
- `right now.`

### Required UI elements
- `Intake` and `Research` must appear in `<nav>` text
- A `Talk to Us` button must exist
- A link containing `White Paper` or `Download` must exist
- The contact modal with `id="contactModal"` must exist

### Structural items tests enforce (`tests/test_html_structure.py`, `test_accessibility.py`)
- DOCTYPE, charset, viewport meta, `<title>`, Open Graph tags
- Skip link, ARIA roles, focus trap on modals, focus-visible CSS
- Hamburger button must have correct ARIA
- Form labels must be associated with inputs
- All decorative SVGs must have `aria-hidden`
- Media query breakpoints and touch target sizes on mobile

---

## What Is Off Limits

Do not change these without explicit authorization from the principals:

- **Legal/compliance copy** — privacy policy, terms, WOSB / Public Benefit Corp claims, compliance white paper content.
- **Formspree endpoint** (`formspree.io/f/xbdzzwqo`) and notification recipient list — routed through the Formspree account dashboard, not the HTML.
- **`CNAME` file** — controls the custom domain. Changing it takes the live site offline until DNS reconverges.
- **Research statistics** — `$4.6M`, `25%`, `36 nights`, `90 seconds`, `1977`. These are cited numbers tied to source material; don't round or revise them without a source update.
- **Partnership attribution** — SciLaw language and the Cameron County / Brownsville pilot framing.
- **CI workflow** (`.github/workflows/ci.yaml`) and the `tests/` directory — changing these silences the guardrails that protect the rest of this list.

---

## Key People

Derived from Formspree notification recipients and git history. If this is incomplete, update this section.

| Role | Contact |
|---|---|
| Principal (contact form notifications) | `kb@justiceinnovations.us` |
| Principal (contact form notifications) | `sd@justiceinnovations.us` |
| Research partner | SciLaw (see `#about-scilaw`) |
| Active pilot | Cameron County DA / Brownsville (see `#about-pilot`) |

Company location: San Antonio, TX.

---

## How to Make a Change Safely

1. **Pull latest:** `git pull`
2. **Back up** if the change is large: `cp index.html index_BACKUP_before_<change>.html`
3. **Locate the section** using the Section Map above, or:
   ```
   grep -n "distinctive phrase from the section" index.html
   ```
4. **Edit** `index.html`. Keep the change scoped to the smallest block that achieves the goal.
5. **Check against "What Is Fragile"** — make sure you haven't removed a required phrase, renamed a required ID, or reintroduced a forbidden phrase.
6. **Run the tests locally** (first-time setup: `pip install -r requirements-test.txt`):
   ```
   pytest tests/ -v
   ```
7. **Preview** — open `index.html` in a browser. Check the section you changed AND the sections above and below it (CSS can bleed).
8. **Commit** with a message that describes the *why*:
   ```
   git add index.html
   git commit -m "Short description of what changed and why"
   git push
   ```
9. **Verify the live site** after ~2 minutes: https://justiceinnovations.github.io/JI-Website/
10. **Check CI:** https://github.com/JusticeInnovations/JI-Website/actions — green check means tests passed.

If tests fail, read the failure — it almost always points directly at which phrase or ID broke the contract.

---

## How to Add a Research Paper

The research papers live in `#research-papers` (around line 1926). To add a paper:

1. Open `index.html` and find the `#research-papers` section.
2. Copy an existing paper card block as a template.
3. Replace the title, authors, journal/venue, year, and link.
4. Place the new card in reverse-chronological order (most recent first) unless a different ordering already exists in the section.
5. If the paper is a Justice Innovations white paper rather than an external publication, add it to the `#white-paper` block (line ~1987), not the general papers list.
6. Ensure external links have `target="_blank" rel="noopener"` — `tests/test_security.py` enforces this.
7. Run `pytest tests/ -v` and push.

---

## How to Update This Document

Update this file whenever any of the following happens:

- A new section is added to `index.html` → update the **Section Map**.
- A new test is added to `tests/` that enforces a copy / ID / fact → update **What Is Fragile**.
- A new principal or partner starts receiving Formspree emails → update **Key People**.
- Deployment model changes (custom domain, new hosting, build step introduced) → update **How the Site Works**.
- A new support file is added to the repo root → update **File Structure**.

Then bump the `Last updated` date at the top and commit with a message like `docs: update site architecture guide for <change>`.
