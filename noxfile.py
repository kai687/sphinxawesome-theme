"""Nox sessions."""

import re
import tempfile
from typing import Any

import nox
from nox.sessions import Session

nox.options.stop_on_first_error = True
nox.options.sessions = ["docs", "lint", "black", "mypy", "netlify_test", "tests"]
python_files = ["src/sphinxawesome_theme", "noxfile.py", "tests", "docs/conf.py"]
python_versions = ["3.6", "3.7", "3.8", "3.9"]


def install_constrained_version(session: Session, *args: str, **kwargs: Any) -> None:
    """Install packages with version constraints from poetry.lock."""
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            "poetry",
            "export",
            "--format=requirements.txt",
            "--without-hashes",
            "--dev",
            f"--output={requirements.name}",
            external=True,
        )
        session.install(f"--constraint={requirements.name}", *args, **kwargs)


def append_to_requirements(session: Session, *package_names: str) -> None:
    """Add additional dependency to requirements file.

    Poetry doesn't have optional development dependencies yet (potentially in 1.2).
    For building the docs, I need some depencenies that you don't need to run the
    package. I also don't want to import _all_ development dependencies on netlify.

    This function exports a temporary requirement.txt with dependencies, extracts
    matching lines and appends that to the `requirements.txt` file.

    The final `requirements.txt` file has only the `production` dependencies plus
    some extra (development) dependencies.
    """
    pattern = re.compile("|".join(package_names))

    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            "poetry",
            "export",
            "--without-hashes",
            "--dev",
            f"--output={requirements.name}",
            external=True,
        )

        with open(requirements.name) as tmpfile:
            packages = [line for line in tmpfile if pattern.search(line)]

    with open("requirements.txt", "a") as requirement_file:
        for package in packages:
            requirement_file.write(package)


@nox.session(python=python_versions)
def tests(session: Session) -> None:
    """Run unit tests."""
    args = session.posargs or ["--cov"]
    session.run("poetry", "install", "--no-dev", external=True)
    install_constrained_version(
        session, "coverage[toml]", "pytest", "pytest-cov", "pytest-randomly"
    )
    session.run("pytest", *args)


@nox.session(python=python_versions)
def docs(session: Session) -> None:
    """Build the docs."""
    args = session.posargs or ["-b", "dirhtml", "-aqWTE", "docs", "docs/public"]
    session.run("poetry", "install", "--no-dev", external=True)
    install_constrained_version(session, "myst-parser[linkify]")
    session.run("sphinx-build", *args)


@nox.session(python=python_versions[-1])
def live_docs(session: Session) -> None:
    """Build the docs and live-reload."""
    args = session.posargs or ["-b", "dirhtml", "-aWTE", "docs", "docs/public"]
    session.run("poetry", "install", "--no-dev", external=True)
    install_constrained_version(session, "myst-parser[linkify]", "sphinx-autobuild")
    session.run("sphinx-autobuild", *args)


@nox.session(python="3.9")
def linkcheck(session: Session) -> None:
    """Check links."""
    args = session.posargs or ["-b", "linkcheck", "-aWTE", "docs", "docs/public/_links"]
    session.run("poetry", "install", "--no-dev", external=True)
    install_constrained_version(session, "myst-parser[linkify]")
    session.run("sphinx-build", *args)


@nox.session(python=python_versions[-1])
def xml(session: Session) -> None:
    """Build XML version of the docs.

    This can be useful for development, to look at the structure and node types.
    """
    args = ["-b", "xml", "-aWTE", "docs", "docs/public/xml"]
    session.run("poetry", "install", external=True)
    session.run("sphinx-build", *args)


@nox.session(python="3.7")
def netlify_test(session: Session) -> None:
    """Test, if netlify can build the docs."""
    args = ["-b", "dirhtml", "-T", "-W", "docs/", "docs/public"]

    export(session)

    session.install("-r", "requirements.txt")
    session.run("sphinx-build", *args)


@nox.session(python="3.7")
def export(session: Session) -> None:
    """Export requirements from poetry.lock for Netlify.

    Netlify uses Python 3.7.
    """
    session.run(
        "poetry",
        "export",
        "--without-hashes",
        "--output=requirements.txt",
        external=True,
    )

    append_to_requirements(session, "myst-parser", "linkify-it-py")


@nox.session(python=python_versions)
def lint(session: Session) -> None:
    """Lint python files with flake8."""
    args = session.posargs or python_files

    install_constrained_version(
        session,
        "flake8",
        "flake8-annotations",
        "flake8-bandit",
        "flake8-black",
        "flake8-bugbear",
        "flake8-docstrings",
        "flake8-implicit-str-concat",
    )
    session.run("flake8", *args)


@nox.session(python="3.9")
def black(session: Session) -> None:
    """Format python files with black."""
    args = session.posargs or python_files

    install_constrained_version(session, "black")
    session.run("black", *args)


@nox.session(python="3.9")
def isort(session: Session) -> None:
    """Rearrange imports on all Python files."""
    args = session.posargs or python_files

    install_constrained_version(session, "isort")
    session.run("isort", *args)


@nox.session(python=python_versions)
def mypy(session: Session) -> None:
    """Typecheck python files with mypy."""
    args = session.posargs or ["--strict", "--no-warn-unused-ignores"]

    install_constrained_version(
        session, "mypy", "pytest", "sphinx", "types-docutils", "bs4", "nox"
    )
    session.run("mypy", *args)
