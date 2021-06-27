"""Tests for copyright info.

When the `copyright` setting is empty,
no copyright info should be printed.

Issue #285.
"""
import re
from pathlib import Path

import pytest
from sphinx.application import Sphinx

from .util import parse_html


@pytest.mark.sphinx(
    "html",
    testroot="copyright",
)
def test_empty_copyright_info(app: Sphinx) -> None:
    """It does not contain any Copyright info in the footer."""
    app.build()
    tree = parse_html(Path(app.outdir) / "index.html")
    footer = tree("footer")
    assert len(footer) == 1

    # search for text in the children of footer
    for child in footer:
        matches = child.find_all(text=re.compile("©"))
        assert len(matches) == 0


@pytest.mark.sphinx(
    "html",
    testroot="copyright",
    confoverrides={"show_copyright": "False"},
)
def test_dont_show_copyright(app: Sphinx) -> None:
    """It does notcontain any Copyright info in the footer."""
    app.build()
    tree = parse_html(Path(app.outdir) / "index.html")
    footer = tree("footer")
    assert len(footer) == 1

    # search for text in the children of footer
    for child in footer:
        matches = child.find_all(text=re.compile("©"))
        assert len(matches) == 0


@pytest.mark.sphinx(
    "html",
    testroot="copyright",
    confoverrides={"copyright": "Test"},
)
def test_show_copyright(app: Sphinx) -> None:
    """It contains any Copyright info in the footer."""
    app.build()
    tree = parse_html(Path(app.outdir) / "index.html")
    footer = tree("footer")
    assert len(footer) == 1

    # search for text in the children of footer
    for child in footer:
        matches = child.find_all(text=re.compile("©"))
        assert len(matches) == 1
