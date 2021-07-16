"""Unit tests for the sphinxawesome_theme python extensions."""

import os

import pytest
from sphinx.application import Sphinx

import sphinxawesome_theme


def test_returns_version() -> None:
    """It has the correct version."""
    assert sphinxawesome_theme.__version__ == "2.0.0"


@pytest.mark.sphinx("dummy")
def test_can_access_and_compile_test(app: Sphinx) -> None:
    """It compiles the basic test files."""
    if app.builder is not None:
        app.builder.build_all()
    assert os.path.exists(app.outdir)
    assert not os.listdir(app.outdir)


def test_loads_extensions(app: Sphinx) -> None:
    """It loads all internal extensions."""
    _ = sphinxawesome_theme.setup(app)
    assert "sphinxawesome.sampdirective" in app.extensions
    assert "sphinxawesome_theme.html_translator" in app.extensions
    assert "sphinxawesome_theme.jinja_filters" in app.extensions
    assert "sphinxawesome_theme.postprocess" in app.extensions
    assert "sphinxawesome_theme.admonition_ids" in app.extensions
    assert "sphinxawesome_theme.highlighting" in app.extensions
