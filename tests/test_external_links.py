"""Test the construction of canonical links."""

import os
from pathlib import Path

import pytest
from sphinx.application import Sphinx

from .util import parse_html


@pytest.mark.sphinx(
    "html",
    testroot="external",
    confoverrides={
        "extensions": ["sphinxawesome_theme"],
        "html_theme": "sphinxawesome_theme",
    },
)
def test_no_external_link_icons(app: Sphinx) -> None:
    """It doesn't add canonical links by default."""
    app.build()
    assert os.path.exists(Path(app.outdir) / "index.html")
    tree = parse_html(Path(app.outdir) / "index.html")
    links = tree.select(".reference")
    assert len(links) == 3

    for a in links:
        icon = a("svg")
        assert len(icon) == 0


@pytest.mark.sphinx(
    "html",
    testroot="external",
    confoverrides={
        "extensions": ["sphinxawesome_theme"],
        "html_theme": "sphinxawesome_theme",
        "html_awesome_external_links": True,
    },
)
def test_external_link_icons(app: Sphinx) -> None:
    """It adds an external link icon to external references."""
    app.build()
    assert os.path.exists(Path(app.outdir) / "index.html")
    tree = parse_html(Path(app.outdir) / "index.html")

    icons = tree.select("a svg")
    assert len(icons) == 1
