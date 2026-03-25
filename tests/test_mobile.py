"""Tests for mobile/device compatibility."""

import re

from bs4 import BeautifulSoup


def test_viewport_meta_no_user_scalable_no(soup: BeautifulSoup) -> None:
    """Must not prevent user zoom (accessibility requirement)."""
    viewport = soup.find("meta", attrs={"name": "viewport"})
    assert viewport is not None
    content = viewport.get("content", "")
    assert "user-scalable=no" not in content
    assert "maximum-scale=1" not in content


def test_responsive_breakpoints_defined(raw_html: str) -> None:
    """CSS must include media queries for mobile breakpoints."""
    assert "@media" in raw_html
    # Check for a mobile breakpoint
    assert re.search(r"@media[^{]*max-width\s*:\s*[47]\d{2}px", raw_html)


def test_mobile_nav_drawer_exists(soup: BeautifulSoup) -> None:
    mnav = soup.find(id="mobileNav")
    assert mnav is not None, "Mobile nav drawer #mobileNav not found"


def test_hamburger_button_exists(soup: BeautifulSoup) -> None:
    burger = soup.find(id="hamburgerBtn")
    assert burger is not None
    assert burger.name == "button"


def test_hero_h1_uses_clamp(raw_html: str) -> None:
    """h1 font size should use clamp() for responsive sizing."""
    assert re.search(r"h1\s*\{[^}]*clamp\(", raw_html, re.DOTALL)


def test_grid_collapses_on_mobile(raw_html: str) -> None:
    """Multi-column grids should collapse to single column on mobile."""
    # Grids (.g2/.g3/.g4) must have a 1fr responsive override somewhere
    assert re.search(
        r"\.(g2|g3|g4)[^{]*\{[^}]*grid-template-columns\s*:\s*1fr", raw_html
    ), "No 1fr grid-template-columns override found for .g2/.g3/.g4"


def test_touch_cta_buttons_exist(soup: BeautifulSoup) -> None:
    """Mobile nav must have a visible CTA button."""
    cta = soup.find(class_="mnav__cta")
    assert cta is not None
    assert cta.name == "button"


def test_overflow_x_handled_for_status_flow(raw_html: str) -> None:
    """Status flow diagram needs overflow-x: auto on small screens."""
    assert "overflow-x" in raw_html and "auto" in raw_html
