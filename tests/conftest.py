"""Common configurations and fixtures for Pytest."""

import pytest
from _pytest.config import Config
from sphinx.testing.path import path

pytest_plugins = "sphinx.testing.fixtures"
collect_ignore = ["roots"]


@pytest.fixture(scope="session")
def rootdir() -> path:
    """Root directory for test files."""
    return path(__file__).parent.abspath() / "roots"


def pytest_configure(config: Config) -> None:
    """Register `sphinx` marker with pytest."""
    config.addinivalue_line("markers", "sphinx")
