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
            ".highlight { background: #0d1117; color: #E6EDF3 }",
            "span.linenos { color: #6e7681; background-color: #0d1117; padding-left: 5px; }",
            "td.linenos .normal { color: #6e7681; background-color: #0d1117; }",
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
            ".highlight .hll { background-color: #6e7681 }",
            "span.linenos.special { color: #000000; background-color: #ffffc0; }",
            ".highlight .gd { background-color: #ffdddd }",
        ]
    )

    assert _drop_backgrounds(css) == css


@pytest.mark.sphinx(
    "html",
    testroot="root",
    confoverrides={
        # Sphinx 7.1 processes overrides before loading the theme entry point.
        "extensions": ["sphinxawesome_theme"],
        "html_theme": "sphinxawesome_theme",
        "pygments_style": "default",
        "pygments_style_dark": "one-dark",
    },
    freshenv=True,
)
def test_dark_styles_follow_theme_toggle(app: Sphinx) -> None:
    """It scopes dark styles to the `dark` class and doesn't link a separate file."""
    app.build()

    css = (Path(app.outdir) / "_static" / "pygments.css").read_text(encoding="utf-8")
    light_scope = ":where(:root:not(.dark))"
    dark_scope = ":where(:root.dark)"
    rules = css.splitlines()
    assert all(rule.startswith((f"{light_scope} ", f"{dark_scope} ")) for rule in rules)
    light_keyword = next(rule for rule in rules if rule.startswith(f"{light_scope} .highlight .k {{"))
    dark_keyword = next(rule for rule in rules if rule.startswith(f"{dark_scope} .highlight .k {{"))
    assert "font-weight: bold" in light_keyword
    assert "font-weight" not in dark_keyword
    assert "prefers-color-scheme" not in css
    # Explicit styles keep their own code block backgrounds.
    assert f"{light_scope} .highlight {{ background" in css
    assert f"{dark_scope} .highlight {{ background" in css

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
    """It lets the theme style the background of the default `bw` scheme."""
    app.build()

    css = (Path(app.outdir) / "_static" / "pygments.css").read_text(encoding="utf-8")
    assert ".dark" not in css
    assert ".highlight { background" not in css


@pytest.mark.sphinx(
    "html",
    testroot="root",
    confoverrides={
        "extensions": ["sphinxawesome_theme"],
        "html_theme": "child",
        "html_theme_path": ["_themes"],
    },
    freshenv=True,
)
def test_inherited_theme_style_keeps_its_palette(app: Sphinx) -> None:
    """It keeps the background selected by an inherited theme."""
    app.build()

    css = (Path(app.outdir) / "_static" / "pygments.css").read_text(encoding="utf-8")
    assert ".highlight { background: #272822; color: #F8F8F2 }" in css


@pytest.mark.sphinx(
    "html",
    testroot="root",
    confoverrides={"html_theme": "sphinxawesome_theme", "pygments_style": "xcode"},
    freshenv=True,
)
def test_explicit_single_style_keeps_its_palette(app: Sphinx) -> None:
    """It preserves contrast even when the page switches to dark mode."""
    app.build()

    css = (Path(app.outdir) / "_static" / "pygments.css").read_text(encoding="utf-8")
    assert ".dark" not in css
    assert ".highlight { background: #ffffff; }" in css
    assert ".highlight { color: #000; }" in css


def test_pygments_rules_are_single_line() -> None:
    """It guards the per-line scoping in `create_pygments_style_file`."""
    from sphinxawesome_theme.highlighting import AwesomePygmentsBridge

    for style in ("default", "one-dark", "github-dark"):
        css = AwesomePygmentsBridge("html", style).get_stylesheet()
        for line in css.splitlines():
            assert line.strip()
            assert "{" in line
            assert "}" in line
