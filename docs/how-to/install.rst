How to install the theme
========================

.. set the default highlighting language for this document
.. highlight:: console

Depending on how you want to use the theme
and its extensions, use one of the following
methods to install the Sphinx awesome theme.

.. contents:: On this page
   :local:
   :backlinks: none

Installing the theme as a Python package (recommended)
------------------------------------------------------

In most cases,
you should install the theme as a Python package.
You can make small modifications
by adding custom CSS or JavaScript files.
See :ref:`Adding or overriding styles`
for more information.

You can install a released version
from the Python Package Index (PyPI_)::

    $ pip install sphinxawesome-theme

.. _PyPI: https://pypi.org/project/sphinxawesome-theme/

You can also install the latest development version
of the theme directly from GitHub::

    $ pip install git+https://github.com/kai687/sphinxawesome-theme.git

Check the "MASTER" section at the top of the CHANGELOG_ file.
These features and bugfixes are available
in the version on GitHub
but not yet in the released version on PyPI_.

.. _CHANGELOG: https://github.com/kai687/sphinxawesome-theme/blob/master/CHANGELOG.rst

Installing the theme as a local package
---------------------------------------

If you want to use a modified version of the theme,
you can load the theme from a local Python package.
This doesn't require any special configuration,
but can be slower initially,
since you need to rebuild and reinstall the local package
after each modification.

#. :ref:`Create a local copy <Creating a local copy of the theme>`

#. Build the theme as a Python package.

   .. code-block:: console

      $ poetry build

   This command creates a new directory :dir:`dist` containing the
   source distribution in ``.tar.bz2`` format and as wheel in a ``.whl``
   file.

#. In your project, install the theme from the locally built package.

   .. code-block:: console

      $ pip install /path/to/sphinxawesome_theme/dist/sphinxawesome_theme-*-py3-none-any.whl

   This command installs the pre-built package in the current environment.

.. tip::

   You can also skip the separate build step and install the top level directory:

   .. code-block:: console

      $ pip install /path/to/sphinxawesome_theme

   This command builds and installs the package in one step.
   It's a bit slower than the procedure outlined before.

Setting up a development environment
------------------------------------

The project has two different sets of dependencies.
If you want to write documentation,
write tests,
or modify the Python extensions,
install the Python dependencies.
See :ref:`Installing Python dependencies` for more information.

If you want to modify the Jinja2 templates, the CSS,
or the JavaScript files,
you also need to install the JavaScript dependencies.
See :ref:`Installing JavaScript dependencies` for more information.

In both cases,
create a local copy first.

Creating a local copy of the theme
----------------------------------

In order to modify the theme,
create a local copy first:

#. **Optional:** fork the repository.

   If you don't want to merge your changes with the original repository,
   you can skip this step. See `Fork a repo`_  in the GitHub documentation
   for more information.

   .. _Fork a repo: https://docs.github.com/en/github/getting-started-with-github/fork-a-repo

#. Clone the (forked) repository.

   If you forked the repository, enter:

   .. samp::

      $ git clone https://github.com/{YOUR_GITHUB_USERNAME}/sphinxawesome-theme.git

   Replace :samp:`{YOUR_GITHUB_USERNAME}` with your user name on GitHub.
   If you didn't fork the repository,
   clone the original repository::

       $ git clone https://github.com/kai687/sphinxawesome-theme.git

   See `Cloning a repository`_ in the GitHub documentation for more information.

   .. _Cloning a repository: https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository

Installing Python dependencies
------------------------------

The Sphinx awesome theme uses Poetry_ to
manage the Python dependencies. Testing,
linting, and building the documentation
is handled by Nox_.

.. _Poetry: https://python-poetry.org/
.. _Nox: https://nox.thea.codes/en/stable/

Follow these steps to install the Python dependencies:

#. Install Poetry and Nox.

   Follow the recommended steps for `how to install Poetry`_.
   Install Nox via pip::

       $ pip install --user --upgrade nox

   If you want to use the same version of Poetry and Nox as the original repository,
   see the versions in the file `constraints.txt`_.

   .. _how to install Poetry: https://python-poetry.org/docs/#installation
   .. _constraints.txt: https://github.com/kai687/sphinxawesome-theme/blob/master/.github/workflows/constraints.txt

#. Install the dependencies.

   .. code-block:: console

       $ poetry install

   Check Poetry's documentation_ for more information.

   .. _documentation: https://python-poetry.org/docs/basic-usage/

#. **Optional:** install pre-commit hooks.

   .. code-block:: console

       $ poetry run pre-commit install

   If you don't plan on committing any changes to the forked repository,
   you can skip this step.
   Check the file `.pre-commit-config.yaml`_ to see
   which pre-commit hooks are active.

   .. _.pre-commit-config.yaml: https://github.com/kai687/sphinxawesome-theme/blob/master/.pre-commit-config.yaml

   To test pre-commit in combination with poetry, run::

       $ poetry run pre-commit run --all

#. Run a Nox session.

   You can run any Nox session to confirm that the environment is working.
   To list the available sessions, enter::

      $ nox -ls

   Enter ``nox`` without any option to run the default sessions,
   such as building the docs, testing, and linting.

   To build the documentation, for example, with Python 3.9::

      $ nox -s docs -p 3.9

Installing JavaScript dependencies
----------------------------------

Follow these steps to install the JavaScript dependencies:

#. Check, if `Node.js <https://nodejs.org/en/>`_ is installed.

   .. code-block:: console

       $ node --version

   If Node.js is installed, this command returns the version number,
   for example::

       $ v14.15.0

   If the command fails, you may need to install Node.js first,
   or activate it in your current terminal session.
   Have a look at the `Node Version Manager`_
   project for a way to install and manage multiple versions of Node.js.

   .. _Node Version Manager: https://github.com/nvm-sh/nvm

#. **Optional:** install ``yarn``.

   .. code-block:: console

       $ npm install --global yarn

   The awesome theme uses yarn_ (classic).
   The dependencies are pinned to the specific versions
   in the :file:`yarn.lock` file.
   If you don't want to use the same versions of the JavaScript
   packages, you can use ``npm`` as well.

   .. _yarn: https://classic.yarnpkg.com/lang/en/

#. Change to the :dir:`theme-src` directory.

   .. code-block:: console
      :emphasize-lines: 4

      ./sphinxawesome-theme/
        ├src/
        │ ├sphinxawesome_theme/
        │ └theme-src/
        ├docs/
        └...

#. Install the JavaScript dependencies.

   .. code-block::

       $ yarn install

#. Build the theme.

   .. code-block:: console

       $ yarn build
