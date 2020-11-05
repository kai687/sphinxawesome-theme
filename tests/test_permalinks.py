"""Unit tests for the permalink behavior."""

from typing import Dict

from bs4 import BeautifulSoup
import pytest
from sphinx.application import Sphinx


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
    "html",
    testroot="permalinks",
    confoverrides={"html_theme": "sphinxawesome_theme"},
    freshenv=True,
)
def test_labels_html(app: Sphinx) -> None:
    """It assigns an ID to notes automatically in HTML."""
    app.build()

    # tree = cached_parse(app.outdir / "index.html")
