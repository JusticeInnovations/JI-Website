"""Tests verifying David Eagleman's editorial edits and copy accuracy."""

from bs4 import BeautifulSoup

# ── Contrastive Constructions Removed ─────────────────────────────────────────


def test_no_is_not_a_theory(raw_html: str) -> None:
    assert "is not a theory" not in raw_html


def test_no_not_a_new_idea(raw_html: str) -> None:
    assert "not a new idea" not in raw_html


def test_no_science_is_not_a_footnote(raw_html: str) -> None:
    assert "science is not a footnote" not in raw_html


def test_no_not_just_software(raw_html: str) -> None:
    assert "Not just software" not in raw_html


def test_no_not_running_proof_of_concept(raw_html: str) -> None:
    assert "not running a proof-of-concept" not in raw_html


def test_no_not_retrofitted_em_dash(raw_html: str) -> None:
    """'not retrofitted' should use a comma, not an em-dash."""
    assert "&mdash; not retrofitted" not in raw_html
    assert "— not retrofitted" not in raw_html


# ── Specific Copy Edits Applied ────────────────────────────────────────────────


def test_intake_intro_no_there_standing(raw_html: str) -> None:
    """'there — standing side by side' should be simplified."""
    assert "there &mdash; standing side by side" not in raw_html
    assert "there — standing side by side" not in raw_html


def test_research_indicates_not_suggests(soup: BeautifulSoup) -> None:
    text = soup.get_text()
    assert "indicates that this process" in text
    assert "suggests that this process" not in text


def test_harris_county_they_run(soup: BeautifulSoup) -> None:
    text = soup.get_text()
    assert "They run the most efficient prosecution office" in text


def test_justice_innovations_has_built(soup: BeautifulSoup) -> None:
    text = soup.get_text()
    assert "Justice Innovations has built the software" in text


def test_features_no_field_proven(raw_html: str) -> None:
    assert "field-proven processes" not in raw_html


def test_publications_tagline(soup: BeautifulSoup) -> None:
    """Publications section tagline should be 'The science.' not longer."""
    h2s = [h.get_text(strip=True) for h in soup.find_all("h2")]
    assert "The science." in h2s, f"'The science.' not found in h2 tags: {h2s}"


def test_cost_of_doing_nothing_no_right_now(raw_html: str) -> None:
    assert "right now." not in raw_html


def test_no_action_uses_parentheses(soup: BeautifulSoup) -> None:
    text = soup.get_text()
    assert "(someone who should never have been arrested)" in text


def test_equity_accountability_comma(raw_html: str) -> None:
    assert "from day one, not retrofitted" in raw_html


def test_harris_county_model_revised(soup: BeautifulSoup) -> None:
    text = soup.get_text()
    assert "results of over four decades in Harris County are unambiguous" in text


def test_harris_county_near_zero_phrasing(soup: BeautifulSoup) -> None:
    text = soup.get_text()
    assert "Harris County is near zero" in text


def test_cameron_county_pilot_positive_framing(soup: BeautifulSoup) -> None:
    text = soup.get_text()
    assert "structured as a rigorously designed evaluation" in text


# ── Key Facts & Statistics ─────────────────────────────────────────────────────


def test_cameron_county_savings_stat(soup: BeautifulSoup) -> None:
    text = soup.get_text()
    assert "$4.6M" in text


def test_pretrial_reduction_stat(soup: BeautifulSoup) -> None:
    text = soup.get_text()
    assert "25%" in text


def test_average_call_length(soup: BeautifulSoup) -> None:
    text = soup.get_text()
    assert "90" in text  # 90 seconds average call


def test_no_action_nights(soup: BeautifulSoup) -> None:
    text = soup.get_text()
    assert "36" in text  # 36 avg nights in jail


def test_harris_county_since_1977(soup: BeautifulSoup) -> None:
    text = soup.get_text()
    assert "1977" in text


def test_pilot_agencies_mentioned(soup: BeautifulSoup) -> None:
    text = soup.get_text()
    assert "Cameron County" in text
    assert "Brownsville" in text


def test_offense_types_covered(soup: BeautifulSoup) -> None:
    text = soup.get_text()
    assert "DUI" in text
    assert "Domestic Violence" in text


def test_wosb_certification_mentioned(soup: BeautifulSoup) -> None:
    text = soup.get_text()
    assert "Woman-Owned" in text or "WOSB" in text


def test_public_benefit_corp(soup: BeautifulSoup) -> None:
    text = soup.get_text()
    assert "Public Benefit" in text


# ── Navigation Structure ───────────────────────────────────────────────────────


def test_nav_has_product_section(soup: BeautifulSoup) -> None:
    nav_text = soup.find("nav").get_text()
    assert "Intake" in nav_text


def test_nav_has_research_section(soup: BeautifulSoup) -> None:
    nav_text = soup.find("nav").get_text()
    assert "Research" in nav_text


def test_nav_has_talk_to_us(soup: BeautifulSoup) -> None:
    buttons = [b.get_text(strip=True) for b in soup.find_all("button")]
    assert any("Talk to Us" in b for b in buttons)


# ── Sections Present ───────────────────────────────────────────────────────────


REQUIRED_SECTION_IDS = [
    "what-is-intake",
    "why-prosecutor",
    "features",
    "implementation",
    "what-we-measure",
    "research",
    "solutions",
    "about",
]


def test_required_sections_present(soup: BeautifulSoup) -> None:
    missing = [sid for sid in REQUIRED_SECTION_IDS if not soup.find(id=sid)]
    assert not missing, f"Missing required section IDs: {missing}"


def test_contact_form_present(soup: BeautifulSoup) -> None:
    assert soup.find(id="contactModal") is not None


def test_white_paper_download_link(soup: BeautifulSoup) -> None:
    links = [a.get_text(strip=True) for a in soup.find_all("a")]
    assert any("White Paper" in lnk or "Download" in lnk for lnk in links)
