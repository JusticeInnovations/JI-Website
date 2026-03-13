[README (1).md](https://github.com/user-attachments/files/25978809/README.1.md)
# Justice Innovations — Marketing Website

> **Prosecutor-Guided Intake Technology** | justice.winningit.com

A single-page marketing website for Justice Innovations, presenting the company's AI-powered prosecutor-guided intake and case management platform to District Attorneys, law enforcement agencies, courts, and legislators — primarily in Texas.

---

## Overview

This is a static, single-file HTML site (`justice-innovations-v5.html`) designed for GitHub Pages deployment. It includes navigation, product sections, research references, role-based solution pages, and a contact/demo request modal.

---

## File Structure

```
/
└── justice-innovations-v5.html   # Entire site — HTML, CSS, and JS in one file
└── README.md                     # This file
```

No build tools, frameworks, or dependencies are required. The site is fully self-contained with the exception of Google Fonts (loaded via CDN).

---

## Sections

| Section | Anchor | Description |
|---|---|---|
| Home / Hero | `#top` | Tagline and primary CTA |
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

This site is designed for **GitHub Pages** with zero configuration.

### Steps

1. Push `justice-innovations-v5.html` (and this README) to the `main` branch of your repository.
2. In repository **Settings → Pages**, set the source to `main` branch, root `/`.
3. Rename `justice-innovations-v5.html` to `index.html` **or** configure GitHub Pages to serve the file directly.

> **Recommended:** Rename the file to `index.html` before pushing so the site loads at the root URL without requiring the filename in the path.

---

## Fonts

Loaded via Google Fonts CDN — no local assets required:

- **Cormorant Garamond** — headings / display
- **Outfit** — body / UI
- **DM Mono** — data / code elements

An internet connection is required to render fonts correctly.

---

## Customization

All styles are embedded in the `<style>` block at the top of the file. Key CSS variables control the color palette and can be updated in one place:

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

The site includes a contact/demo request modal triggered by CTA buttons throughout the page. To connect this to a live form backend, update the modal's form action or replace the inline handler with your preferred service (e.g., Formspree, Netlify Forms, or a custom endpoint).

---

## License

Proprietary. All content, design, and code are the property of Justice Innovations. Not licensed for redistribution or reuse without written permission.

---

*Built by Justice Innovations | Houston, TX*
