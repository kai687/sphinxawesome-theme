"""Run commands for this repository."""
import shutil
from enum import Enum
from typing import List, Type, TypeVar

import nox
from nox_poetry import Session, session

nox.options.stop_on_first_error = True
nox.options.sessions = ["docs", "lint", "black", "mypy", "tests"]

python_files = ["src/sphinxawesome_theme", "noxfile.py", "docs/conf.py", "tests/"]

docs_dependencies = [
    "sphinx",
    "bs4",
    "sphinx-sitemap",
    "sphinx-design",
]

VersionType = TypeVar("VersionType", bound="Versions")


class Versions(Enum):
    """Python versions as `Enum`."""

    THREE_EIGHT = "3.8"
    THREE_NINE = "3.9"
    THREE_TEN = "3.10"
    THREE_ELEVEN = "3.11"

    @classmethod
    def all(cls: Type[VersionType]) -> List[str]:
        """Return the supported versions as strings."""
        return [i.value for i in cls]

    @classmethod
    def latest(cls: Type[VersionType]) -> str:
        """Return the latest supported version string."""
        versions = cls.all()
        return versions[-1]


@session(python=Versions.all())
def tests(session: Session) -> None:
    """Run unit tests."""
    args = session.posargs or ["--cov"]
    deps = ["coverage[toml]", "pytest", "pytest-cov", "sphinx-design"]
    session.install(".", *deps)
    session.run("pytest", *args)


@session(python=Versions.all())
def docs(session: Session) -> None:
    """Build the docs."""
    export(session)
    args = session.posargs or ["-b", "dirhtml", "-aWTE", "docs", "docs/public"]
    session.install(".", *docs_dependencies)
    session.run("sphinx-build", *args)


@session(python=Versions.latest())
def live_docs(session: Session) -> None:
    """Build the docs and live-reload."""
    args = session.posargs or [
        "-a",
        "-b",
        "dirhtml",
        "-A",
        "mode=development",
        "docs",
        "docs/public",
        "--watch",
        "src/sphinxawesome_theme",
        "--ignore",
        "*woff*",
        "--ignore",
        "docsearch*",
    ]
    session.install(".", "sphinx-autobuild", *docs_dependencies)
    session.run("sphinx-autobuild", *args)


@session()
def linkcheck(session: Session) -> None:
    """Check links."""
    args = session.posargs or ["-b", "linkcheck", "-aWTE", "docs", "docs/public/_links"]
    session.install(".", *docs_dependencies)
    session.run("sphinx-build", *args)


@session()
def xml(session: Session) -> None:
    """Build XML version of the docs.

    This can be useful for development, to look at the structure and node types.
    """
    args = ["-b", "xml", "-aWTE", "docs", "docs/public/xml"]
    session.install(".", *docs_dependencies)
    session.run("sphinx-build", *args)


@session(python=Versions.THREE_EIGHT.value)
def export(session: Session) -> None:
    """Export requirements from poetry.lock for Netlify.

    Netlify uses Python 3.8.
    """
    requirements = session.poetry.export_requirements()
    shutil.copy(requirements, "requirements.txt")


@session(python=Versions.all())
def lint(session: Session) -> None:
    """Lint python files with flake8."""
    if "--fix" in session.posargs:
        args = ["--fix", *python_files]
    else:
        args = session.posargs or python_files

    deps = [
        "ruff",
    ]

    session.install(".", *deps)
    session.run("ruff", *args)


@session(python=Versions.latest())
def black(session: Session) -> None:
    """Format python files with black."""
    args = session.posargs or python_files

    session.install(".", "black")
    session.run("black", *args)


@session(python=Versions.all())
def mypy(session: Session) -> None:
    """Typecheck python files with mypy."""
    args = session.posargs

    # Install these packages in the venv so that mypy can find the libs/types
    deps = [
        "mypy",
        "pytest",
        "sphinx",
        "types-docutils",
        "bs4",
        "nox",
        "nox-poetry",
    ]

    session.install(".", *deps)
    session.run("mypy", *args)
