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

try:
    __version__ = version(__name__)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"


def setup(app: "Sphinx") -> Dict[str, Any]:
    """Register the theme."""
    app.add_html_theme("sphinxawesome_theme", path.abspath(path.dirname(__file__)))
    app.setup_extension("sphinxawesome.sampdirective")

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
