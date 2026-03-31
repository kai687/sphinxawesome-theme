"""Test the construction of canonical links."""

from pathlib import Path
from typing import cast

import pytest
from sphinx.application import Sphinx

from .util import parse_html


@pytest.mark.sphinx(
    "html",
    testroot="external",
    freshenv=True,
    confoverrides={
        "html_theme": "sphinxawesome_theme",
    },
)
def test_no_external_link_icons(app: Sphinx) -> None:
    """It doesn't add canonical links by default."""
    app.build()
    tree = parse_html(Path(app.outdir) / "index.html")
    links = tree.select(".reference")
    assert len(links) == 3

    icons = tree.select(".reference svg")
    assert len(icons) == 0


@pytest.mark.sphinx(
    "html",
    testroot="external",
    freshenv=True,
    confoverrides={
        "html_theme": "sphinxawesome_theme",
        "html_theme_options": {
            "awesome_external_links": True,
        },
    },
)
def test_external_link_icons(app: Sphinx) -> None:
    """It adds an external link icon to external references."""
    app.build()
    theme_options = cast(dict[str, object], getattr(app.builder, "theme_options", {}))
    assert "awesome_external_links" in theme_options
    assert theme_options["awesome_external_links"] is True

    tree = parse_html(Path(app.outdir) / "index.html")

    links = tree.select(".reference")
    assert len(links) == 3
    icons = tree.select(".reference svg")
    assert len(icons) == 1
