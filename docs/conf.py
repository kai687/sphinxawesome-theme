import datetime
import sys
from pathlib import Path

this_dir = Path(__file__).parent
top_dir = (this_dir / "..").resolve()

sys.path.append(str(top_dir))

year = datetime.datetime.now().year

# -- Project information -----------------------------------------------------

project = "Sphinx Awesome Theme"
author = "Kai Welke"
copyright = f"{year}, {author}."

# -- General configuration ---------------------------------------------------

extensions = ["sphinx.ext.autosectionlabel", "samp_directive"]

exclude_patterns = ["public"]
nitpicky = True
default_role = "literal"

# -- Options for HTML output -------------------------------------------------

html_title = "Sphinx awesome theme"
html_theme = "sphinxawesome_theme"
html_theme_path = ["../"]
html_last_updated_fmt = ""
html_add_permalinks = "#"
