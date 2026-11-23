.. _sec:install-local-package:

Install from a local directory
------------------------------

To build your own version of the theme,
clone the repository. Then install the cloned version
as a `local Python package <https://packaging.python.org/en/latest/tutorials/installing-packages/#installing-from-a-local-src-tree>`_.

#. :ref:`sec:fork-and-clone`.
#. Install the local copy of the theme in your project:

   .. code-block:: bash
      :emphasize-text: /path/to/sphinxawesome_theme

      pip install --editable /path/to/sphinxawesome_theme

   Replace :samp:`{/path/to/sphinxawesome_theme}` with the path to your local copy
   of the theme.
   The ``--editable`` option installs the package in editable mode (development mode).

After you install the theme, you can :doc:`add it to your project <../add/index>`.
