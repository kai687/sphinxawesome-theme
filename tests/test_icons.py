"""Unit tests for the icons module."""

from sphinxawesome_theme import icons


def test_icons_to_html() -> None:
    """It returns the correct HTML representation of an icon."""
    i = icons.ICONS["headerlink"]
    html = icons.html(i)
    assert len(html) == 1
    svg = html("svg")
    assert len(svg) == 1
    path = html("path")
    assert len(path) == 1
    assert path[0].parent.name == "svg"
