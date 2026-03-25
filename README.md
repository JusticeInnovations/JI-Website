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
└── index.html     # Entire site — HTML, CSS, and JS in one file
└── README.md      # This file
```

No build tools, frameworks, or dependencies are required. The site is fully self-contained with the exception of Google Fonts (loaded via CDN).

---

## Sections

| Section | Anchor | Description |
|---|---|---|
| Home / Hero | `#top` | Tagline and primary CTA with animated police light background |
| What Is Intake? | `#what-is-intake` | Product overview |
| How It Works | `#how-it-works` | Process walkthrough |
| Why a Prosecutor? | `#why-prosecutor` | Methodology rationale |
| Features & Platform | `#features` | Feature grid |
| Implementation Package | `#implementation` | Deployment details |
| What We Measure | `#what-we-measure` | Metrics & outcomes |
| Research | `#research` | Harris County Model, evidence base |
| Published Papers | `#research-papers` | Academic citations |
| White Papers | `#white-paper` | Methodology documents |
| Solutions by Role | `#solutions` | DA, Law Enforcement, Courts, Legislators |
| About | `#about` | Company info |
| Request a Demo | `#cta` | Contact form / modal |

---

## Deployment

Hosted on **GitHub Pages** from the `main` branch. Any file committed to `main` goes live automatically within 1-2 minutes.

### Updating the Site
1. Make changes to `index.html`
2. Upload the updated file to the repo via **Add file → Upload files**
3. Click **Commit changes**
4. Wait 1-2 minutes and refresh the live URL

---

## Fonts

Loaded via Google Fonts CDN — no local assets required:

- **Cormorant Garamond** — headings / display
- **Outfit** — body / UI
- **DM Mono** — data / code elements

---

## Customization

All styles are embedded in the `<style>` block at the top of `index.html`. Key CSS variables control the color palette:

```css
:root {
  --navy:        #0D1F35;
  --electric:    #1B6FE8;
  --electric-lt: #4D9BFF;
  --gold:        #D4AA50;
  /* ... */
}
```

---

## Contact & Demo Requests

The site includes a contact/demo request modal triggered by **Talk to Us** and **Request Demo** CTA buttons throughout the page. Form submissions are handled via **Formspree** (endpoint: `https://formspree.io/f/xbdzzwqo`) and delivered by email to `kb@justiceinnovations.us` and `sd@justiceinnovations.us`. No email client is required on the visitor's end.

To update the notification recipients, log in to [formspree.io](https://formspree.io) with the Justice Innovations account.

---

## License

Proprietary. All content, design, and code are the property of Justice Innovations. Not licensed for redistribution or reuse without written permission.

---

*Built by Justice Innovations | Houston, TX*
