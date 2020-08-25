Setting up a development environment
====================================

.. highlight:: console

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
   If you don't plan on merging your changes with the original repository,
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

#. Install Poetry_ and Nox_. Follow the recommended steps on `how to install Poetry`_.
   Nox can be installed via pip, for example::

       $ pip install --user --upgrade nox

   If you want to make sure,
   you are using the same version of Poetry and Nox as the :term:`upstream` repository,
   check the file `constraints.txt`_.

   .. _Poetry: https://python-poetry.org/
   .. _how to install Poetry: https://python-poetry.org/docs/#installation
   .. _Nox: https://nox.thea.codes/en/stable/
   .. _constraints.txt: https://github.com/kai687/sphinxawesome-theme/blob/master/.github/workflows/constraints.txt


#. Install the project's dependencies::

       $ poetry install

   This installs all dependencies inside a virtual environment.
   Check Poetry's documentation_ for more information.

   .. _documentation: https://python-poetry.org/docs/basic-usage/

#. Install pre-commit hooks::

       $ poetry run pre-commit install

   Pre-commit is a development dependency of this project.
   You can run it from within the project's virtual environment.
   This command installs pre-commit hooks
   that are executed,
   whenever you commit to the repository.
   Check the file
   `.pre-commit-config.yaml <https://github.com/kai687/sphinxawesome-theme/blob/master/.pre-commit-config.yaml>`_
   to see which pre-commit-hooks are configured.

   To test the pre-commit hooks without actually committing anything,
   run::

       $ poetry run pre-commit run --all

#. Run a Nox session

   To see if the project is setup correctly,
   run any of the defined Nox sessions.
   For example:

   .. code-block:: console

      $ nox -s docs -p 3.8

   This builds the documentation with the Python 3.8 interpreter.
   To see the available sessions, enter:

   .. code-block:: console

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

   Change to the :dir:`theme-src` directory.

#. Install the JavaScript dependencies::

       $ yarn install

#. Build the theme::

       $ yarn build
