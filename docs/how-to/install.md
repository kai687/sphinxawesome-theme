---
html_theme:
  description: |
    Learn how to install the Awesome Theme for your documentation project.
---

(sec:install)=

# Install the theme

```{rst-class} lead
Install the {{ product }} as a Python package,
copy it into a local directory,
or install the development dependencies to create your own theme.
```

```{contents} On this page
---
local: true
backlinks: none
---
```

(sec:install-python-package)=

## Install the theme as a Python package (recommended)

Install the latest **released version** from the Python Package Index
[PyPI](https://pypi.org/project/sphinxawesome-theme/):

```shell-session
pip install sphinxawesome-theme
```

You can also install the latest **development version**:

```shell-session
pip install git+https://github.com/kai687/sphinxawesome-theme.git
```

<!-- vale 18F.UnexpandedAcronyms = NO -->

See the {gh}`CHANGELOG <CHANGELOG.rst>` file for extra features and updates in the
development version that aren't released yet.

<!-- vale 18F.UnexpandedAcronyms = YES -->

If you want to add styles or extra templates,
see {ref}`customize the theme <sec:customize>`.

## Install the theme as a local Python package

If you want to modify the theme and test your modifications first,
you can install the theme as a local Python package.

1. {ref}`sec:fork-and-clone`.
1. To install the local version of the theme in your project:

   ```{code-block} shell-session
   ---
   emphasize-text: "/path/to/sphinxawesome_theme"
   ---
   pip install /path/to/sphinxawesome_theme
   ```

   Replace {samp}`{/path/to/sphinxawesome_theme}` with the path to your local directory
   with the theme (the directory with the `pyproject.toml` file).

(sec:dev-env)=

## Set up a development environment

The project has two different sets of dependencies---for Python and JavaScript. If you
want to write documentation or modify the Python extensions,
{ref}`install the Python dependencies <sec:install-python-deps>`.

If you want to modify the Jinja2 templates, the CSS, or the JavaScript files, you also
need to {ref}`install the JavaScript dependencies <sec:install-js-deps>`.

```{note}
Because this theme uses [Tailwind CSS](https://tailwindcss.com) to apply styles,
you need to _build_ the theme when you make modifications to the styles.
It's best to install the JavaScript dependencies,
even if you just want to edit the HTML templates.
```

(sec:fork-and-clone)=

## Create a local copy of the theme

To modify the theme, create a local copy:

1. Optional: [fork the repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo).

   If you don't want to merge your changes with the original repository, you can skip
   this step.

1. Clone the repository:

   - If you forked the repository, enter:

     ```{code-block} shell-session
     ---
     emphasize-text: GITHUB_USERNAME
     ---
     git clone https://github.com/GITHUB_USERNAME/sphinxawesome-theme.git
     ```

     Replace {samp}`{GITHUB_USERNAME}` with your GitHub username.

   - If you didn't fork the repository, clone the original repository:

     ```shell-session
     git clone https://github.com/kai687/sphinxawesome-theme.git
     ```

```{seealso}
[Clone a repository from GitHub](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
```

(sec:install-python-deps)=

## Install Python dependencies

The {{ product }} uses [Poetry](https://python-poetry.org/) to manage the Python
dependencies and [Nox](https://nox.thea.codes/en/stable/) to test and lint the code.

```{note}
The commands below install the latest versions of Nox and Poetry.
In case of a version conflict,
see the file {gh}`constraints.txt <.github/workflows/constraints.txt>`
for the version numbers used when building the {{ product }} Python package.
```

Follow these steps to install the Python dependencies:

1. {ref}`sec:fork-and-clone`.

1. [Install Poetry](https://python-poetry.org/docs/master/#installing-with-the-official-installer).

1. Install Nox:

   ```shell-session
   pip install --user --upgrade nox
   ```

1. Install the Python dependencies:

   ```shell-session
   poetry install
   ```

   <!-- vale 18F.Clarity = NO -->

1. Optional: install and test the pre-commit hooks:

   ```shell-session
   poetry run pre-commit install
   ```

   If you don't plan on committing any changes to the repository, you can skip
   this step. The active pre-commit hooks are defined in the file {gh}`.pre-commit-config.yaml`.

   To test pre-commit with Poetry, run:

   ```shell-session
   poetry run pre-commit run --all
   ```

   <!-- vale 18F.Clarity = YES -->

1. Test your Nox environment.

   You can run any Nox session to confirm that the environment is working.
   To list the available sessions, enter:

   ```shell-session
   nox -ls
   ```

   For example, to build the documentation with Python 3.10, enter:

   ```shell-session
   nox -s docs -p 3.10
   ```

(sec:install-js-deps)=

## Install JavaScript dependencies

1. Confirm that [Node.js](https://nodejs.org/en/) is installed:

   ```{command-output} node --version

   ```

   If the preceding command fails, make sure that you installed Node.js.
   If you installed Node.js, make sure that the path to the `node`
   executable is in your `PATH` environment variable.

   To install and manage multiple versions of Node.js,
   see the [Node Version Manager](https://github.com/nvm-sh/nvm) project.

1. Optional: install [`yarn`](https://classic.yarnpkg.com/lang/en/):

   ```shell-session
   npm install --global yarn
   ```

   If you want to use the same versions of JavaScript packages as in the {{ product }}
   repository, use the Yarn package manager.

1. {ref}`sec:fork-and-clone`.

1. Go to the `theme-src/` directory:

   ```{code-block} shell-session
   ---
   emphasize-lines: 4
   ---
   ./sphinxawesome-theme/
   ├── src/
   │   ├── sphinxawesome_theme/
   │   └── theme-src/
   ├── docs/
   ├── tests/
   └── ...
   ```

1. Install the JavaScript dependencies:

   ```shell-session
   yarn install
   ```

1. Build the theme:

   ```shell-session
   yarn build
   ```
