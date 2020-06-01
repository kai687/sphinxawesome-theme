"""
Distribute the Sphinx theme as a python package.
See also: http://www.sphinx-doc.org/en/stable/theming.html#distribute-your-theme-as-a-python-package

:copyright: Copyright 2020, Kai Welke.
:license: MIT, see LICENSE for details
"""

from os import path
from typing import Dict, Any
from sphinx.application import Sphinx

__version__ = "1.5.0"

def setup(app: Sphinx) -> Dict[str, Any]:
    """register this theme with Sphinx"""

    app.add_html_theme("sphinxawesome_theme", path.abspath(path.dirname(__file__)))

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
