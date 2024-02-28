"""Run commands for this repository."""

from __future__ import annotations

import tempfile

import nox

nox.options.stop_on_first_error = True
nox.options.sessions = ["docs", "lint", "fmt", "mypy", "tests"]

python_versions = ["3.12", "3.11", "3.10", "3.9", "3.8"]
session_install = nox.Session.install


class PoetryNoxSession(nox.Session):
    """Class for monkey-patching the Session object."""

    def export(self: PoetryNoxSession, group: str, file_name: str) -> None:
        """Export a group's dependencies from poetry.

        Args:
            group: The name of the dependency group from :file:`pyproject.toml`.
            file_name: The file name for exporting the dependencies.
        """
        self.run(
            "poetry",
            "export",
            "--without-hashes",
            "--only",
            group,
            "--output",
            file_name,
            external=True,
        )

    def install(self: PoetryNoxSession, group: str, *args: str) -> None:  # type: ignore
        """Install a group's dependencies into the nox virtual environment.

        To make Nox use the version constraints as defined in :file:`pyproject.toml` ,
        we have to export the dependencies into a temporary :file:`requirements.txt`.

        Args:
            group: The dependency group to export.
            *args: The packages to install, passed on to :meth:`nox.Session.install`.
        """
        with tempfile.NamedTemporaryFile() as requirements:
            self.export(group, requirements.name)
            session_install(self, "-r", requirements.name, *args)


# Monkey-patch galore
nox.Session.install = PoetryNoxSession.install  # type: ignore
nox.Session.export = PoetryNoxSession.export  # type: ignore


@nox.session(python=python_versions)
def tests(session: nox.Session) -> None:
    """Run unit tests."""
    args = session.posargs or ["--cov"]
    deps = ["coverage[toml]", "pytest", "pytest-cov", "sphinx-design"]
    session.install("dev", ".", *deps)
    session.run("pytest", *args)


@nox.session(python=python_versions)
def docs(session: nox.Session, live: bool = False, verbose: bool = False) -> None:
    """Build the docs.

    Args:
        session: The nox session instance.
        live: If ``True``, use :cmd:`sphinx-autobuild` to build the docs with a live-reloading server.
              If ``False``, use the regular :cmd:`sphinx-build`.
        verbose: If ``True``, run sphinx in verbose mode (``-vvv``).
    """
    args = ["-b", "dirhtml", "-aWTE", "docs", "docs/public"]
    deps = ["sphinx", "bs4", "sphinx-sitemap", "sphinx-design", "sphinx-docsearch"]
    sphinx_build = "sphinx-build"

    if "--live" in session.posargs:
        live = True
        session.posargs.remove("--live")

    if "--verbose" in session.posargs:
        verbose = True
        session.posargs.remove("--verbose")

    if live:
        deps.append("sphinx-autobuild")
        sphinx_build = "sphinx-autobuild"
        args += ["-A", "mode=development", "--watch", "src/sphinxawesome_theme"]

    if verbose:
        args += ["-vvv"]

    if session.posargs:
        args += session.posargs

    session.install("docs", ".", *deps)
    session.run(sphinx_build, *args)


@nox.session
def live_docs(session: nox.Session) -> None:
    """Build the docs with :cmd:sphinx-autobuild`."""
    verbose = bool("--verbose" in session.posargs)
    docs(session, True, verbose)


@nox.session
def linkcheck(session: nox.Session) -> None:
    """Check links."""
    args = session.posargs or ["-b", "linkcheck", "-aWTE", "docs", "docs/public/_links"]
    deps = ["sphinx", "bs4", "sphinx-sitemap", "sphinx-design", "sphinx-docsearch"]
    session.install("docs", ".", *deps)
    session.run("sphinx-build", *args)


@nox.session
def xml(session: nox.Session) -> None:
    """Build XML version of the docs."""
    args = ["-b", "xml", "-aWTE", "docs", "docs/public/xml"]
    deps = ["sphinx", "bs4", "sphinx-sitemap", "sphinx-design", "sphinx-docsearch"]
    session.install("docs", ".", *deps)
    session.run("sphinx-build", *args)


@nox.session(venv_backend=None)
def export(session: nox.Session) -> None:
    """Export a :file`requirements.txt` file for Netlify (Python 3.8).

    On Netlify, we install Poetry, Pip, and Pipx with the same versions
    as specified in :file:`requirements.txt`. Then, we use poetry
    to install the regular dependencies, just like on a local machine.

    On GitHub actions, we use the same file, although it runs on Python 3.11.
    """
    session.export("netlify", "requirements.txt")  # type: ignore[attr-defined]

    session.run(
        "poetry",
        "export",
        "--without-hashes",
        "--with",
        "docs",
        "--output",
        "docs/readthedocs.txt",
        external=True,
    )


@nox.session(python=python_versions)
def lint(session: nox.Session) -> None:
    """Lint python files."""
    deps = ["ruff"]
    session.install("lint", ".", *deps)
    session.run("ruff", ".")


@nox.session
def fmt(session: nox.Session) -> None:
    """Format python files."""
    deps = ["ruff"]
    session.install("lint", ".", *deps)
    session.run("ruff", "check", ".", "--fix")
    session.run("ruff", "format", ".")


@nox.session(python=["3.8", "3.12"])
def mypy(session: nox.Session) -> None:
    """Type-check python files with mypy.

    Usually, issues occur either for all versions or the earliest
    supported version, so running for these two is usually enough.
    """
    # We need to install these additional libraries or Mypy will complain
    deps = ["mypy", "pytest", "sphinx", "types-docutils", "bs4", "nox"]
    session.install("dev", *deps)
    session.run("mypy")
