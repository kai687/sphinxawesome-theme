"""Tests for external_links.

External links should have an icon.
Internal links should not.
"""
from pathlib import Path

import pytest
from sphinx.application import Sphinx

from .util import parse_html


@pytest.mark.sphinx(
    "html",
    testroot="external-links",
    freshenv=True,
    confoverrides={"html_theme": "sphinxawesome_theme"},
)
def test_external_links(app: Sphinx) -> None:
    """It distinguishes internal and external links correctly."""
    app.build()
    tree = parse_html(Path(app.outdir) / "index.html")
    section = tree("section", attrs={"id": "test"})
    assert len(section) == 1
    internal = section[0].find_all("a", class_="internal")
    assert len(internal) == 1
    assert internal[0].attrs["href"] == "#foo"
    icon = internal[0].find_all("svg", class_="external-link-icon")
    assert len(icon) == 0

    external = section[0].find_all("a", class_="external")
    assert len(external) == 1
    assert external[0].attrs["href"] == "https://example.com"
    icon = external[0].find_all("svg", class_="external-link-icon")
    assert len(icon) == 1
