.. _sec:install-js-deps:

Install JavaScript dependencies
-------------------------------

#. :ref:`sec:fork-and-clone`

#. Go to the :file:`theme-src/` directory:

   .. code-block:: bash
      :emphasize-lines: 4

      ./sphinxawesome-theme/
      ├── src/
      │   ├── sphinxawesome_theme/
      │   └── theme-src/
      ├── docs/
      ├── tests/
      └── ...

#. Install the JavaScript dependencies:

   .. code-block:: bash

      pnpm install

#. Build the theme:

   .. code-block:: bash

      pnpm run build
