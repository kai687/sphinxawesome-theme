.. meta::
   :description: Make your own theme by building on top of this theme. Fully customize the styles, JavaScript, and templates.

Build your own theme
====================

.. rst-class:: lead

   Build your own theme by changing the templates or CSS.

.. contents:: On this page
   :local:
   :backlinks: none

The project has both Python and JavaScript dependencies.
If you want to write documentation or modify the Python extensions,
:ref:`install the Python dependencies <sec:install-python-deps>`.

If you want to edit the Jinja2 templates, the CSS, or the JavaScript files,
you also need to :ref:`install the JavaScript dependencies <sec:install-js-deps>`.

.. note::

   Because this theme uses `Tailwind CSS <https://tailwindcss.com>`_ to apply styles,
   you  need to build the theme when you make modifications to the styles.
   It's best to install the JavaScript dependencies,
   even if you just want to edit the HTML templates.

.. _sec:install-python-deps:

Prepare Python environment
--------------------------

The |product| uses these Python tools:

- Poetry_ to manage the Python dependencies and building the package
- Nox_ to test and lint the Python code, and to build the docs
- Pipx_ to install Python applications in isolated environments and making them available globally

.. _Poetry: https://python-poetry.org/
.. _Nox: https://nox.thea.codes/en/stable/
.. _Pipx: https://pypa.github.io/pipx/

If you want to use the same versions of the Python tools,
you can provide a :gh:`constraints.txt <constraints.txt>` to the install commands.

To prepare the Python environment, run these commands:

.. code-block:: terminal

   pip install --user pipx [--constraint=constraints.txt]
   pipx install poetry [--pip-args=--constraint=constraints.txt]
   pipx install nox [--pip-args=--constraint=constraints.txt]
   pipx inject nox nox-poetry [--pip-args=--constraint=constraints.txt]

Nox-poetry is a package for using Poetry and Nox together.
It must be installed in the same environment as Nox.

Install the Python dependencies
-------------------------------

#. :ref:`sec:fork-and-clone`.

#. Install the Python dependencies:

   .. code-block:: terminal

      poetry install

#. Optional: install and test the pre-commit hooks:

   .. code-block:: terminal

      poetry run pre-commit install

   If you don't plan on committing any changes to the repository,
   you can skip this step.
   You can see the active pre-commit hooks in the file :gh:`.pre-commit-config.yaml`.

   To test pre-commit with Poetry, run:

   .. code-block:: terminal

      poetry run pre-commit run --all

#. Test your Nox environment.

   You can run any Nox session to confirm that the environment is working.
   To list the available sessions, run:

   .. code-block:: terminal

      nox --list-sessions

   For example, run all default sessions:

   .. code-block:: terminal

      nox

Prepare JavaScript environment
------------------------------

#. Confirm that `Node.js <https://nodejs.org/en/>`_ is installed:

   .. code-block:: terminal

      $ node --version
      v20.00.0

   If the preceding command fails, make sure that you installed Node.js.
   If you installed Node.js, make sure that the path to the ``node``
   executable is in your ``PATH`` environment variable.

   .. tip::

      For installing and managing different Node.js versions,
      see these projects: `nvm <https://github.com/nvm-sh/nvm>`_,
      `fnm <https://github.com/Schniz/fnm>`_,
      `Volta <https://volta.sh/>`_,
      `asdf <https://asdf-vm.com/>`_.

#. Optional: install `yarn <https://yarnpkg.com/>`_:

   .. code-block:: terminal

      npm install --global yarn

   If you want to use the same versions of JavaScript packages as in the |product| repository,
   use the Yarn package manager.

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
