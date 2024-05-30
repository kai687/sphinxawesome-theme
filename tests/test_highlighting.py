"""Test the bundled highlighting extension."""

from io import StringIO
from pathlib import Path

import pytest
from sphinx.application import Sphinx

from .util import parse_html


@pytest.mark.sphinx(
    "html",
    testroot="highlighting",
    confoverrides={"html_theme": "sphinxawesome_theme"},
    freshenv=True,
)
def test_handles_highlighting(app: Sphinx, warning: StringIO) -> None:
    """It handles the extra highlighting options of the code block directive."""
    app.build()

    assert len(warning.getvalue()) == 0

    tree = parse_html(Path(app.outdir) / "index.html")
    code_block = tree("pre")
    assert len(code_block) == 2

    inserted = code_block[0]("ins")
    assert len(inserted) == 1

    inserted = code_block[1]("ins")
    assert len(inserted) == 1

    deleted = code_block[0]("del")
    assert len(deleted) == 1

    deleted = code_block[1]("del")
    assert len(deleted) == 1

    placeholder = code_block[0]("span", class_="ge")
    assert len(placeholder) == 1

    placeholder = code_block[1]("span", class_="ge")
    assert len(placeholder) == 1
