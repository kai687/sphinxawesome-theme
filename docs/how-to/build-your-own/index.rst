.. meta::
   :description: Make your own theme by building on top of this theme. Fully customize the styles, JavaScript, and templates.
   :twitter:description: Make your own theme by building on top of this theme. Fully customize the styles, JavaScript, and templates.

Build your own theme
====================

.. rst-class:: lead

   Build your own theme by changing the templates or CSS.

----

The easiest way to install **all** dependencies is with mise_.

#. :ref:`sec:fork-and-clone`.

#. Optional: enable support for mise's experimental ``postinstall`` hook.

   .. code-block:: bash

      mise settings experimental=true

   .. tip::

      This automatically installs the required Nox_ tool after uv_ is installed.
      If you don't want to do this, run ``uv tool install nox`` after uv is installed.

#. Install Python and Node.js dependencies:

   .. code-block:: bash

      mise install

#. If you didn't enable support for mise's experimental ``postinstall`` hook,
   run:

   .. code-block:: bash

      uv tool install nox
      uv tool install pre-commit
      pre-commit install --hook-type pre-push

#. Test, if everything is working:

   .. code-block:: bash

      nox --list-sessions
      pre-commit run --all

    After making changes to any template or Python file, run:

    .. code-block:: bash

       nox

    This runs a few checks and builds the docs to make sure your changes
    work as expected.

#. If you want to contribute to the docs and test a local preview,
   create a :file:`.env` file with dummy values:

   .. code-block:: bash

      DOCSEARCH_APP_ID=tmp
      DOCSEARCH_API_KEY=tmp
      DOCSEARCH_INDEX_NAME=tmp

   .. note::

      For building the docs, these environment variables need to be defined.
      With dummy values, the search won't work in your local preview.

#. Install JavaScript dependencies.

   Go to the :file:`src/theme-src` directory and run:

   .. code-block:: bash

      pnpm install

#. To build the JavaScript and CSS assets, run:

   .. code-block:: bash

      pnpm build

.. _mise: https://mise.jdx.dev
.. _uv: https://docs.astral.sh/uv/
.. _Nox: https://nox.thea.codes/en/stable/

If you don't want to use mise,
use your preferred version and package managers.
See the files :file:`mise.toml`, :file:`pyproject.toml`,
and :file:`src/theme-src/package.json` for more information.
