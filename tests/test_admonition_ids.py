"""Unit tests for the admonition_id module."""
import os
from typing import Dict

import pytest
from bs4 import BeautifulSoup
from sphinx.application import Sphinx
from sphinx.testing.util import etree_parse

etree_cache: Dict[str, BeautifulSoup] = {}


def cached_parse(filename: str) -> BeautifulSoup:
    """Parse an HTML file and store the parsed tree in a dictionary."""
    if filename in etree_cache:
        return etree_cache[filename]

    with open(filename) as file_handle:
        tree = BeautifulSoup(file_handle, "html.parser")
        etree_cache.clear()
        etree_cache[filename] = tree
        return tree


@pytest.mark.sphinx(
    "xml", testroot="ids", confoverrides={"extensions": ["sphinxawesome_theme"]}
)
def test_does_not_assign_id_in_xml(app: Sphinx) -> None:
    """It does not assign an ID automatically in XML."""
    app.build()

    et = etree_parse(os.path.join(app.outdir, "index.xml"))
    notes = et.findall(".//note")
    assert len(notes) == 3

    assert "ids" not in notes[0].attrib
    assert "ids" not in notes[1].attrib
    assert "ids" in notes[2].attrib
    # explicitly referenced notes should have an id though
    assert notes[2].attrib["ids"] == "foo"


@pytest.mark.sphinx(
    "html",
    testroot="ids",
    confoverrides={"html_theme": "sphinxawesome_theme"},
    freshenv=True,
)
def test_assign_id_in_html(app: Sphinx) -> None:
    """It assigns an ID to notes automatically in HTML."""
    app.build()

    tree = cached_parse(os.path.join(app.outdir, "index.html"))

    notes = tree.find_all("div", class_="note")
    assert len(notes) == 3

    # first note is not inside a section
    assert notes[0]["id"] == "undefined-note-1"
    # second note is inside a section 'Test'
    assert notes[1]["id"] == "test-note-2"
    # third note has an explicit label ``foo``
    assert notes[2]["id"] == "foo"


@pytest.mark.sphinx(
    "html",
    testroot="ids",
    confoverrides={"html_theme": "sphinxawesome_theme"},
    freshenv=True,
)
def test_does_not_assign_id_to_desc(app: Sphinx) -> None:
    """It doesn't assign an ID to a description node."""
    app.build()

    tree = cached_parse(os.path.join(app.outdir, "index.html"))
    dl = tree.find_all("dl")
    assert len(dl) == 1
    assert "id" not in dl[0]
