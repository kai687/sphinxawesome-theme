"""Test the construction of canonical links."""

import os
from pathlib import Path

import pytest
from sphinx.application import Sphinx

from .util import parse_html


@pytest.mark.sphinx(
    "html",
    confoverrides={
        "html_theme": "sphinxawesome_theme",
    },
)
def test_no_canonical_links_in_html(app: Sphinx) -> None:
    """It doesn't add canonical links by default."""
    app.build()
    assert os.path.exists(Path(app.outdir) / "index.html")
    tree = parse_html(Path(app.outdir) / "index.html")
    link = tree.select("[rel=canonical]")
    assert len(link) == 0


@pytest.mark.sphinx(
    "dirhtml",
    confoverrides={
        "html_theme": "sphinxawesome_theme",
    },
)
def test_no_canonical_links_in_dirhtml(app: Sphinx) -> None:
    """It doesn't add canonical links by default."""
    app.build()
    assert os.path.exists(Path(app.outdir) / "index.html")
    tree = parse_html(Path(app.outdir) / "index.html")
    link = tree.select("[rel=canonical]")
    assert len(link) == 0


@pytest.mark.sphinx(
    "html",
    confoverrides={
        "html_theme": "sphinxawesome_theme",
        "html_baseurl": "https://test.org",
    },
)
def test_canonical_links_in_html(app: Sphinx) -> None:
    """It adds the correct canonical link for the HTML builder."""
    app.build()
    assert os.path.exists(Path(app.outdir) / "index.html")
    tree = parse_html(Path(app.outdir) / "index.html")
    link = tree.select("[rel=canonical]")
    assert len(link) == 1
    assert link[0]["href"] == "https://test.org/index.html"


@pytest.mark.sphinx(
    "dirhtml",
    confoverrides={
        "html_theme": "sphinxawesome_theme",
        "html_baseurl": "https://test.org",
    },
)
def test_canonical_links_in_dirhtml(app: Sphinx) -> None:
    """It adds the correct canonical link for the DirectoryHTML builder."""
    app.build()
    assert os.path.exists(Path(app.outdir) / "index.html")
    tree = parse_html(Path(app.outdir) / "index.html")
    link = tree.select("[rel=canonical]")
    assert len(link) == 1
    assert link[0]["href"] == "https://test.org/"
