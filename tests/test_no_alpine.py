"""Guard against Alpine.js directives creeping back in, and check the rendered nav state."""

import re
from pathlib import Path

import pytest
from bs4 import Tag
from sphinx.application import Sphinx

from .util import parse_html

STATIC = Path(__file__).parent.parent / "src" / "sphinxawesome_theme" / "static"
OPTIONS = {
    "main_nav_links": {"Docs": "/index"},
    "show_scrolltop": True,
    "awesome_headerlinks": True,
    "awesome_external_links": True,
}


def alpine_attributes(path: Path) -> list[str]:
    """Names of attributes that look like Alpine directives."""
    tree = parse_html(path)
    found = []
    for tag in tree.find_all(True):
        found.extend(f"{tag.name}[{name}]" for name in tag.attrs if re.match(r"^(x-|@|:)", name))
    return found


@pytest.mark.sphinx(
    "html",
    testroot="nav",
    srcdir="no-alpine",
    confoverrides={"html_theme": "sphinxawesome_theme", "html_theme_options": OPTIONS},
)
def test_no_alpine_attributes(app: Sphinx) -> None:
    """No generated page has `x-*`, `@*` or `:*` attributes."""
    app.build()
    pages = list(Path(app.outdir).glob("*.html"))
    assert pages
    for page in pages:
        assert not alpine_attributes(page), page.name


def test_bundle_has_no_alpine() -> None:
    """The shipped JavaScript doesn't contain Alpine."""
    bundle = (STATIC / "theme.js").read_text()
    assert "Alpine" not in bundle
    assert "x-cloak" not in (STATIC / "theme.css").read_text()


@pytest.mark.sphinx(
    "html",
    testroot="nav",
    srcdir="no-alpine",
    confoverrides={"html_theme": "sphinxawesome_theme", "html_theme_options": OPTIONS},
)
def test_nav_initial_state_is_rendered(app: Sphinx) -> None:
    """Collapsed branches are hidden in the HTML, the current branch is expanded."""
    app.build()

    other = parse_html(Path(app.outdir) / "index.html")
    link = other.select_one('#left-sidebar a[href="parent.html"]')
    assert link is not None
    assert "expandable" in link["class"]
    assert "expanded" not in link["class"]
    children = link.find_next_sibling("ul")
    assert isinstance(children, Tag)
    assert children.has_attr("hidden")
    assert link.select_one("button[type=button]") is not None

    current = parse_html(Path(app.outdir) / "parent.html")
    link = current.select_one("#left-sidebar a.expandable")
    assert link is not None
    assert "expanded" in link["class"]
    children = link.find_next_sibling("ul")
    assert isinstance(children, Tag)
    assert not children.has_attr("hidden")


@pytest.mark.sphinx(
    "html",
    testroot="nav",
    srcdir="no-alpine",
    confoverrides={"html_theme": "sphinxawesome_theme", "html_theme_options": OPTIONS},
)
def test_js_hooks_present(app: Sphinx) -> None:
    """The templates carry the hooks that `ui.js` binds to."""
    app.build()
    tree = parse_html(Path(app.outdir) / "long.html")
    assert tree.select_one("button[data-theme-toggle][aria-pressed]")
    assert tree.select_one("button[data-sidebar-open]")
    assert tree.select_one("#left-sidebar button[data-sidebar-close]")
    assert tree.select_one("#sidebar-overlay[hidden]")
    assert tree.select_one("#search-input")
    scrolltop = tree.select_one("#scrolltop")
    assert scrolltop is not None
    assert "invisible" in scrolltop["class"]
    assert tree.select("a.headerlink[data-copy-link][data-tooltip]")
    assert tree.select("a.headerlink[data-scrollspy]")
    assert tree.select("#right-sidebar a[href^='#']")
