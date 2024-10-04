"""Test the presence or absense of the scroll to top button."""

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
def test_no_scroll_top_button(app: Sphinx) -> None:
    """It doesn't have a scroll to top button by default."""
    app.build()
    assert os.path.exists(Path(app.outdir) / "index.html")
    tree = parse_html(Path(app.outdir) / "index.html")
    button = tree.select("button#scrolltop")
    assert len(button) == 0


@pytest.mark.sphinx(
    "html",
    confoverrides={
        "html_theme": "sphinxawesome_theme",
        "html_theme_options": {"show_scrolltop": True},
    },
)
def test_scroll_top_button(app: Sphinx) -> None:
    """It shows a scroll to top button."""
    app.build()
    assert os.path.exists(Path(app.outdir) / "index.html")
    tree = parse_html(Path(app.outdir) / "index.html")
    button = tree.select("button#scrolltop")
    assert len(button) == 1
