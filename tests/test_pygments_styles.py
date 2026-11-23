"""Test the handling of Pygments styles for light and dark mode."""

from pathlib import Path

import pytest
from sphinx.application import Sphinx

from sphinxawesome_theme.builder import _drop_backgrounds

from .util import parse_html


def test_drop_backgrounds_from_code_block_and_line_numbers() -> None:
    """It removes the backgrounds that the theme owns."""
    css = "\n".join(
        [
            ".highlight { background: #ffffff; }",
            ".dark .highlight { background: #0d1117; color: #E6EDF3 }",
            "span.linenos { color: #6e7681; background-color: #0d1117; padding-left: 5px; }",
            ".dark td.linenos .normal { color: #6e7681; background-color: #0d1117; }",
        ]
    )

    result = _drop_backgrounds(css)

    assert "background" not in result
    assert "color: #E6EDF3" in result
    assert "color: #6e7681" in result
    assert "padding-left: 5px" in result


def test_drop_backgrounds_keeps_highlighted_lines() -> None:
    """It keeps the backgrounds of highlighted lines and tokens."""
    css = "\n".join(
        [
            ".dark .highlight .hll { background-color: #6e7681 }",
            "span.linenos.special { color: #000000; background-color: #ffffc0; }",
            ".highlight .gd { background-color: #ffdddd }",
        ]
    )

    assert _drop_backgrounds(css) == css


@pytest.mark.sphinx(
    "html",
    testroot="root",
    confoverrides={
        "html_theme": "sphinxawesome_theme",
        "pygments_style": "xcode",
        "pygments_style_dark": "github-dark",
    },
    freshenv=True,
)
def test_dark_styles_follow_theme_toggle(app: Sphinx) -> None:
    """It scopes dark styles to the `dark` class and doesn't link a separate file."""
    app.build()

    css = (Path(app.outdir) / "_static" / "pygments.css").read_text(encoding="utf-8")
    assert ".dark .highlight .k" in css
    assert "prefers-color-scheme" not in css
    # The theme owns the background of code blocks
    assert ".highlight { background" not in css
    assert ".dark .highlight { background" not in css

    assert not (Path(app.outdir) / "_static" / "pygments_dark.css").exists()
    tree = parse_html(Path(app.outdir) / "index.html")
    hrefs = [str(link["href"]) for link in tree.select('link[rel="stylesheet"]')]
    assert not any("pygments_dark" in href for href in hrefs)


@pytest.mark.sphinx(
    "html",
    testroot="root",
    confoverrides={"html_theme": "sphinxawesome_theme"},
    freshenv=True,
)
def test_no_dark_styles_by_default(app: Sphinx) -> None:
    """It doesn't add dark styles unless you configure `pygments_style_dark`."""
    app.build()

    css = (Path(app.outdir) / "_static" / "pygments.css").read_text(encoding="utf-8")
    assert ".dark" not in css
