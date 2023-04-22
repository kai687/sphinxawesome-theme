.. _sec:install-js-deps:

Install JavaScript dependencies
-------------------------------

#. :ref:`sec:fork-and-clone`

#. Go to the :file:`theme-src/` directory:

   .. code-block:: terminal
      :emphasize-lines: 4

      ./sphinxawesome-theme/
      ├── src/
      │   ├── sphinxawesome_theme/
      │   └── theme-src/
      ├── docs/
      ├── tests/
      └── ...

#. Install the JavaScript dependencies:

   .. code-block:: terminal

      yarn install

#. Build the theme:

   .. code-block:: terminal

      yarn build
