"""Common configurations and fixtures for Pytest."""

from pathlib import Path

from _pytest.config import Config
import pytest
from sphinx.testing.path import path

pytest_plugins = "sphinx.testing.fixtures"


@pytest.fixture(scope="session")
def rootdir() -> Path:
    """Root directory for test files."""
    return path(__file__).parent.abspath()


def pytest_configure(config: Config) -> None:
    """Register `sphinx` marker with pytest."""
    config.addinivalue_line("markers", "sphinx")
