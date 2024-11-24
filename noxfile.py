"""Run automated tasks."""

from __future__ import annotations

import nox  # type: ignore (external tool)

nox.options.stop_on_first_error = True
nox.options.sessions = ["docs", "lint", "test", "typecheck"]
nox.options.default_venv_backend = "uv"

python_versions = ["3.9", "3.13"]


def get_requirements(groups: list[str] | str | None = None) -> list[str]:
    """Load requirements from a `pyproject.toml` file."""
    pyproject = nox.project.load_toml("pyproject.toml")
    pkgs = pyproject["project"]["dependencies"]

    if groups and "dependency-groups" in pyproject:
        for g in groups if isinstance(groups, list) else [groups]:
            pkgs += pyproject["dependency-groups"].get(g, [])

    return pkgs


def install_requirements(
    session: nox.Session, groups: list[str] | str | None = None
) -> None:
    """Install requirements into the session's environment."""
    requirements = get_requirements(groups)
    session.install(*requirements)
    session.install("-e", ".")


@nox.session(python=python_versions)
def docs(session: nox.Session) -> None:
    """Build the docs.

    Args:
        session: The nox session instance.
        live: Whether to build a live-reloading version with ``sphinx-autobuild``.
        verbose: Whether to run Sphinx in verbose mode.
    """
    install_requirements(session, "docs")
    build_cmd = "sphinx-build"
    args = ["-b", "dirhtml", "-aWTE", "docs", "docs/public"]

    if "--live" in session.posargs:
        build_cmd = "sphinx-autobuild"
        args += ["-A", "mode=development"]
        session.posargs.remove("--live")

    if "--verbose" in session.posargs:
        args += ["-vvv"]
        session.posargs.remove("--verbose")

    if session.posargs:
        args += session.posargs

    session.run(build_cmd, *args)


@nox.session
def links(session: nox.Session) -> None:
    """Check for broken links."""
    args = session.posargs or ["-b", "linkcheck", "-aWTE", "docs", "docs/public/_links"]
    install_requirements(session, "docs")
    session.run("sphinx-build", *args)


@nox.session(python=python_versions)
def lint(session: nox.Session) -> None:
    """Check for common issues."""
    install_requirements(session, "dev")
    session.run("ruff", "check", ".")


@nox.session(python=python_versions)
def test(session: nox.Session) -> None:
    """Run tests."""
    args = session.posargs or ["--cov"]
    install_requirements(session, ["dev", "docs"])
    session.run("pytest", *args)


@nox.session
def fmt(session: nox.Session) -> None:
    """Format python files."""
    install_requirements(session, "dev")
    session.run("ruff", "check", ".", "--fix")
    session.run("ruff", "format", ".")


@nox.session(python=python_versions)
def typecheck(session: nox.Session) -> None:
    """Check type annotations."""
    install_requirements(session, "dev")
    session.run("pyright")


@nox.session(python=False)
def export(session: nox.Session) -> None:
    """Export dependencies for Netlify."""
    session.run(
        "uv",
        "export",
        "--no-hashes",
        "--python=3.12",
        "--group=docs",
        "--group=netlify",
        "--output-file=requirements.txt",
        external=True,
    )
