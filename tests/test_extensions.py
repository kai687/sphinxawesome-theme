"""Test the loading of the awesome extensions."""

import os
import re
from pathlib import Path

import pytest
from sphinx.application import Sphinx

from .util import parse_html


@pytest.mark.sphinx(
    "html",
    confoverrides={
        "html_theme": "sphinxawesome_theme",
        "extensions": ["sphinx_design"],
    },
)
def test_awesome_sphinx_design(app: Sphinx) -> None:
    """It loads CSS for the `sphinx-design` extension."""
    app.build()
    assert os.path.exists(Path(app.outdir) / "index.html")
    tree = parse_html(Path(app.outdir) / "index.html")
    pattern = re.compile(r"awesome-sphinx-design.(css|js)")

    # It adds the `awesome-sphinx-design.css` file
    css = tree.select('link[rel="stylesheet"]')
    assert len(css) == 4
    hrefs = [item["href"] for item in css]
    assert any(filter(pattern.search, hrefs))  # type: ignore[arg-type]


@pytest.mark.sphinx(
    "html",
    confoverrides={
        "html_theme": "sphinxawesome_theme",
        "extensions": ["myst_nb"],
    },
)
def test_awesome_myst_nb(app: Sphinx) -> None:
    """It loads CSS for the `myst-nb` extension."""
    app.build()
    assert os.path.exists(Path(app.outdir) / "index.html")
    tree = parse_html(Path(app.outdir) / "index.html")
    pattern = re.compile(r"awesome-myst-nb.css")

    # It adds the `awesome-myst-nb.css` file
    css = tree.select('link[rel="stylesheet"]')
    assert len(css) == 4
    hrefs = [item["href"] for item in css]
    assert any(filter(pattern.search, hrefs))  # type: ignore[arg-type]
