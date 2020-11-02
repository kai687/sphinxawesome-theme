"""Unit tests for the admonition_id module."""

from bs4 import BeautifulSoup
import pytest
from sphinx.application import Sphinx
from sphinx.testing.util import etree_parse


def html_parse(filename: str) -> BeautifulSoup:
    """Parse the HTML5 output."""
    with open(filename) as file_handle:
        tree = BeautifulSoup(file_handle, "html.parser")
    return tree


@pytest.mark.sphinx("xml", confoverrides={"extensions": ["sphinxawesome_theme"]})
def test_does_not_assign_id_in_xml(app: Sphinx) -> None:
    """It does not assign an ID in XML."""
    app.build()

    et = etree_parse(app.outdir / "index.xml")
    notes = et.findall(".//note")
    assert len(notes) == 2
    for note in notes:
        assert "id" not in note.attrib


@pytest.mark.sphinx("html", confoverrides={"html_theme": "sphinxawesome_theme"})
def test_assigns_id_in_html(app: Sphinx) -> None:
    """It assigns an ID to notes (but not <desc>) in HTML."""
    app.build()

    tree = html_parse(app.outdir / "index.html")
    notes = tree.find_all("div", class_="note")
    assert len(notes) == 2
    # first note is not inside section
    assert notes[0]["id"] == "undefined-note-1"
    assert notes[1]["id"] == "test-section-note-2"
    # <desc> nodes are also admonitions in Sphinx (sphinx.addnodes.desc)
    # but they should not get any ids
    dl = tree.find_all("dl")
    assert len(dl) == 1
    assert "id" not in dl[0]
