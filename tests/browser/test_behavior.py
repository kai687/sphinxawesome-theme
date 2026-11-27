"""Check theme behavior in a real browser: theme switching and the mobile drawer."""

from typing import Any

import pytest

TOGGLE = 'button[aria-label="Toggle color scheme"]'
SIDEBAR = "#left-sidebar"


def is_dark(page: Any) -> bool:
    """Whether the `dark` class is set on the root element."""
    return bool(page.evaluate("document.documentElement.classList.contains('dark')"))


@pytest.mark.parametrize("os_scheme", ["dark", "light"])
def test_toggle_choice_survives_reload(browser: Any, site: str, os_scheme: str) -> None:
    """A user's choice wins over the OS preference, including after a reload."""
    context = browser.new_context(color_scheme=os_scheme)
    page = context.new_page()
    page.goto(f"{site}/index.html")
    assert is_dark(page) == (os_scheme == "dark")

    page.click(TOGGLE)
    flipped = os_scheme != "dark"
    assert is_dark(page) == flipped
    assert page.get_attribute(TOGGLE, "aria-pressed") == str(flipped).lower()

    page.reload()
    assert is_dark(page) == flipped
    context.close()


def test_stored_choice_applied_before_scripts_load(browser: Any, site: str) -> None:
    """The inline head script sets the theme without waiting for theme.js."""
    context = browser.new_context(color_scheme="dark")
    page = context.new_page()
    page.goto(f"{site}/index.html")
    page.click(TOGGLE)  # choose light on a dark OS

    page.route("**/theme.js", lambda route: route.abort())
    page.reload()
    assert not is_dark(page)
    context.close()


def test_mobile_drawer_focus_and_escape(browser: Any, site: str) -> None:
    """The closed drawer is skipped by Tab; the open drawer closes on Escape."""
    context = browser.new_context(viewport={"width": 390, "height": 800})
    page = context.new_page()
    page.goto(f"{site}/index.html")

    for _ in range(10):
        page.keyboard.press("Tab")
        in_sidebar = page.evaluate(f"document.querySelector('{SIDEBAR}').contains(document.activeElement)")
        assert not in_sidebar, "focus reached the closed drawer"

    # The focused skip link overlaps the menu button; drop focus before clicking.
    page.evaluate("document.activeElement.blur()")
    page.click("button:has(.sr-only)")
    page.wait_for_function(f"!document.querySelector('{SIDEBAR}').inert")

    page.keyboard.press("Escape")
    page.wait_for_function(f"document.querySelector('{SIDEBAR}').inert")
    context.close()


def test_sidebar_is_interactive_on_desktop(browser: Any, site: str) -> None:
    """On desktop the sidebar is part of the page, so it must not be inert."""
    context = browser.new_context(viewport={"width": 1200, "height": 800})
    page = context.new_page()
    page.goto(f"{site}/index.html")
    assert not page.evaluate(f"document.querySelector('{SIDEBAR}').inert")
    context.close()


def active_section(page: Any) -> str:
    """The TOC link currently marked as active, or an empty string."""
    links = page.query_selector_all('#right-sidebar a[data-current="true"]')
    return links[0].get_attribute("href") if links else ""


def test_scrollspy_follows_scroll_and_reaches_last_section(browser: Any, site: str) -> None:
    """The active TOC entry follows the scroll, including the short last section."""
    context = browser.new_context(viewport={"width": 1440, "height": 800})
    page = context.new_page()
    page.goto(f"{site}/long.html")
    page.wait_for_function("window.Alpine !== undefined")

    page.evaluate("document.querySelector('#second-section').scrollIntoView()")
    page.wait_for_function("document.querySelector('#right-sidebar [data-current]')")
    assert active_section(page) == "#second-section"

    # The last sections are too short to scroll to the top of the viewport.
    page.evaluate("window.scrollTo(0, document.documentElement.scrollHeight)")
    page.wait_for_function(
        "document.querySelector('#right-sidebar a[href=\"#fourth-section\"]').dataset.current === 'true'"
    )
    assert active_section(page) == "#fourth-section"
    context.close()
