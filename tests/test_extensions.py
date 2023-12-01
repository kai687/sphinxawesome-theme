"""Test the loading of the awesome extensions."""

import os
import re
from pathlib import Path

import pytest
from sphinx.application import Sphinx

from .util import parse_html


@pytest.mark.sphinx("html", confoverrides={"html_theme": "sphinxawesome_theme"})
def test_compiles_html_with_theme(app: Sphinx) -> None:
    """It compiles HTML with the theme but doesn't load the extra extensions."""
    app.build()
    assert os.path.exists(Path(app.outdir) / "index.html")
    assert app.config.html_theme == "sphinxawesome_theme"

    assert "sphinxawesome_theme.highlighting" not in app.extensions


@pytest.mark.sphinx(
    "html",
    confoverrides={
        "html_theme": "sphinxawesome_theme",
        "extensions": ["sphinxawesome_theme.highlighting"],
    },
)
def test_awesome_highlighting(app: Sphinx) -> None:
    """It loads the highlighting extension."""
    app.build()
    assert "sphinxawesome_theme.highlighting" in app.extensions


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
