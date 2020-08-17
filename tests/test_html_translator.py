"""Unit tests for the html_translator module."""

from bs4 import BeautifulSoup
import pytest
from sphinx.application import Sphinx


def html_parse(filename: str) -> BeautifulSoup:
    """Parse the HTML5 output."""
    with open(filename) as file_handle:
        tree = BeautifulSoup(file_handle, "html.parser")
    return tree


@pytest.mark.sphinx("html", confoverrides={"html_theme": "sphinxawesome_theme"})
def test_permalinks(app: Sphinx) -> None:
    """It assigns an ID to notes (but not <desc>) in HTML."""
    app.builder.build_all()

    tree = html_parse(app.outdir / "index.html")
    headerlinks = tree("a", class_="headerlink")
    assert len(headerlinks) == 5
    assert (
        headerlinks[0]["title"]
        == "Copy link to section: Test the Python extension of the Sphinx Awesome Theme."
    )
    assert headerlinks[1]["title"] == "Copy link to section: Test Section."
    assert headerlinks[2]["title"] == "Copy link to this note."
    assert headerlinks[3]["title"] == "Permalink to this definition"
    assert headerlinks[4]["title"] == "Copy link to this code block."
