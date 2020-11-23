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

If you want to use the theme
without modifying it,
install it as a Python package.
You can still override the CSS
or add additional JavaScript files.
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

Setting up a development environment
------------------------------------

If you want to modify the theme,
install the project's dependencies.

The project is split into two separate parts.
If you want to edit the documentation,
or modify any Python code,
install the Python dependencies.
If you *just* want to modify the way
the theme looks or behaves, that is,
the HTML, CSS, or JavaScript,
install the JavaScript dependencies.

Regardless of which part of the theme
you want to modify, create a local copy
first.

Creating a local copy of the theme
----------------------------------

In order to modify the theme,
you need to create a local copy first.

To create a local copy of the theme,
follow these steps:

#. **Optional:** :term:`Fork the repository <forking a repository>`.
   If you don't want to merge your changes with the original repository,
   you can skip this step.

#. :term:`Clone the (forked) repository <cloning a repository>`.

   If you forked the repository, enter:

   .. samp::

      $ git clone https://github.com/{YOUR_GITHUB_USERNAME}/sphinxawesome-theme.git

   Replace :samp:`{YOUR_GITHUB_USERNAME}` with your user name on GitHub.
   If you didn't fork the repository,
   clone the original repository::

       $ git clone https://github.com/kai687/sphinxawesome-theme.git

Installing Python dependencies
------------------------------

If you want to edit the documentation,
or modify any of the Python code in
:dir:`sphinxawesome-theme/src/sphinxawesome_theme`,
follow these steps to install the project's Python dependencies.

#. Install Poetry_ and Nox_.
   Follow the recommended steps for `how to install Poetry`_.
   Install Nox via pip::

       $ pip install --user --upgrade nox

   If you want to use the same version of Poetry and Nox
   as the :term:`upstream` repository,
   check the file `constraints.txt`_.

   .. _Poetry: https://python-poetry.org/
   .. _how to install Poetry: https://python-poetry.org/docs/#installation
   .. _Nox: https://nox.thea.codes/en/stable/
   .. _constraints.txt: https://github.com/kai687/sphinxawesome-theme/blob/master/.github/workflows/constraints.txt


#. Install the project's dependencies inside a virtual environment::

       $ poetry install

   Check Poetry's documentation_ for more information.

   .. _documentation: https://python-poetry.org/docs/basic-usage/

#. Install pre-commit hooks::

       $ poetry run pre-commit install

   This command installs pre-commit hooks
   that are executed,
   whenever you commit to the repository.
   Check the file
   `.pre-commit-config.yaml`_
   to see which pre-commit hooks are configured.

  .. _.pre-commit-config.yaml: https://github.com/kai687/sphinxawesome-theme/blob/master/.pre-commit-config.yaml

   To test the pre-commit hooks, run::

       $ poetry run pre-commit run --all

#. Run a Nox session

   To check if the project is set up correctly,
   run any of the Nox sessions.
   For example, to build the documentation
   with Python 3.8::

      $ nox -s docs -p 3.8

   To list the available sessions, enter::

      $ nox -ls

Installing JavaScript dependencies
----------------------------------

If you want to modify the look and behavior of the theme,
follow these steps to install the JavaScript dependencies.

#. Check, if `Node.js <https://nodejs.org/en/>`_ is installed::

       $ node --version

   If this command does not return a Node.js version, for example::

       $ v12.18.3

   you need to install Node.js first.

#. **Optional:** Install ``yarn``::

       $ npm install --global yarn

   If you don't want to install yarn_,
   you can use ``npm`` as well.
   The commands in this documentation use ``yarn``.
   You can replace the commmands to *run* something,
   for example, ``yarn build``, with ``npm run build``.

   .. _yarn: https://yarnpkg.com/

#. Change to the :dir:`theme-src` directory.

   The repository :dir:`sphinxawesome-theme`
   has the following structure:

   .. code-block:: console
      :emphasize-lines: 4

      ./sphinxawesome-theme/
        ├src/
        │ ├sphinxawesome_theme/
        │ └theme-src/
        ├docs/
        └...

#. Install the JavaScript dependencies::

       $ yarn install

#. Build the theme::

       $ yarn build
