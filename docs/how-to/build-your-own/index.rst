.. meta::
   :description: Make your own theme by building on top of this theme. Fully customize the styles, JavaScript, and templates.
   :twitter:description: Make your own theme by building on top of this theme. Fully customize the styles, JavaScript, and templates.

.. _sec:build-your-own:

Build your own theme
====================

.. rst-class:: lead

   Build your own theme by changing the templates or CSS.

----

The easiest way to install **all** dependencies is with mise_.

#. :ref:`sec:fork-and-clone`.

#. Install the dependencies.

   .. code-block:: bash

      mise install

#. Test, if everything is working.

   .. code-block:: bash

      hatch run dev:all

   This runs tests and the linter.

   Too see a list of available tasks, run:

   .. code-block:: bash

      hatch env show

#. Install JavaScript dependencies.

   Go to the :file:`src/theme-src` directory and run:

   .. code-block:: bash

      pnpm install

#. To build the JavaScript and CSS assets, run:

   .. code-block:: bash

      pnpm build

#. Optional: add DocSearch environment variables.

   If you have access to the environment variables for DocSearch,
   copy the file :file:`docs/.env.example` to :file:`docs/.env`
   and fill in the values. They're safe to expose on your website.

   By default, placeholder values are used and DocSerach won't work
   when developing locally.

.. _mise: https://mise.jdx.dev

If you don't want to use mise,
use your preferred version and package managers.
See the files :file:`mise.toml`, :file:`pyproject.toml`,
and :file:`src/theme-src/package.json` for more information.

Now you can make any change you want.
