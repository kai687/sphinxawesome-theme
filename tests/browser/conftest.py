"""Fixtures for browser tests.

These tests need the optional `browser` dependency group and a Chromium
install (`playwright install chromium`). Without them they are skipped.
Set `CHROMIUM_PATH` to use an existing Chromium binary instead.
"""

import functools
import http.server
import os
import threading
from collections.abc import Iterator
from pathlib import Path
from typing import Any

import pytest
from sphinx.application import Sphinx

sync_api = pytest.importorskip("playwright.sync_api")

ROOT = Path(__file__).parent.parent / "roots" / "test-nav"
NAV_LINKS = {"Docs": "/index", "About": "/about", "A": "/a"}


class _QuietHandler(http.server.SimpleHTTPRequestHandler):
    """Static file handler that doesn't log requests."""

    def log_message(self, format: str, *args: Any) -> None:  # noqa: A002
        """Silence request logging."""


@pytest.fixture(scope="session")
def site(tmp_path_factory: pytest.TempPathFactory) -> Iterator[str]:
    """Build the `test-nav` project and serve it over HTTP."""
    base = tmp_path_factory.mktemp("browser-site")
    outdir = base / "html"
    app = Sphinx(
        srcdir=str(ROOT),
        confdir=str(ROOT),
        outdir=str(outdir),
        doctreedir=str(base / "doctrees"),
        buildername="html",
        confoverrides={
            "html_theme": "sphinxawesome_theme",
            "html_theme_options": {"main_nav_links": NAV_LINKS, "show_scrolltop": True, "awesome_headerlinks": True},
        },
        freshenv=True,
        status=None,
        warning=None,
    )
    app.build()

    handler = functools.partial(_QuietHandler, directory=str(outdir))
    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    yield f"http://127.0.0.1:{server.server_address[1]}"
    server.shutdown()


@pytest.fixture(scope="session")
def browser() -> Iterator[Any]:
    """Launch Chromium once per session, or skip if it isn't available."""
    with sync_api.sync_playwright() as pw:
        try:
            instance = pw.chromium.launch(executable_path=os.environ.get("CHROMIUM_PATH") or None)
        except sync_api.Error as exc:
            pytest.skip(f"Chromium not available: {str(exc).splitlines()[0]}")
        yield instance
        instance.close()
