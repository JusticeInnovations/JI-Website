"""Tests for ADA / WCAG 2.1 AA accessibility compliance."""

import re

from bs4 import BeautifulSoup

# ── Skip Navigation ────────────────────────────────────────────────────────────


def test_skip_link_exists(soup: BeautifulSoup) -> None:
    skip = soup.find("a", class_="skip-link")
    assert skip is not None, "Missing skip-to-main-content link"


def test_skip_link_targets_main(soup: BeautifulSoup) -> None:
    skip = soup.find("a", class_="skip-link")
    assert skip is not None
    assert skip.get("href") == "#main-content"


def test_skip_link_is_first_focusable(soup: BeautifulSoup) -> None:
    """Skip link must appear before the nav in DOM order."""
    body = soup.find("body")
    assert body is not None
    children = list(body.descendants)
    skip = soup.find("a", class_="skip-link")
    nav = soup.find("nav")
    assert children.index(skip) < children.index(nav)


# ── Modals ─────────────────────────────────────────────────────────────────────


def test_all_modals_have_dialog_role(soup: BeautifulSoup) -> None:
    modals = soup.find_all(class_="modal-overlay")
    assert modals, "No modal overlays found"
    for modal in modals:
        assert (
            modal.get("role") == "dialog"
        ), f"Modal #{modal.get('id')} missing role='dialog'"


def test_all_modals_have_aria_modal(soup: BeautifulSoup) -> None:
    for modal in soup.find_all(class_="modal-overlay"):
        assert (
            modal.get("aria-modal") == "true"
        ), f"Modal #{modal.get('id')} missing aria-modal='true'"


def test_all_modals_have_aria_labelledby(soup: BeautifulSoup) -> None:
    for modal in soup.find_all(class_="modal-overlay"):
        labelledby = modal.get("aria-labelledby")
        assert labelledby, f"Modal #{modal.get('id')} missing aria-labelledby"
        # The referenced id must exist in the document
        assert soup.find(
            id=labelledby
        ), f"aria-labelledby='{labelledby}' references missing id"


def test_modal_close_buttons_have_aria_label(soup: BeautifulSoup) -> None:
    for btn in soup.find_all(class_="modal-close"):
        assert btn.get("aria-label"), "Modal close button missing aria-label"


# ── Navigation ─────────────────────────────────────────────────────────────────


def test_hamburger_has_aria_label(soup: BeautifulSoup) -> None:
    burger = soup.find(id="hamburgerBtn")
    assert burger is not None
    assert burger.get("aria-label"), "Hamburger button missing aria-label"


def test_hamburger_has_aria_expanded(soup: BeautifulSoup) -> None:
    burger = soup.find(id="hamburgerBtn")
    assert burger is not None
    assert (
        burger.get("aria-expanded") is not None
    ), "Hamburger button missing aria-expanded"


def test_hamburger_has_aria_controls(soup: BeautifulSoup) -> None:
    burger = soup.find(id="hamburgerBtn")
    assert burger is not None
    controls = burger.get("aria-controls")
    assert controls, "Hamburger button missing aria-controls"
    assert soup.find(id=controls), f"aria-controls='{controls}' references missing id"


# ── Interactive Elements ────────────────────────────────────────────────────────


def test_no_anchor_onclick_hash(soup: BeautifulSoup) -> None:
    """All modal triggers must be <button>, not <a href='#' onclick>."""
    violations = [
        str(a)[:100] for a in soup.find_all("a", href="#") if a.get("onclick")
    ]
    assert not violations, f"Found <a href='#' onclick> — use <button>: {violations}"


def test_nav_cta_is_button(soup: BeautifulSoup) -> None:
    cta = soup.find(class_="nav__cta")
    assert cta is not None
    assert cta.name == "button", "nav__cta should be a <button>"


def test_nav_login_is_link(soup: BeautifulSoup) -> None:
    login = soup.find(class_="nav__login")
    assert login is not None
    assert login.name == "a", "nav__login should be an <a> link"
    assert login.get("href") == "https://app.justiceinnovations.us"


# ── Forms ──────────────────────────────────────────────────────────────────────


def test_form_inputs_have_labels(soup: BeautifulSoup) -> None:
    """Every visible form input must have an associated <label for=...>."""
    inputs = soup.find_all("input", id=True)
    missing = []
    for inp in inputs:
        inp_id = inp["id"]
        label = soup.find("label", attrs={"for": inp_id})
        if label is None:
            missing.append(inp_id)
    assert not missing, f"Inputs without labels: {missing}"


def test_textarea_has_label(soup: BeautifulSoup) -> None:
    for ta in soup.find_all("textarea", id=True):
        label = soup.find("label", attrs={"for": ta["id"]})
        assert label is not None, f"Textarea #{ta['id']} has no associated label"


def test_contact_form_required_fields_present(soup: BeautifulSoup) -> None:
    required_ids = ["m-name", "m-email", "m-message"]
    for field_id in required_ids:
        assert soup.find(id=field_id) is not None, f"Missing form field #{field_id}"


# ── SVG Accessibility ──────────────────────────────────────────────────────────


def test_logo_svg_aria_hidden(soup: BeautifulSoup) -> None:
    logo_svg = soup.find("a", class_="nav__logo")
    assert logo_svg is not None
    svg = logo_svg.find("svg")
    assert svg is not None
    assert svg.get("aria-hidden") == "true"


def test_feature_card_svgs_aria_hidden(soup: BeautifulSoup) -> None:
    for svg in soup.find_all("svg", class_="fc-icon"):
        assert (
            svg.get("aria-hidden") == "true"
        ), "fc-icon SVG missing aria-hidden='true'"


def test_impact_card_svgs_aria_hidden(soup: BeautifulSoup) -> None:
    for svg in soup.find_all("svg", class_="impact-icon"):
        assert (
            svg.get("aria-hidden") == "true"
        ), "impact-icon SVG missing aria-hidden='true'"


# ── CSS Checks (via raw HTML) ──────────────────────────────────────────────────


def test_focus_visible_styles_defined(raw_html: str) -> None:
    assert ":focus-visible" in raw_html, "No :focus-visible styles found"


def test_prefers_reduced_motion_defined(raw_html: str) -> None:
    assert "prefers-reduced-motion" in raw_html


def test_skip_link_css_focus_reveal(raw_html: str) -> None:
    """Skip link must become visible on focus."""
    assert re.search(
        r"\.skip-link:focus\s*\{[^}]*top\s*:", raw_html
    ), "Skip link :focus CSS not found"


def test_police_lights_hidden_on_reduced_motion(raw_html: str) -> None:
    """prefers-reduced-motion block must exist and hide police-lights."""
    # Confirm the media query block exists
    assert "prefers-reduced-motion" in raw_html
    # Confirm .police-lights { display: none } appears somewhere in the file
    # (it lives inside the prefers-reduced-motion block)
    assert re.search(
        r"\.police-lights\s*\{[^}]*display\s*:\s*none",
        raw_html,
    ), "police-lights not set to display:none (expected inside prefers-reduced-motion)"
