# How to install the theme

```{rst-class} lead
Depending on how you want to use the Sphinx awesome theme,
install it as a Python package or load it from a directory.
```

```{contents} On this page
:local:
:backlinks: none
```

## Install the theme as a Python package (recommended)

In most cases, it's best to install the theme as a Python package.
You can still modify the look and feel of the theme by adding
custom CSS or JavaScript files.
See {ref}`Add or override styles` for more information.

**To install the latest released version** from the Python Package Index
[PyPI](https://pypi.org/project/sphinxawesome-theme/), enter the following:

```shell-session
$ pip install sphinxawesome-theme
```

To install the latest development version of the theme directly from GitHub:

```shell-session
$ pip install git+https://github.com/kai687/sphinxawesome-theme.git
```

<!-- vale 18F.UnexpandedAcronyms = NO -->

See the "HEAD" section at the top of the
[CHANGELOG](https://github.com/kai687/sphinxawesome-theme/blob/master/CHANGELOG.rst)
file for features and bugfixes are available in the version on GitHub but not yet in
the released version.

<!-- vale 18F.UnexpandedAcronyms = YES -->

## Install the theme as a local package

If you want to use a modified version of the theme, you can load the theme from a local
Python package. This doesn't require any special configuration, but can be slower
initially, since you need to rebuild and reinstall the local package after each
modification.

1. {ref}`Create a local copy of the theme`
1. Build the theme as a Python package:

   ```shell-session
   $ poetry build
   ```

   This command creates a new directory `dist/` containing the source distribution in
   `.tar.bz2` format and as wheel in a `.whl` file.

1. In your project, install the theme from the locally built package:

   ```shell-session
   $ pip install /path/to/sphinxawesome_theme/dist/sphinxawesome_theme-*-py3-none-any.whl
   ```

   This command installs the pre-built package in the current environment.

   ````{tip}
   You can also skip the separate build step and install the top level directory:

   ```shell-session
   $ pip install /path/to/sphinxawesome_theme
   ```

   This command builds and installs the package in one step. It's a bit slower than the
   procedure outlined before.
   ````

## Set up a development environment

The project has two different sets of dependencies, for Python and JavaScript. If you
want to write documentation, write tests, or modify the Python extensions, install the
Python dependencies. See {ref}`Install Python dependencies` for more information.

If you want to modify the Jinja2 templates[^1], the CSS, or the JavaScript files, you
also need to install the JavaScript dependencies. See
{ref}`Install JavaScript dependencies` for more information.

<!-- vale Google.Colons = NO -->
<!-- vale 18F.SentenceLength = NO -->
<!-- vale 18F.Reading = NO -->

[^1]: Technically, you only need to add the JavaScript dependencies, if you want to _change_ the CSS classes inside the templates. For example, if you add a utility class that wasn't previously used, you need to run the JavaScript/CSS pipeline again to include it in the final style sheet.

<!-- vale Google.Colons = YES -->
<!-- vale 18F.SentenceLength = YES -->
<!-- vale 18F.Reading = YES -->

In both cases, create a local copy first.

## Create a local copy of the theme

In order to modify the theme, create a local copy first:

1. **Optional:** fork the repository

   <!-- vale Awesome.SpellCheck = NO -->

   If you don't want to merge your changes with the original repository, you can skip
   this step. See [Fork a
   repo](https://docs.github.com/en/get-started/quickstart/fork-a-repo) in the GitHub
   documentation for more information.
   <!-- vale Awesome.SpellCheck = YES -->

1. Clone the (forked) repository:

   If you forked the repository, enter:

   ```{code-block} shell-session
   ---
   emphasize-text: GITHUB_USERNAME
   ---
   $ git clone https://github.com/GITHUB_USERNAME/sphinxawesome-theme.git
   ```

   Replace {samp}`{GITHUB_USERNAME}` with your GitHub username. If you didn't fork
   the repository, clone the original repository:

   ```shell-session
   $ git clone https://github.com/kai687/sphinxawesome-theme.git
   ```

   See [Cloning a
   repository](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository)
   in the GitHub documentation for more information.

## Install Python dependencies

The Sphinx awesome theme uses [Poetry](https://python-poetry.org/) to manage the Python
dependencies. Testing, linting, and building the documentation is handled by
[Nox](https://nox.thea.codes/en/stable/).

Follow these steps to install the Python dependencies:

1. Follow the recommended steps for [how to install Poetry](https://python-poetry.org/docs/#installation).

   On macOS and Linux, enter:

   ```shell-session
   $ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
   ```

   On Windows PowerShell:

   ```Powershell
   (Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py -UseBasicParsing).Content | python -
   ```

1. Install Nox via pip:

   ```shell-session
   $ pip install --user --upgrade nox
   ```

   If you want to use the same version of Poetry and Nox as the original repository, see
   the versions in the file
   [`constraints.txt`](https://github.com/kai687/sphinxawesome-theme/blob/master/.github/workflows/constraints.txt)

1. Install the Python dependencies:

   ```shell-session
   $ poetry install
   ```

   Check Poetry's [documentation](https://python-poetry.org/docs/basic-usage/) for more information.

   <!-- vale 18F.Clarity = NO -->

1. **Optional:** install pre-commit hooks:

   ```shell-session
   $ poetry run pre-commit install
   ```

   If you don't plan on committing any changes to the forked repository, you can skip
   this step. Check the file
   [`.pre-commit-config.yaml`](https://github.com/kai687/sphinxawesome-theme/blob/master/.pre-commit-config.yaml)
   to see which pre-commit hooks are active.

   To test pre-commit in combination with poetry, run:

   ```shell-session
   $ poetry run pre-commit run --all
   ```

   <!-- vale 18F.Clarity = YES -->

1. Run a Nox session.

   You can run any Nox session to confirm that the environment is working.
   To list the available sessions, enter:

   ```shell-session
   $ nox -ls
   ```

   Enter `nox` without any option to run the default sessions,
   such as building the docs, testing, and linting.

   For example, to build the documentation with Python 3.9, enter:

   ```shell-session
   $ nox -s docs -p 3.9
   ```

## Install JavaScript dependencies

Follow these steps to install the JavaScript dependencies:

1. Check, if [Node.js](https://nodejs.org/en/) is installed:

   ```shell-session
   $ node --version
   ```

   If Node.js is installed, this command returns the version number,
   for example:

   ```shell-session
   v14.17.4
   ```

   If the command fails, you may need to install Node.js first,
   or activate it in your current terminal session.
   Have a look at the [Node Version Manager](https://github.com/nvm-sh/nvm)
   project for a way to install and manage multiple versions of Node.js.

1. **Optional:** install [`yarn`](https://classic.yarnpkg.com/lang/en/):

   ```shell-session
   $ npm install --global yarn
   ```

   The awesome theme uses yarn (classic). The dependencies are pinned to the specific
   versions in the `yarn.lock` file. If you don't want to use the same versions of the
   JavaScript packages, you can use `npm` as well.

1. Change to the `theme-src/` directory:

   ```{code-block} shell
   ---
   emphasize-lines: 4
   ---
   ./sphinxawesome-theme/
      ├src/
      │ ├sphinxawesome_theme/
      │ └theme-src/
      ├docs/
      └...
   ```

1. Install the JavaScript dependencies:

   ```shell-session
   $ yarn install
   ```

1. Build the theme:

   ```shell-session
   $ yarn build
   ```
