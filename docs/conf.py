"""Sphinx configuration file."""

import sys
from pathlib import Path
from typing import List, Tuple

from docutils import nodes
from docutils.nodes import Node, system_message
from sphinx.application import Sphinx
from sphinx.roles import EmphasizedLiteral
from sphinx.util.docfields import Field

# Add path to local extension
this_dir = Path(__file__).parent
ext_dir = (this_dir / ".." / "src").resolve()
sys.path.append(str(ext_dir.absolute()))

# -- Project information -----------------------------------------------------

project = "Sphinx Awesome Theme"
author = "Kai Welke"
copyright = f"{author}."

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.autodoc",
    "sphinxawesome_theme",
    "myst_parser",
]

myst_enable_extensions = ["colon_fence", "deflist"]

exclude_patterns = ["public"]
nitpicky = True
nitpick_ignore = [
    ("py:class", "sphinx.application.Sphinx"),
    ("py:class", "docutils.nodes.Element"),
]
default_role = "literal"
autodoc_default_flags = ["members"]
autodoc_warningiserror = False

# I keep forgetting how to spell this term
rst_prolog = ".. |rst| replace:: reStructuredText"

# -- Options for HTML output -------------------------------------------------

html_title = "Sphinx awesome theme"
html_theme = "sphinxawesome_theme"
html_theme_path = ["../src"]
html_last_updated_fmt = ""
html_use_index = False  # Don't create index
html_domain_indices = False  # Don't need module indices
html_copy_source = False

# extra option from the sphinxawesome_theme
html_collapsible_definitions = True

html_theme_options = {"show_scrolltop": True}

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
    app.add_object_type(
        "confval",
        "confval",
        objname="configuration parameter",
        doc_field_types=[
            Field(
                "default",
                label="default",
                has_arg=True,
                names=("default",),
                bodyrolename="class",
            )
        ],
    )
