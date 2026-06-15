"""Test package artifacts contain theme files."""

# ruff: noqa: S603

import shutil
import subprocess
import tarfile
import zipfile
from pathlib import Path

import pytest

REQUIRED_WHEEL_FILES = {
    "sphinxawesome_theme/__init__.py",
    "sphinxawesome_theme/theme.conf",
    "sphinxawesome_theme/theme.toml",
    "sphinxawesome_theme/layout.html",
    "sphinxawesome_theme/static/theme.css",
    "sphinxawesome_theme/static/theme.js",
}

REQUIRED_SDIST_FILES = {
    "src/sphinxawesome_theme/__init__.py",
    "src/sphinxawesome_theme/theme.conf",
    "src/sphinxawesome_theme/theme.toml",
    "src/sphinxawesome_theme/layout.html",
    "src/sphinxawesome_theme/static/theme.css",
    "src/sphinxawesome_theme/static/theme.js",
}


def test_build_artifacts_include_theme_files(tmp_path: Path) -> None:
    """Build sdist/wheel and ensure theme package files are included."""
    uv = shutil.which("uv")
    if uv is None:
        pytest.skip("uv is required to build package artifacts")

    subprocess.run(
        [uv, "build", "--out-dir", str(tmp_path)],
        check=True,
        cwd=Path(__file__).parents[1],
    )

    wheels = list(tmp_path.glob("*.whl"))
    sdists = list(tmp_path.glob("*.tar.gz"))
    assert len(wheels) == 1
    assert len(sdists) == 1

    with zipfile.ZipFile(wheels[0]) as wheel:
        wheel_names = set(wheel.namelist())
    assert not REQUIRED_WHEEL_FILES - wheel_names

    with tarfile.open(sdists[0]) as sdist:
        sdist_names = {Path(name).as_posix() for name in sdist.getnames()}
    sdist_without_root = {"/".join(Path(name).parts[1:]) for name in sdist_names}
    assert not REQUIRED_SDIST_FILES - sdist_without_root
