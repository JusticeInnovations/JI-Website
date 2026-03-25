"""Shared fixtures for the JI website test suite."""

from pathlib import Path

import pytest
from bs4 import BeautifulSoup


@pytest.fixture(scope="session")
def html_path() -> Path:
    return Path(__file__).parent.parent / "index.html"


@pytest.fixture(scope="session")
def soup(html_path: Path) -> BeautifulSoup:
    with open(html_path, encoding="utf-8") as f:
        return BeautifulSoup(f.read(), "html5lib")


@pytest.fixture(scope="session")
def raw_html(html_path: Path) -> str:
    with open(html_path, encoding="utf-8") as f:
        return f.read()
