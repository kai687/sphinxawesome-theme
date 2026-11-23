.. meta::
   :description: Make your own theme by building on top of this theme. Fully customize the styles, JavaScript, and templates.
   :twitter:description: Make your own theme by building on top of this theme. Fully customize the styles, JavaScript, and templates.

.. _sec:build-your-own:

Build your own theme
====================

.. rst-class:: lead

   Build your own theme by changing the templates or CSS.

----

To install **all** dependencies, use mise_.

#. :ref:`sec:fork-and-clone`.

#. Install the dependencies.

   .. code-block:: bash

      mise install

#. Make sure that everything works.

   .. code-block:: bash

      mise run quality

   This command runs the linter and the type checker.

   To see a list of the available tasks, run:

   .. code-block:: bash

      mise tasks

#. Install JavaScript dependencies.

   Go to the :file:`src/theme-src` directory. Then run:

   .. code-block:: bash

      pnpm install

#. Build the JavaScript and CSS assets:

   .. code-block:: bash

      pnpm build

#. Optional: add DocSearch environment variables.

   If you have the environment variables for DocSearch,
   copy the file :file:`docs/.env.example` to :file:`docs/.env`.
   Then enter the values in the new file.
   It is safe to show these values on your website.

   By default, the build uses placeholder values.
   With these values, DocSearch does not work during local development.

.. _mise: https://mise.jdx.dev

If you do not want to use mise,
use your preferred version manager and package manager.
For more information, read the files :file:`mise.toml`, :file:`pyproject.toml`,
and :file:`src/theme-src/package.json`.

Now you can change the theme.
