"""Tests for core HTML document structure."""

from bs4 import BeautifulSoup


def test_doctype_present(raw_html: str) -> None:
    assert raw_html.strip().lower().startswith("<!doctype html")


def test_html_lang_attribute(soup: BeautifulSoup) -> None:
    html_tag = soup.find("html")
    assert html_tag is not None
    assert html_tag.get("lang") == "en"


def test_charset_meta(soup: BeautifulSoup) -> None:
    charset = soup.find("meta", attrs={"charset": True})
    assert charset is not None
    assert charset["charset"].upper() == "UTF-8"


def test_viewport_meta(soup: BeautifulSoup) -> None:
    viewport = soup.find("meta", attrs={"name": "viewport"})
    assert viewport is not None
    content = viewport.get("content", "")
    assert "width=device-width" in content
    assert "initial-scale=1" in content


def test_title_present(soup: BeautifulSoup) -> None:
    title = soup.find("title")
    assert title is not None
    assert "Justice Innovations" in title.get_text()


def test_meta_description(soup: BeautifulSoup) -> None:
    desc = soup.find("meta", attrs={"name": "description"})
    assert desc is not None, "Missing <meta name='description'>"
    assert len(desc.get("content", "")) >= 50, "Meta description too short"


def test_og_title(soup: BeautifulSoup) -> None:
    og_title = soup.find("meta", attrs={"property": "og:title"})
    assert og_title is not None
    assert "Justice Innovations" in og_title.get("content", "")


def test_og_description(soup: BeautifulSoup) -> None:
    og_desc = soup.find("meta", attrs={"property": "og:description"})
    assert og_desc is not None
    assert len(og_desc.get("content", "")) >= 50


def test_favicon_present(soup: BeautifulSoup) -> None:
    icon = soup.find("link", attrs={"rel": lambda r: r and "icon" in r})
    assert icon is not None


def test_h1_exists_once(soup: BeautifulSoup) -> None:
    h1_tags = soup.find_all("h1")
    assert len(h1_tags) == 1, f"Expected exactly 1 <h1>, found {len(h1_tags)}"


def test_h2_tags_exist(soup: BeautifulSoup) -> None:
    assert len(soup.find_all("h2")) >= 5


def test_nav_element_exists(soup: BeautifulSoup) -> None:
    assert soup.find("nav") is not None


def test_main_element_exists(soup: BeautifulSoup) -> None:
    main = soup.find("main")
    assert main is not None


def test_main_has_id(soup: BeautifulSoup) -> None:
    main = soup.find("main")
    assert main is not None
    assert main.get("id") == "main-content"


def test_footer_exists(soup: BeautifulSoup) -> None:
    assert soup.find("footer") is not None


def test_internal_anchor_links_resolve(soup: BeautifulSoup) -> None:
    """Every href='#anchor' must correspond to an id on the page."""
    all_ids = {tag.get("id") for tag in soup.find_all(id=True)}
    broken = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href.startswith("#") and href != "#":
            target = href[1:]
            if target not in all_ids:
                broken.append(href)
    assert not broken, f"Broken internal anchor links: {broken}"


def test_external_links_have_noopener(soup: BeautifulSoup) -> None:
    """External links that open in a new tab must have rel='noopener'."""
    violations = []
    for a in soup.find_all("a", href=True, target="_blank"):
        rel = a.get("rel") or []
        if "noopener" not in rel:
            violations.append(a.get("href"))
    assert not violations, f"External links missing rel=noopener: {violations}"


def test_google_fonts_preconnect(soup: BeautifulSoup) -> None:
    preconnects = soup.find_all("link", attrs={"rel": "preconnect"})
    hrefs = [p.get("href", "") for p in preconnects]
    assert any("fonts.googleapis.com" in h for h in hrefs)
