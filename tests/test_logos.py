"""Test the handling of logos."""

from io import StringIO
from pathlib import Path

import pytest
from sphinx.application import Sphinx

from .util import parse_html


@pytest.mark.sphinx(
    "html",
    testroot="logos",
    confoverrides={
        "html_theme": "sphinxawesome_theme",
        "extensions": "sphinxawesome_theme",
        "html_logo": "assets/logo.svg",
        "html_theme_options": {"logo_light": "assets/logo.svg"},
    },
)
def test_includes_only_one_html_logo(app: Sphinx, warning: StringIO) -> None:
    """It includes a single logo if both `logo_light` and `html_logo` are defined."""
    app.build()
    tree = parse_html(Path(app.outdir) / "index.html")
    logos = tree.select("header img", attrs={"alt": "Logo"})
    assert len(logos) == 1

    sidebar = tree.select("#left-sidebar img", attrs={"alt": "Logo"})
    assert len(sidebar) == 1

    warnings = warning.getvalue()
    assert (
        "Conflicting theme options: use either `html_logo` or `logo_light` and `logo_dark`."
        in warnings
    )
    assert "You must use `logo_light` and `logo_dark` together." in warnings


@pytest.mark.sphinx(
    "html",
    testroot="logos",
    confoverrides={
        "html_theme": "sphinxawesome_theme",
        "extensions": "sphinxawesome_theme",
        "html_theme_options": {
            "logo_light": "assets/light_no_exist.svg",
            "logo_dark": "assets/dark_no_exist.svg",
        },
    },
)
def test_raises_warnings_for_non_existing(app: Sphinx, warning: StringIO) -> None:
    """It raises warnings, if light and dark logos do not exist."""
    app.build()
    warnings = warning.getvalue()
    assert "Path to logo assets/dark_no_exist.svg does not exist." in warnings
    assert "Path to logo assets/light_no_exist.svg does not exist." in warnings


@pytest.mark.sphinx(
    "html",
    testroot="logos",
    confoverrides={
        "html_theme": "sphinxawesome_theme",
        "extensions": "sphinxawesome_theme",
        "html_theme_options": {
            "logo_light": "assets/light.svg",
            "logo_dark": "assets/dark.svg",
        },
    },
)
def test_copies_logos(app: Sphinx, warning: StringIO) -> None:
    """It copies the light and dark logos without warnings."""
    app.build()
    warnings = warning.getvalue()
    assert len(warnings) == 0
    light = Path(app.outdir) / "_static" / "light.svg"
    assert light.exists()
    dark = Path(app.outdir) / "_static" / "dark.svg"
    assert dark.exists()

    tree = parse_html(Path(app.outdir) / "index.html")
    logos = tree.select("header img", attrs={"alt": "Logo"})
    assert len(logos) == 2

    sidebar = tree.select("#left-sidebar img", attrs={"alt": "Logo"})
    assert len(sidebar) == 2
