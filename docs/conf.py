import datetime

year = datetime.datetime.now().year

# -- Project information -----------------------------------------------------

project = "Sphinx Awesome Theme"
author = "Kai Welke"
copyright = f"{year}, {author}"

# -- General configuration ---------------------------------------------------

extensions = ["sphinx.ext.autosectionlabel"]

exclude_patterns = ["public"]
nitpicky = True
default_role = "literal"

# -- Options for HTML output -------------------------------------------------

html_title = "Sphinx awesome theme"
html_theme = "sphinxawesome_theme"
html_theme_path = ["../"]
html_theme_options = {"nav_include_hidden": True}
html_last_updated_fmt = ""
html_add_permalinks = "#"
