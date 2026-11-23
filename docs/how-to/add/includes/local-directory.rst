Load the theme from a local directory
-------------------------------------

To load the |product| from a local directory
without a Python package, do these steps:

#. Install the ``beautifulsoup`` package.

   .. code-block:: bash

      pip install bs4

   If you load the theme from a local directory,
   you must manage the dependencies of the theme.

#. :ref:`sec:fork-and-clone`.
#. Make a new directory for themes in your Sphinx project, for example :file:`_themes/`:

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

   This configuration does these things:

   - It makes the local :file:`_themes` directory available to Sphinx.
   - It adds the |product| as an HTML theme and as an extension.
   - It stops Sphinx from searching the directory for documentation files.

   .. note::

      If you load the |product| with the ``html_theme_path`` option,
      you must add it as an extension *and* as a theme.
      The |product| needs a setup function.
      This function runs only when you import the theme as Python code.

   .. seealso::

      :confval:`sphinx:exclude_patterns`
      :confval:`sphinx:html_theme_path`
      :confval:`sphinx:html_theme`
      :confval:`sphinx:extensions`
