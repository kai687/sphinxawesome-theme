.. _sec:install-js-deps:

Install JavaScript dependencies
-------------------------------

#. :ref:`sec:fork-and-clone`

#. Go to the :file:`theme-src/` directory:

   .. code-block:: sh
      :emphasize-lines: 4

      ./sphinxawesome-theme/
      ├── src/
      │   ├── sphinxawesome_theme/
      │   └── theme-src/
      ├── docs/
      ├── tests/
      └── ...

#. Install the JavaScript dependencies:

   .. code-block:: sh

      yarn install

#. Build the theme:

   .. code-block:: sh

      yarn build
