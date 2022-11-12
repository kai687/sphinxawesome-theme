---
myst:
  html_meta:
    description: |
      Learn how to install the Awesome Theme for your documentation project.
---

(sec:install)=

# Install the theme

```{rst-class} lead
Install the {{ product }} as a Python package,
copy it into a local directory,
or install a full development environment.
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

```terminal
pip install sphinxawesome-theme
```

To install the latest **development version**, run:

```terminal
pip install git+https://github.com/kai687/sphinxawesome-theme.git
```

<!-- vale 18F.UnexpandedAcronyms = NO -->

See the {gh}`CHANGELOG <CHANGELOG.md>` file for extra features and updates in the
development version that aren't released yet.

<!-- vale 18F.UnexpandedAcronyms = YES -->

If you want to add styles or extra templates,
see {ref}`customize the theme <sec:customize>`.

## Install the theme from a local directory

If you want to customize the theme,
you can clone the repository and install the cloned version
as a [local Python package](https://packaging.python.org/en/latest/tutorials/installing-packages/#installing-from-a-local-src-tree).

1. {ref}`sec:fork-and-clone`.
1. Install the local copy of the theme in your project:

   ```{code-block} terminal
   ---
   emphasize-text: "/path/to/sphinxawesome_theme"
   ---
   pip install --editable /path/to/sphinxawesome_theme
   ```

   Replace {samp}`{/path/to/sphinxawesome_theme}` with the path to your local copy
   of the theme (the directory with the `pyproject.toml` file).
   The `--editable` option installs the package in editable, or development, mode.

(sec:dev-env)=

## Set up a development environment

The project has both Python and JavaScript dependencies.
If you want to write documentation or modify the Python extensions,
{ref}`install the Python dependencies <sec:install-python-deps>`.

If you want to edit the Jinja2 templates, the CSS, or the JavaScript files,
you also need to {ref}`install the JavaScript dependencies <sec:install-js-deps>`.

```{note}
Because this theme uses [Tailwind CSS](https://tailwindcss.com) to apply styles,
you need to _build_ the theme when you make modifications to the styles.
It's best to install the JavaScript dependencies,
even if you just want to edit the HTML templates.
```

(sec:fork-and-clone)=

### Create a local copy of the repository

1. Optional: [fork the repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo).

   If you don't want to merge your changes with the original repository, you can skip
   this step.

1. Clone the repository:

   - If you forked the repository, run:

     ```{code-block} terminal
     ---
     emphasize-text: GITHUB_USERNAME
     ---
     git clone https://github.com/GITHUB_USERNAME/sphinxawesome-theme.git
     ```

     Replace {samp}`{GITHUB_USERNAME}` with your GitHub username.

   - If you didn't fork the repository, clone the original repository:

     ```terminal
     git clone https://github.com/kai687/sphinxawesome-theme.git
     ```

```{seealso}
[Clone a repository from GitHub](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
```

(sec:install-python-deps)=

<!-- vale Google.Headings = NO -->

### Install Python dependencies

<!-- vale Google.Headings = YES -->

The {{ product }} uses these Python tools:

- [Poetry](https://python-poetry.org/) to manage the Python dependencies and building the package
- [Nox](https://nox.thea.codes/en/stable/) to test and lint the Python code, and to build the docs
- [Pipx](https://pypa.github.io/pipx/) to install Python applications in isolated environments and making them available globally

```{note}
The commands shown in this section install the latest versions of Nox and Poetry.
See the file {gh}`constraints.txt <.github/workflows/constraints.txt>`
for the version numbers of Nox and Poetry used for building the {{ product }} Python package.
```

Follow these steps to install the Python dependencies:

1. {ref}`sec:fork-and-clone`

1. [Install pipx](https://pypa.github.io/pipx/#install-pipx):

   ```terminal
   pip install --user pipx
   ```

1. [Install Poetry](https://python-poetry.org/docs/master/#installing-with-pipx):

   ```terminal
   pipx install poetry
   ```

1. [Install Nox](https://github.com/wntrblm/nox/#installation):

   ```terminal
   pipx install nox
   ```

1. [Install nox-poetry](https://github.com/cjolowicz/nox-poetry/#installation):

   ```terminal
   pipx inject nox nox-poetry
   ```

   Nox-poetry is a package for using Poetry and Nox together.
   The `nox-poetry` package must be installed in the same environment as Nox.

1. Install the Python dependencies:

   ```terminal
   poetry install
   ```

   <!-- vale 18F.Clarity = NO -->

1. Optional: install and test the pre-commit hooks:

   ```terminal
   poetry run pre-commit install
   ```

   If you don't plan on committing any changes to the repository, you can skip
   this step. You can see the active pre-commit hooks in the file {gh}`.pre-commit-config.yaml`.

   To test pre-commit with Poetry, run:

   ```terminal
   poetry run pre-commit run --all
   ```

   <!-- vale 18F.Clarity = YES -->

1. Test your Nox environment.

   You can run any Nox session to confirm that the environment is working.
   To list the available sessions, run:

   ```terminal
   nox --list-sessions
   ```

   For example, run all default sessions:

   ```terminal
   nox
   ```

#### Using the same versions of the Python packages

The commands in the preceding section install the latest versions of Poetry, Nox, and pipx.
If you want to _constrain_ the versions to install, you can use pip's [constraint file](https://pip.pypa.io/en/stable/user_guide/#constraints-files).

For example, to install a specific version of pipx, run:

```terminal
pip install --user --constraint=constraints.txt pipx
```

For example, to install a specific version of Nox with pipx, run:

```terminal
pipx --pip-args=--constraint=constraints.txt nox
```

See the file {gh}`constraints.txt` for the version constraints used in the {{ product }} repository.

```{tip}
In development environments, you might use the latest versions of packages,
while for reproducible results in continuous integration (CI) pipelines,
it's often better to install specific versions of packages.
```

(sec:install-js-deps)=

### Install JavaScript dependencies

1. Confirm that [Node.js](https://nodejs.org/en/) is installed:

   ```terminal
   $ node --version
   v16.16.0
   ```

   If the preceding command fails, make sure that you installed Node.js.
   If you installed Node.js, make sure that the path to the `node`
   executable is in your `PATH` environment variable.

   ```{note}
   For installing and managing Node.js versions, see these projects:

   - [nvm](https://github.com/nvm-sh/nvm)
   - [Volta](https://volta.sh/)
   - [asdf](https://asdf-vm.com/)
   ```

1. Optional: install [`yarn`](https://yarnpkg.com/):

   ```terminal
   npm install --global yarn
   ```

   If you want to use the same versions of JavaScript packages as in the {{ product }}
   repository, use the Yarn package manager.

1. {ref}`sec:fork-and-clone`

1. Go to the `theme-src/` directory:

   ```{code-block} terminal
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

   ```terminal
   yarn install
   ```

1. Build the theme:

   ```terminal
   yarn build
   ```
