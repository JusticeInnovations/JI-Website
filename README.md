# Justice Innovations — Marketing Website

[![CI](https://github.com/JusticeInnovations/JI-Website/actions/workflows/ci.yaml/badge.svg)](https://github.com/JusticeInnovations/JI-Website/actions/workflows/ci.yaml)
[![Tests](https://img.shields.io/badge/tests-88%20passing-brightgreen)](https://github.com/JusticeInnovations/JI-Website/actions/workflows/ci.yaml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![WCAG 2.1 AA](https://img.shields.io/badge/accessibility-WCAG%202.1%20AA-blue)](https://www.w3.org/WAI/WCAG21/quickref/)
[![GitHub Pages](https://img.shields.io/badge/hosted-GitHub%20Pages-222?logo=github)](https://justiceinnovations.github.io/JI-Website/)

> **Prosecutor-Guided Intake Technology** | https://justiceinnovations.github.io/JI-Website/

A single-page marketing website for Justice Innovations, presenting the company's prosecutor-guided intake and case management platform to District Attorneys, law enforcement agencies, courts, and legislators — primarily in Texas.

---

## Live Site

**https://justiceinnovations.github.io/JI-Website/**

---

## File Structure

```
/
├── index.html                        # Entire site — HTML, CSS, and JS in one file
├── social-preview.svg                # 1200×630 Open Graph image for social sharing
├── requirements-test.txt             # Python test dependencies
├── pyproject.toml                    # pytest, black, and ruff configuration
├── README.md                         # This file
├── .github/
│   └── workflows/
│       └── ci.yaml                   # GitHub Actions CI pipeline
└── tests/
    ├── conftest.py                   # pytest fixtures (soup, raw_html)
    ├── test_html_structure.py        # 18 tests — DOCTYPE, meta, headings, structure
    ├── test_accessibility.py         # 24 tests — WCAG, ARIA, focus, modals
    ├── test_content.py               # 32 tests — copy, statistics, sections
    ├── test_mobile.py                # 8 tests — viewport, breakpoints, touch targets
    └── test_security.py              # 6 tests — noopener, HTTPS, no credentials
```

No build tools, frameworks, or runtime dependencies are required. The site is fully self-contained with the exception of Google Fonts (loaded via CDN).

---

## Sections

| Section | Anchor | Description |
|---|---|---|
| Home / Hero | `#top` | Tagline and primary CTA with animated police light background |
| What Is Intake? | `#what-is-intake` | Product overview, officer quote, $4.6M stat |
| Why a Prosecutor? | `#why-prosecutor` | Methodology rationale |
| How It Works | `#how-it-works` | 4-step process walkthrough |
| Features & Platform | `#features` | Feature card grid |
| Implementation Package | `#implementation` | 3-phase deployment timeline |
| What We Measure | `#what-we-measure` | Metrics & outcomes |
| Research | `#research` | Harris County Model, evidence base |
| Cost of Doing Nothing | `#research-data` | Statistical cost analysis |
| Published Papers | `#research-papers` | Academic citations |
| White Paper | `#white-paper` | Security & compliance documentation |
| Solutions by Role | `#solutions` | Overview for all audiences |
| — District Attorneys | `#solutions-da` | DA / Prosecutor role view |
| — Law Enforcement | `#solutions-le` | Law enforcement role view |
| — Courts & Judges | `#solutions-courts` | Courts role view |
| — Legislators & Policy | `#solutions-policy` | Policy role view |
| About | `#about` | Company mission and overview |
| SciLaw Partnership | `#about-scilaw` | Research partner details |
| Cameron County Pilot | `#about-pilot` | Live pilot program |
| Request a Demo | `#cta` | Final CTA |

---

## Deployment

Hosted on **GitHub Pages** from the `main` branch. Any commit to `main` goes live automatically within 1–2 minutes.

### Updating the Site

```bash
# Make changes to index.html, then:
git add index.html
git commit -m "Description of change"
git push origin main
```

The CI pipeline runs automatically on push. If all checks pass, the site deploys. If any test fails, the push is flagged in the Actions tab.

---

## Testing

Tests require Python 3.11+ and the packages in `requirements-test.txt`.

```bash
# Install dependencies
pip install -r requirements-test.txt

# Run all 88 tests
pytest tests/ -v

# Run a specific file
pytest tests/test_accessibility.py -v
```

### Test files

| File | Tests | What it checks |
|---|---|---|
| `test_html_structure.py` | 18 | DOCTYPE, charset, viewport, title, meta, OG tags, headings, landmarks |
| `test_accessibility.py` | 24 | Skip link, ARIA roles, focus trap, hamburger ARIA, form labels, SVG aria-hidden, focus-visible CSS, reduced motion |
| `test_content.py` | 32 | Copy accuracy, key statistics, required section IDs, navigation structure |
| `test_mobile.py` | 8 | Viewport meta, media query breakpoints, grid collapse, touch targets |
| `test_security.py` | 6 | External link safety, no javascript: hrefs, HTTPS form endpoint, no credentials in HTML |

---

## CI/CD

GitHub Actions runs on every push to `main` and every pull request:

1. **Black** — format check (`black --check tests/`)
2. **Ruff** — lint (`ruff check tests/`)
3. **pytest** — full test suite (`pytest tests/ -v --tb=short`)

See `.github/workflows/ci.yaml` for the full pipeline definition.

---

## Fonts

Loaded via Google Fonts CDN — no local assets required:

- **Cormorant Garamond** — headings, display text, statistics
- **Outfit** — body text, navigation, buttons, forms
- **DM Mono** — section labels, monospace tags, mockup UI

---

## Customization

All styles are embedded in the `<style>` block at the top of `index.html`. Key CSS custom properties control the color palette and layout:

```css
:root {
  /* Colors */
  --blue:        #0D1F35;   /* Primary navy */
  --electric:    #1B6FE8;   /* Brand blue */
  --electric-lt: #3D8EFF;   /* Light blue */
  --teal-lt:     #00C2D4;   /* Teal accent */
  --gold:        #D4860A;   /* Gold accent */
  --red-lt:      #FF6B6B;   /* Coral red — section labels */

  /* Layout */
  --px: 48px;    /* Horizontal padding */
  --py: 96px;    /* Vertical padding */
  --mw: 1280px;  /* Max content width */
  --nh: 116px;   /* Nav height */
}
```

---

## Contact & Demo Requests

The site includes a contact/demo request modal triggered by **Talk to Us** and **Request Demo** buttons throughout the page. Submissions POST to **Formspree** (`https://formspree.io/f/xbdzzwqo`) and are delivered by email to `kb@justiceinnovations.us` and `sd@justiceinnovations.us`. No server or email client is required on the visitor's end.

To update notification recipients, log in to [formspree.io](https://formspree.io) with the Justice Innovations account.

---

## License

Proprietary. All content, design, and code are the property of Justice Innovations. Not licensed for redistribution or reuse without written permission.

---

*Built by Justice Innovations | Houston, TX*
