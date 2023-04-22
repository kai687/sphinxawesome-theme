.. meta::
   :description: Learn how to add the Awesome Theme to your Sphinx documentation.

Add the theme
=============

.. rst-class:: lead

   Learn how to add the |product| to your Sphinx documentation.

.. contents:: On this page
   :local:
   :backlinks: none

.. _sec:add-to-sphinx:

Add the theme to your Sphinx configuration
------------------------------------------

To use the |product| in your documentation:

#. :ref:`sec:install-python-package`.
#. Add the |product| as an HTML theme and extension:

   .. code-block:: python
      :caption: File: conf.py

      html_theme = "sphinxawesome_theme"
      extensions = ["sphinxawesome_theme"]

   .. seealso::

      :ref:`sec:extension-options`
      :confval:`sphinx:html_theme`
      :confval:`sphinx:extensions`

Load the theme from a local directory
-------------------------------------

If you want to build your own theme,
you can load the |product| from a local directory.

.. note::

   When loading the theme from a local directory,
   you need to manage the dependencies yourself.
   This theme needs the ``beautifulsoup`` package.
   You can install it with ``pip``:

   .. code-block:: terminal

      pip install bs4

.. rubric:: Example

The following example adds a :file:`_themes/` directory to the Sphinx project.
You can add local themes to this directory without installing Python packages.

.. code-block:: terminal
   :emphasize-lines: 4

   ./
   ├── conf.py
   ├── index.rst
   ├── _themes/
   └── ...

To load the theme from a local directory, follow these steps:

#. :ref:`sec:fork-and-clone`.
#. Copy the directory :file:`sphinxawesome-theme/src/sphinxawesome_theme/` into your Sphinx project:

   .. code-block:: terminal

      cp -r sphinxawesome-theme/src/sphinxawesome_theme _themes/

#. Add the :file:`_themes/` directory to the system path in the Sphinx configuration:

   .. code-block:: python
      :caption: File: conf.py

      sys.path.append(os.path.abspath("_themes"))

   Adding this directory makes it discoverable for Sphinx.

#. Exclude the :file:`_themes/` directory from searching for documentation files:

   .. code-block:: python
      :caption: File: conf.py

      exclude_patterns = ["_themes"]

   .. seealso::

      :confval:`sphinx:exclude_patterns`

#. :ref:`sec:add-to-sphinx`.
