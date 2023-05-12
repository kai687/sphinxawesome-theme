Load the theme from a local directory
-------------------------------------

If you want to load the |product| from a local directory
without installing a Python package,
follow these steps:

#. Install the ``beautifulsoup`` package.

   .. code-block:: bash

      pip install bs4

   If you load the theme from a local directly,
   you need to manage the theme's dependencies.

#. :ref:`sec:fork-and-clone`.
#. Create a new directory for themes in your Sphinx project—for example, :file:`_themes/`:

   .. code-block:: bash
      :emphasize-lines: 4

      ./
      ├── conf.py
      ├── index.rst
      ├── _themes/
      └── ...

#. Copy the directory :file:`sphinxawesome-theme/src/sphinxawesome_theme/` into the :file:`_themes/` directory:

   .. code-block:: bash

      cp -r sphinxawesome-theme/src/sphinxawesome_theme _themes/

#. Update your Sphinx configuration:

   .. code-block:: python
      :caption: |conf|

      import os
      import sys

      sys.path.insert(0, os.path.abspath("_themes"))

      html_theme = "sphinxawesome_theme"
      extensions = ["sphinxawesome_theme"]
      html_theme_path = ["_themes"]
      exclude_patterns = ["_themes"]

   This configuration makes the local :file:`_themes` directory available to Sphinx,
   adds the |product| as HTML theme and extension,
   and excludes the directory from being searched for documentation files.

   .. note::

      If you load the |product| via the ``html_theme_path`` option,
      you must add it as extension *and* theme.
      That's because the |product| depends on a setup function that only runs when you import the theme as Python code.

   .. seealso::

      :confval:`sphinx:exclude_patterns`
      :confval:`sphinx:html_theme_path`
      :confval:`sphinx:html_theme`
      :confval:`sphinx:extensions`
