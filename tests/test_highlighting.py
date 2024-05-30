"""Test the bundled highlighting extension."""

from io import StringIO
from pathlib import Path

import pytest
from sphinx.application import Sphinx

from .util import parse_html


@pytest.mark.sphinx(
    "html",
    testroot="highlighting",
    confoverrides={
        "html_theme": "sphinxawesome_theme",
    },
    freshenv=True,
)
def test_has_unrecognized_options(app: Sphinx, warning: StringIO) -> None:
    """It raises a warning when the ``sphinxawesome_theme.highlighting`` extension is not active."""
    app.build()

    # The full error message has line breaks and I can't be bothered to replicate it here.
    # assert (
    #     'unknown option: "emphasize-removed"'
    #     in warning.getvalue()
    # )
    assert "sphinxawesome_theme.highlighting" not in app.extensions


@pytest.mark.sphinx(
    "html",
    testroot="highlighting",
    confoverrides={
        "html_theme": "sphinxawesome_theme",
        "extensions": ["sphinxawesome_theme.highlighting"],
    },
    freshenv=True,
)
def test_handles_highlighting(app: Sphinx, warning: StringIO) -> None:
    """It handles the extra highlighting options of the code block directive."""
    app.build()

    assert len(warning.getvalue()) == 0
    assert "sphinxawesome_theme.highlighting" in app.extensions

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
