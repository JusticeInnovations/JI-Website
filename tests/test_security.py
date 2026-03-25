"""Tests for basic security hygiene in the static site."""

import re

from bs4 import BeautifulSoup


def test_external_links_have_noopener(soup: BeautifulSoup) -> None:
    violations = []
    for a in soup.find_all("a", href=True, target="_blank"):
        rel = a.get("rel") or []
        if isinstance(rel, str):
            rel = rel.split()
        if "noopener" not in rel:
            violations.append(a.get("href", ""))
    assert not violations, f"External _blank links missing rel=noopener: {violations}"


def test_no_javascript_hrefs(soup: BeautifulSoup) -> None:
    """No links should use javascript: protocol."""
    js_links = [
        a["href"]
        for a in soup.find_all("a", href=True)
        if a["href"].strip().lower().startswith("javascript:")
    ]
    assert not js_links, f"Found javascript: href(s): {js_links}"


def test_no_inline_event_handlers_on_anchors(soup: BeautifulSoup) -> None:
    """Anchor tags must not use href='#' as modal triggers (use buttons)."""
    violations = [
        str(a)[:120] for a in soup.find_all("a", href="#") if a.get("onclick")
    ]
    assert (
        not violations
    ), f"Anchor tags used as button triggers (use <button>): {violations}"


def test_form_uses_https_endpoint(raw_html: str) -> None:
    """Contact form must POST to an HTTPS endpoint."""
    assert re.search(
        r"https://formspree\.io/", raw_html
    ), "Formspree endpoint not found or not HTTPS"


def test_no_sensitive_data_in_html(raw_html: str) -> None:
    """Check for obvious credential patterns."""
    patterns = [
        r"password\s*=\s*['\"][^'\"]{4,}",
        r"api[_-]?key\s*=\s*['\"][^'\"]{8,}",
        r"secret\s*=\s*['\"][^'\"]{8,}",
        r"aws[_-]?access[_-]?key",
    ]
    for pattern in patterns:
        assert not re.search(
            pattern, raw_html, re.IGNORECASE
        ), f"Possible sensitive data found matching: {pattern}"


def test_formspree_id_is_expected_format(raw_html: str) -> None:
    """Formspree form IDs follow a known pattern."""
    match = re.search(r"formspree\.io/f/([a-zA-Z0-9]+)", raw_html)
    assert match is not None, "Formspree endpoint not found"
    form_id = match.group(1)
    assert len(form_id) >= 6, f"Formspree ID '{form_id}' looks malformed"
