"""Test if a simple test compiles."""

import os
from pathlib import Path

import pytest
from sphinx.application import Sphinx

import sphinxawesome_theme


def test_returns_version() -> None:
    """It has the correct version."""
    assert sphinxawesome_theme.__version__ == "6.0.0b2"


@pytest.mark.sphinx("dummy")
def test_can_access_and_compile_test(app: Sphinx) -> None:
    """It compiles the basic test files."""
    app.build()
    assert os.path.exists(app.outdir)
    assert not os.listdir(app.outdir)


@pytest.mark.sphinx("html")
def test_compiles_html(app: Sphinx) -> None:
    """It compiles HTML with default settings."""
    app.build()
    assert os.path.exists(Path(app.outdir) / "index.html")
