"""Nox sessions."""

import tempfile
from typing import Any

import nox
from nox.sessions import Session

nox.options.sessions = ["docs"]

python_files = ["src/sphinxawesome_theme/__init__.py", "noxfile.py", "docs/conf.py"]
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


@nox.session(python="3.8")
def docs(session: Session) -> None:
    """Build the docs."""
    args = session.posargs or ["-aWTE", "docs", "docs/public"]
    session.run("poetry", "install", "--no-dev", external=True)
    session.run("sphinx-build", *args)


@nox.session(python="3.7")
def export_requirements(session: Session) -> None:
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
