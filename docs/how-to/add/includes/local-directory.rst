Load the theme from a local directory
-------------------------------------

If you want to load the |product| from a local directory
without installing a Python package,
follow these steps:

.. note::

   If you load the theme from a local directory,
   you need to manage the theme's dependencies.
   For example, you need to install the ``beautifulsoup`` package.
   To install it, run: ``pip install bs4``.

#. :ref:`sec:fork-and-clone`.
#. Create a new directory for themes in your Sphinx project—for example, :file:`_themes/`:

   .. code-block:: terminal
      :emphasize-lines: 4

      ./
      ├── conf.py
      ├── index.rst
      ├── _themes/
      └── ...

#. Copy the directory :file:`sphinxawesome-theme/src/sphinxawesome_theme/` into the :file:`_themes/` directory:

   .. code-block:: terminal

      cp -r sphinxawesome-theme/src/sphinxawesome_theme _themes/

#. Update your Sphinx configuration:

   .. code-block:: python
      :caption: File: conf.py

      html_theme = "sphinxawesome_theme"
      html_theme_path = ["_themes"]
      exclude_patterns = ["_themes"]
      extensions = ["sphinxawesome_theme"]

   This configuration makes the local :file:`_themes` directory available to Sphinx,
   adds the |product| as HTML theme and extension,
   and excludes the directory from being searched for documentation files.

   .. seealso::

      :confval:`sphinx:exclude_patterns`
      :confval:`sphinx:html_theme_path`
      :confval:`sphinx:html_theme`
      :confval:`sphinx:extensions`
