"""Unit tests for the sphinxawesome_theme python extensions."""

import os

from bs4 import BeautifulSoup
import pytest
from sphinx.application import Sphinx
from sphinx.testing.util import etree_parse

from sphinxawesome_theme import __version__


def html_parse(filename: str) -> BeautifulSoup:
    """Parse the HTML5 output."""
    with open(filename) as file_handle:
        tree = BeautifulSoup(file_handle, "html.parser")
    return tree


def test_returns_version() -> None:
    """It has the correct version."""
    assert __version__ == "1.10.5"


@pytest.mark.sphinx("dummy")
def test_can_access_and_compile_test(app: Sphinx) -> None:
    """It compiles the basic test files."""
    app.builder.build_all()
    assert app.outdir.exists()
    assert not os.listdir(app.outdir)


@pytest.mark.sphinx("xml", confoverrides={"extensions": ["sphinxawesome_theme"]})
def test_compiles_xml(app: Sphinx) -> None:
    """It compiles XML."""
    app.builder.build_all()

    et = etree_parse(app.outdir / "index.xml")
    notes = et.findall(".//note")
    assert len(notes) == 1
    assert "id" not in notes[0].attrib


@pytest.mark.sphinx("html", confoverrides={"html_theme": "sphinxawesome_theme"})
def test_compiles_html(app: Sphinx) -> None:
    """It compiles HTML."""
    app.builder.build_all()

    tree = html_parse(app.outdir / "index.html")
    notes = tree.find_all("div", class_="note")
    assert len(notes) == 1
    assert notes[0]["id"] == "test-section-note-1"
    # <desc> nodes are also admonitions in Sphinx (sphinx.addnodes.desc)
    # but they should not get any ids
    dl = tree.find_all("dl")
    assert len(dl) == 1
    assert "id" not in dl[0]
