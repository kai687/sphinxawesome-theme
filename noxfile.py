"""Nox sessions."""

import tempfile
from typing import Any

import nox
from nox.sessions import Session

nox.options.sessions = ["docs"]

#  locations = ["src", "tests", "noxfile.py"]
#  python_versions = ["3.6", "3.7", "3.8"]


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
    session.run("poetry", "install", external=True)
    session.run("sphinx-build", *args)


@nox.session(python="3.7")
def export_requirements(session: Session) -> None:
    """Export requirements from poetry.lock for Netlify."""
    session.run(
        "poetry",
        "export",
        "--without-hashes",
        "--format=requirements.txt",
        "--output=requirements.txt",
        external=True,
    )
