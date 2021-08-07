"""The Sphinx awesome theme as a Python package.

:copyright: Copyright Kai Welke.
:license: MIT, see LICENSE_ for details

.. _LICENSE: https://github.com/kai687/sphinxawesome-theme/blob/master/LICENSE
"""

try:
    from importlib.metadata import PackageNotFoundError, version  # type: ignore
except ImportError:  # pragma: no cover
    # ignore mypy error about incompatible imports
    from importlib_metadata import version, PackageNotFoundError  # type: ignore

from os import path
from typing import Any, Dict

from sphinx.application import Sphinx

try:
    # obtain version from `pyproject.toml` via `importlib.metadata.version()`
    __version__ = version(__name__)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"


def setup(app: "Sphinx") -> Dict[str, Any]:
    """Register the theme and its extensions wih Sphinx."""
    app.add_html_theme("sphinxawesome_theme", path.abspath(path.dirname(__file__)))
    app.add_config_value("html_awesome_postprocessing", True, "html")
    app.add_config_value("html_awesome_html_translator", True, "html")
    app.setup_extension("sphinxawesome_theme.highlighting")
    app.setup_extension("sphinxawesome_theme.jinja_functions")

    if app.config.html_awesome_html_translator:
        app.setup_extension("sphinxawesome_theme.html_translator")

    if app.config.html_awesome_postprocessing:
        app.setup_extension("sphinxawesome_theme.postprocess")

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
