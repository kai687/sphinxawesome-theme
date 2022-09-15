"""Unit tests for the sphinxawesome_theme python extensions."""

import os

import pytest
from sphinx.application import Sphinx

import sphinxawesome_theme


def test_returns_version() -> None:
    """It has the correct version."""
    assert sphinxawesome_theme.__version__ == "3.3.4"


@pytest.mark.sphinx("dummy")
def test_can_access_and_compile_test(app: Sphinx) -> None:
    """It compiles the basic test files."""
    if app.builder is not None:
        app.builder.build_all()
    assert os.path.exists(app.outdir)
    assert not os.listdir(app.outdir)
