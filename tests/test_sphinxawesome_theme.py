"""Unit tests for the sphinxawesome_theme python extensions."""

import os
from pathlib import Path

import pytest
from sphinx.application import Sphinx

from sphinxawesome_theme import __version__


def test_returns_version() -> None:
    """It has the correct version."""
    assert __version__ == "1.10.5"


@pytest.mark.sphinx("dummy")
def test_can_access_and_compile_test(rootdir: Path, app: Sphinx) -> None:
    """It compiles the basic test files."""
    app.builder.build_all()
    assert app.outdir.exists()
    assert not os.listdir(app.outdir)


@pytest.mark.sphinx("dummy", confoverrides={"extensions": ["sphinxawesome_theme"]})
def test_dummy_compiles_with_extension(app: Sphinx) -> None:
    """It compiles with enabling the extension."""
    app.builder.build_all()

    assert app.outdir.exists()
    assert not os.listdir(app.outdir)
