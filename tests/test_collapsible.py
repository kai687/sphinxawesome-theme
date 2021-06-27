"""Tests for collapsible definition lists.

When the option ``html_collapsible_definitions``
is ``True``, some HTML classes should be added
to some definition lists but not all of them.
"""

from pathlib import Path

import pytest
from sphinx.application import Sphinx

from .util import parse_html


@pytest.mark.sphinx(
    "html",
    testroot="collapsible",
    confoverrides={"html_theme": "sphinxawesome_theme"},
    freshenv=True,
)
def test_no_permalinks(app: Sphinx) -> None:
    """It tests that there are no permalinks."""
    app.config.html_permalinks = False
    app.build()
    tree = parse_html(Path(app.outdir) / "index.html")
    dl = tree("dl")
    assert len(dl) == 2
    headerlinks = tree("a", class_="headerlink")
    assert len(headerlinks) == 0


@pytest.mark.sphinx(
    "html",
    testroot="collapsible",
    confoverrides={"html_theme": "sphinxawesome_theme"},
    freshenv=True,
)
def test_no_collapsible_definitions(app: Sphinx) -> None:
    """By default, no classes should be added."""
    app.build()
    tree = parse_html(Path(app.outdir) / "index.html")
    dl = tree("dl")
    assert len(dl) == 2

    assert str(dl[0]).replace("\n", "") == (
        '<dl class="simple"><dt>term</dt><dd><p>definition</p></dd></dl>'
    )

    assert dl[1]["class"] == ["std", "option", "code-definition"]
    dt, dd = (c for c in dl[1].children if c.strip is None)
    assert dt.name == "dt"
    assert "accordion" not in dt["class"]
    assert dd.name == "dd"
    assert "class" not in dd

    expand_more_button = dt("button", class_="expand-more")
    assert len(expand_more_button) == 0


@pytest.mark.sphinx(
    "html",
    testroot="collapsible",
    confoverrides={"html_theme": "sphinxawesome_theme"},
    freshenv=True,
)
def test_collapsible_definitions(app: Sphinx) -> None:
    """It tests the correct classes being added to the definition lists.

    It should not add the classes to normal definition lists.
    """
    # if specified in 'confoverrides', this returns a warning
    app.config.html_collapsible_definitions = True
    app.build()
    tree = parse_html(Path(app.outdir) / "index.html")
    dl = tree("dl")

    assert len(dl) == 2
    assert str(dl[0]).replace("\n", "") == (
        '<dl class="simple"><dt>term</dt><dd><p>definition</p></dd></dl>'
    )
    assert "code-definition" in dl[1]["class"]
    dt, dd = (c for c in dl[1].children if c.strip is None)
    assert dt.name == "dt"
    assert dt["class"] == ["sig", "sig-object", "std", "accordion"]
    assert dd.name == "dd"
    assert dd["class"] == ["panel"]

    expand_more_button = dt("button", class_="expand-more")
    assert len(expand_more_button) == 1
