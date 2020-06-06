"""
The Sphinx awesome theme as a Python package.

:copyright: Copyright 2020, Kai Welke.
:license: MIT, see LICENSE for details
"""

from os import path
from typing import Any, Dict

from sphinx.application import Sphinx

__version__ = "1.5.0"


def setup(app: "Sphinx") -> Dict[str, Any]:
    """Register the theme."""

    app.add_html_theme("sphinxawesome_theme", path.abspath(path.dirname(__file__)))

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
