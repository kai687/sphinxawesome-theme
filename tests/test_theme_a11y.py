"""Test accessibility markup where the markup itself is the contract."""

from pathlib import Path

import pytest
from sphinx.application import Sphinx

from .util import parse_html

NAV_LINKS = {
    "Docs": "/index",
    "About": "/about",
    "A": "/a",
    "External": "https://example.org",
}
OPTIONS = {
    "html_theme": "sphinxawesome_theme",
    "html_theme_options": {"main_nav_links": NAV_LINKS},
}


@pytest.mark.sphinx("html", testroot="nav", confoverrides=OPTIONS)
def test_theme_toggle_has_accessible_name(app: Sphinx) -> None:
    """The toggle button has an accessible name and exposes its pressed state."""
    app.build()
    tree = parse_html(Path(app.outdir) / "index.html")
    button = tree.select_one('button[aria-label="Toggle color scheme"]')
    assert button is not None
    assert button.get(":aria-pressed") == "darkMode.toString()"


@pytest.mark.sphinx("html", testroot="nav", confoverrides=OPTIONS)
@pytest.mark.parametrize(
    ("page", "active"),
    [("index", "Docs"), ("about", "About"), ("a", "A")],
)
def test_main_nav_marks_only_current_page(app: Sphinx, page: str, active: str) -> None:
    """Exactly one link is active: the current page. External links never are.

    The short page name `a` is a substring of `about`, which would trip a
    substring match.
    """
    app.build()
    tree = parse_html(Path(app.outdir) / f"{page}.html")
    links = {a.get_text(strip=True): a for a in tree.select("header nav a")}
    is_active = {name: "text-foreground/60" not in links[name].get("class", []) for name in NAV_LINKS}
    assert {name for name, on in is_active.items() if on} == {active}
