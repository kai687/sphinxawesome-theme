"""The Sphinx awesome theme as a Python package.

:copyright: Copyright 2020, Kai Welke.
:license: MIT, see LICENSE for details
"""

try:
    from importlib.metadata import version, PackageNotFoundError  # type: ignore
except ImportError:  # pragma: no cover
    from importlib_metadata import version, PackageNotFoundError  # type: ignore

from os import path
from typing import Any, Dict

from sphinx.application import Sphinx

from .admonitions_ids import AdmonitionId
from .html_translator import BetterHTMLTranslator
from .jinja_filter import setup_jinja_filter
from .postprocess import post_process_html

try:
    __version__ = version(__name__)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"


def setup(app: "Sphinx") -> Dict[str, Any]:
    """Register the theme."""
    app.add_html_theme("sphinxawesome_theme", path.abspath(path.dirname(__file__)))
    app.setup_extension("sphinxawesome.sampdirective")
    app.set_translator("html", BetterHTMLTranslator)
    app.set_translator("dirhtml", BetterHTMLTranslator)
    app.add_post_transform(AdmonitionId)
    app.connect("html-page-context", setup_jinja_filter)
    app.connect("build-finished", post_process_html)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
