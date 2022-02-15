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
from sphinx.config import Config
from sphinxcontrib.serializinghtml import JSONHTMLBuilder

from . import jsonimpl

try:
    # obtain version from `pyproject.toml` via `importlib.metadata.version()`
    __version__ = version(__name__)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"


def conditional_setup(app: Sphinx, config: Config) -> None:
    """Set up extensions if configuration is ready."""
    if config.html_awesome_docsearch:
        app.setup_extension("sphinxawesome_theme.docsearch")

    if config.html_awesome_html_translator:
        app.setup_extension("sphinxawesome_theme.html_translator")

    if config.html_awesome_postprocessing:
        app.setup_extension("sphinxawesome_theme.postprocess")


def setup(app: "Sphinx") -> Dict[str, Any]:
    """Register the theme and its extensions wih Sphinx."""
    app.add_html_theme(
        name="sphinxawesome_theme", theme_path=path.abspath(path.dirname(__file__))
    )
    app.add_config_value(
        name="html_awesome_postprocessing", default=True, rebuild="html", types=(bool)
    )
    app.add_config_value(
        name="html_awesome_html_translator", default=True, rebuild="html", types=(bool)
    )
    app.add_config_value(
        name="html_awesome_docsearch", default=False, rebuild="html", types=(bool)
    )
    app.add_config_value(
        name="docsearch_config", default={}, rebuild="html", types=(dict)
    )
    app.add_config_value(
        name="html_collapsible_definitions", default=False, rebuild="html", types=(str)
    )
    app.add_config_value(
        name="html_awesome_headerlinks", default=True, rebuild="html", types=(str)
    )
    app.add_config_value(
        name="html_awesome_code_headers", default=True, rebuild="html", types=(str)
    )

    app.setup_extension("sphinxawesome_theme.highlighting")
    app.setup_extension("sphinxawesome_theme.jinja_functions")

    app.connect("config-inited", conditional_setup)

    JSONHTMLBuilder.out_suffix = ".json"
    JSONHTMLBuilder.implementation = jsonimpl
    JSONHTMLBuilder.indexer_format = jsonimpl

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
