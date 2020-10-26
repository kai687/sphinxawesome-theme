"""Unit tests for the sphinxawesome_theme python extensions."""

import os

from bs4 import BeautifulSoup
import pytest
from sphinx.application import Sphinx

from sphinxawesome_theme import __version__


def html_parse(filename: str) -> BeautifulSoup:
    """Parse the HTML5 output."""
    with open(filename) as file_handle:
        tree = BeautifulSoup(file_handle, "html.parser")
    return tree


def test_returns_version() -> None:
    """It has the correct version."""
    assert __version__ == "1.14.0"


@pytest.mark.sphinx("dummy")
def test_can_access_and_compile_test(app: Sphinx) -> None:
    """It compiles the basic test files."""
    app.builder.build_all()
    assert app.outdir.exists()
    assert not os.listdir(app.outdir)
