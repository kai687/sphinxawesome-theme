"""Run commands for this repository."""
from __future__ import annotations

import shutil
import tempfile
from typing import Literal

import nox
from nox import Session, session

nox.options.stop_on_first_error = True
nox.options.sessions = ["docs", "lint", "fmt", "mypy", "tests"]

python_versions = ["3.11", "3.10", "3.9", "3.8"]

python_files = ["src/sphinxawesome_theme", "noxfile.py", "docs/conf.py", "tests/"]


def install_with_requirements(
    session: Session, group: Literal["dev", "docs", "lint"] = "dev", *args: str
) -> None:
    """Install a group's dependencies in the nox environment using version constraints.

    To make Nox use the version constraints as defined in the ``pyproject.toml`` file,
    we have to export the dependencies into a temporary ``requirements.txt``.

    Args:
        session: The nox session object.
        group: The dependency group to export.
        args: The packages to install, passed on to ``session.install``
    """
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            "poetry",
            "export",
            "--without-hashes",
            "--only",
            group,
            "--output",
            requirements.name,
            external=True,
        )
        session.install("-r", requirements.name, *args)


@session(python=python_versions)
def tests(session: Session) -> None:
    """Run unit tests."""
    args = session.posargs or ["--cov"]
    deps = ["coverage[toml]", "pytest", "pytest-cov", "sphinx-design"]
    install_with_requirements(session, "dev", ".", *deps)
    session.run("pytest", *args)


@session(python=python_versions)
def docs(session: Session) -> None:
    """Build the docs.

    Run ``nox -p <python> -s docs`` to build the docs the standard way.
    Run ``nox -p <python> -s docs -- --live`` to use ``sphinx-autobuild``.
    """
    args = ["-b", "dirhtml", "-aWTE", "docs", "docs/public"]
    deps = ["sphinx", "bs4", "sphinx-sitemap", "sphinx-design"]
    sphinx_build = "sphinx-build"

    if "--live" in session.posargs:
        deps.append("sphinx-autobuild")
        sphinx_build = "sphinx-autobuild"
        session.posargs.remove("--live")
        args += ["-A", "mode=development", "--watch", "src/sphinxawesome_theme"]

    if session.posargs:
        args += session.posargs

    install_with_requirements(session, "docs", ".", *deps)
    session.run(sphinx_build, *args)


@session
def linkcheck(session: Session) -> None:
    """Check links."""
    args = session.posargs or ["-b", "linkcheck", "-aWTE", "docs", "docs/public/_links"]
    deps = ["sphinx", "bs4", "sphinx-sitemap", "sphinx-design"]
    install_with_requirements(session, "docs", ".", *deps)
    session.run("sphinx-build", *args)


@session
def xml(session: Session) -> None:
    """Build XML version of the docs."""
    args = ["-b", "xml", "-aWTE", "docs", "docs/public/xml"]
    deps = ["sphinx", "bs4", "sphinx-sitemap", "sphinx-design"]
    install_with_requirements(session, "docs", ".", *deps)
    session.run("sphinx-build", *args)


@session(venv_backend=None)
def export(session: Session) -> None:
    """Export a requirements.txt file Netlify (Python 3.8)."""
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            "poetry",
            "export",
            "--with=docs,dev,lint",
            "--without-hashes",
            "--output",
            requirements.name,
            external=True,
        )
        shutil.copy(requirements.name, "requirements.txt")


@session(python=python_versions)
def lint(session: Session) -> None:
    """Lint python files."""
    deps = ["ruff", "djlint"]
    install_with_requirements(session, "lint", ".", *deps)

    session.run("ruff", ".")
    session.run("djlint", "src")


@session
def fmt(session: Session) -> None:
    """Format python files."""
    deps = ["ruff", "black", "djlint"]
    install_with_requirements(session, "lint", ".", *deps)

    session.run("ruff", "check", ".", "--select", "I", "--fix")
    session.run("black", ".")
    session.run("djlint", "src", "--reformat")


@session(python=["3.8", "3.11"])
def mypy(session: Session) -> None:
    """Typecheck python files with mypy.

    Usually, issues occur either for all versions or the earliest
    supported version, so running for these two is usually enough.
    """
    # We need to install these additional libraries or Mypy will complain
    deps = ["mypy", "pytest", "sphinx", "types-docutils", "bs4", "nox"]
    install_with_requirements(session, "dev", *deps)
    session.run("mypy")
