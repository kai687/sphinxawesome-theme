"""Sphinx configuration file."""

import datetime
from pathlib import Path
import sys
from typing import List, Tuple

from docutils import nodes
from docutils.nodes import Node, system_message
from sphinx.application import Sphinx
from sphinx.roles import EmphasizedLiteral

year = datetime.datetime.now().year

# Add path to local extension
this_dir = Path(__file__).parent
ext_dir = (this_dir / ".." / "src").resolve()
sys.path.append(str(ext_dir.absolute()))

# -- Project information -----------------------------------------------------

project = "Sphinx Awesome Theme"
author = "Kai Welke"
copyright = f"{year}, {author}."

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.autodoc",
    "sphinxawesome_theme",
]

exclude_patterns = ["public"]
nitpicky = True
default_role = "literal"

# -- Options for HTML output -------------------------------------------------

html_title = "Sphinx awesome theme"
html_theme = "sphinxawesome_theme"
html_theme_path = ["../src"]
html_last_updated_fmt = ""
html_add_permalinks = "#"

# -- Register a :dir: interpreted text role ----------------------------------


class DirRole(EmphasizedLiteral):
    """Modify the ``EmphasizedLiteral`` role.

    To distinguish files from directories, I'll append
    ``/`` to every directory. In case the author forgets it,
    append the trailing slash automatically.
    """

    def run(self) -> Tuple[List[Node], List[system_message]]:
        """Implement tiny bit of extra logic."""
        if not self.text.strip().endswith("/"):
            self.text += "/"

        children = self.parse(self.text)
        node = nodes.literal(
            self.rawtext, "", *children, role=self.name.lower(), classes=[self.name]
        )

        return [node], []


def setup(app: Sphinx) -> None:
    """Register the :dir: role.

    This is just a shortcut to curb the cognitive dissonance
    when saying :file:`directory/`.
    """
    app.add_role("dir", DirRole())
