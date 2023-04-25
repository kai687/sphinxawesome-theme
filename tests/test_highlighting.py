"""Test the loading of the awesome extensions."""

import os
from pathlib import Path

import pytest
from sphinx.application import Sphinx


# from .util import parse_html


@pytest.mark.sphinx(
    "html",
    confoverrides={
        "extensions": ["sphinxawesome_theme"],
        "html_awesome_highlighting": False,
    },
)
def test_no_awesome_highlighting(app: Sphinx) -> None:
    """It doesn't load the awesome highlighting extension."""
    app.build()
    assert os.path.exists(Path(app.outdir) / "index.html")
    assert "sphinxawesome_theme.highlighting" not in app.extensions
    assert app.config.html_awesome_highlighting is False
