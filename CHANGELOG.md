# Changelog

All notable changes to the Justice Innovations website are logged in this file.

Format based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Newest entries at the top. Each entry links to its commit in the repo.

---

## 2026-04-17

### Added
- **Site Architecture Guide** — `SITE-ARCHITECTURE.md` documenting section map, fragile copy/IDs enforced by CI tests, off-limits areas, key people, and step-by-step procedures for making changes safely and adding research papers. ([`4422517`](https://github.com/JusticeInnovations/JI-Website/commit/4422517))

### Changed
- **Hero paragraph rewrite** (Sasha's edit) — reframed the opening paragraph from "stopping bad cases before they start" to "Most cases are reviewed too late. *Intake* fixes that — putting prosecutors in the conversation before arrests, where case quality, costs, and outcomes are actually determined." ([`702ced1`](https://github.com/JusticeInnovations/JI-Website/commit/702ced1))

### Fixed
- **Company location corrected to San Antonio, TX** — updated 8 references in `index.html` (JSON-LD `foundingLocation`, About paragraph, About citation, footer copyright, and four legal-modal address blocks) from Houston to San Antonio. Preserved two intentional Houston references: the SciLaw partnership description (SciLaw is Houston-based) and the research paper title "Gendered Outcomes in Prostitution Arrests in Houston, Texas." Also updated `SITE-ARCHITECTURE.md` Key People section.

---

## 2026-04-10

### Changed
- **Login button now links directly to Back Office app** — replaced the desktop and mobile Login buttons (which opened a "Coming Soon" modal) with direct `<a>` links to `https://app.justiceinnovations.us`. Removed the login modal HTML and all associated JavaScript. Updated accessibility test to assert `<a>` with correct `href`. ([`5c7d97d`](https://github.com/JusticeInnovations/JI-Website/commit/5c7d97d))

---

## How to add a new entry

1. Add a new dated section at the top, under the most recent `---` divider.
2. Use `## YYYY-MM-DD` for the date heading.
3. Group changes under one of: `### Added`, `### Changed`, `### Fixed`, `### Removed`, `### Deprecated`, `### Security`.
4. Write one bullet per change. Lead with a short title in bold, follow with a one-sentence description, and link to the commit hash in backticks.
5. If multiple commits on the same day make related changes, group them into one bullet.
6. Commit with a message like `docs: log <change> in CHANGELOG`.
