"""Nox sessions."""

import tempfile
from typing import Any

import nox
from nox.sessions import Session

nox.options.sessions = ["docs", "lint", "black", "mypy", "netlify_test"]

python_files = [
    "src/sphinxawesome_theme/__init__.py",
    "src/sphinxawesome_theme/html_translator.py",
    "noxfile.py",
    "docs/conf.py",
]
python_versions = ["3.6", "3.7", "3.8"]


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


@nox.session(python=python_versions)
def tests(session: Session) -> None:
    """Run unit tests."""
    args = session.posargs or ["--cov"]
    session.run("poetry", "install", "--no-dev", external=True)
    install_constrained_version(session, "coverage[toml]", "pytest", "pytest-cov")
    session.run("pytest", *args)


@nox.session(python=python_versions)
def docs(session: Session) -> None:
    """Build the docs."""
    args = session.posargs or ["-b", "dirhtml", "-aWTE", "docs", "docs/public"]
    session.run("poetry", "install", "--no-dev", external=True)
    session.run("sphinx-build", *args)


def serve(session: Session) -> None:
    """Serve the docs."""
    session.run("python", "-m", "http.server", "--dir", "docs/public")


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
        "--format=requirements.txt",
        "--output=requirements.txt",
        external=True,
    )


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
        "flake8-import-order",
    )
    session.run("flake8", *args)


@nox.session(python="3.8")
def black(session: Session) -> None:
    """Format python files with black."""
    args = session.posargs or python_files

    install_constrained_version(session, "black")
    session.run("black", *args)


@nox.session(python=python_versions)
def mypy(session: Session) -> None:
    """Typecheck python files with mypy."""
    args = session.posargs or python_files

    install_constrained_version(session, "mypy")
    session.run("mypy", *args)


@nox.session(python="3.8")
def vale(session: Session) -> None:
    """Run vale linter on docs directory."""
    from shutil import which

    install_constrained_version(session, "docutils")

    if which("vale") is not None:
        session.run("vale", "docs", external=True)
    else:
        session.skip("Vale executable not found. Skipping.")
