"""Characterize UI interactions: nav, drawer, scroll-to-top, shortcuts, copy buttons.

These tests describe behavior, not implementation, so they must pass
regardless of the JavaScript library behind them.
"""

import re
from collections.abc import Iterator
from typing import Any

import pytest
from playwright.sync_api import expect

SIDEBAR = "#left-sidebar"
OVERLAY = "body > div.fixed.inset-0"
MENU_BUTTON = 'button:has-text("Toggle navigation menu")'
DESKTOP = {"width": 1200, "height": 800}
MOBILE = {"width": 390, "height": 800}


@pytest.fixture
def new_page(browser: Any, site: str) -> Iterator[Any]:
    """Return a factory for pages that fail the test on JavaScript errors."""
    contexts: list[Any] = []
    errors: list[str] = []

    def factory(path: str, **context_options: Any) -> Any:
        context = browser.new_context(**context_options)
        contexts.append(context)
        page = context.new_page()
        page.on("pageerror", lambda exc: errors.append(str(exc)))
        page.on(
            "console",
            lambda msg: (
                errors.append(msg.text) if msg.type == "error" and "Failed to load resource" not in msg.text else None
            ),
        )
        page.goto(f"{site}/{path}")
        return page

    yield factory
    for context in contexts:
        context.close()
    assert not errors, f"JavaScript errors: {errors}"


def open_drawer(page: Any) -> None:
    """Open the mobile drawer through the menu button."""
    page.evaluate("document.activeElement.blur()")
    page.click(MENU_BUTTON)
    page.wait_for_function(f"!document.querySelector('{SIDEBAR}').inert")


def sidebar_inert(page: Any) -> bool:
    """Whether the sidebar is inert."""
    return bool(page.evaluate(f"document.querySelector('{SIDEBAR}').inert"))


def body_scroll_locked(page: Any) -> bool:
    """Whether the page body can't scroll."""
    return bool(page.evaluate("getComputedStyle(document.body).overflow === 'hidden'"))


# Collapsible navigation


def test_nav_collapsed_by_default(new_page: Any) -> None:
    """Children of a page that isn't current stay hidden."""
    page = new_page("index.html", viewport=DESKTOP)
    expect(page.locator(f'{SIDEBAR} a[href="child.html"]')).to_be_hidden()


def test_nav_current_branch_expanded(new_page: Any) -> None:
    """Children of the current page are visible on load."""
    page = new_page("parent.html", viewport=DESKTOP)
    expect(page.locator(f'{SIDEBAR} a[href="child.html"]')).to_be_visible()


def test_nav_chevron_toggles_without_navigating(new_page: Any) -> None:
    """The chevron button expands and collapses the branch and stays on the page."""
    page = new_page("index.html", viewport=DESKTOP)
    child = page.locator(f'{SIDEBAR} a[href="child.html"]')
    chevron = page.locator(f'{SIDEBAR} a[href="parent.html"] > button')

    chevron.click()
    expect(child).to_be_visible()
    expect(page.locator(f'{SIDEBAR} a[href="parent.html"]')).to_have_class(re.compile(r"\bexpanded\b"))
    assert page.url.endswith("/index.html")

    chevron.click()
    expect(child).to_be_hidden()
    expect(page.locator(f'{SIDEBAR} a[href="parent.html"]')).not_to_have_class(re.compile(r"\bexpanded\b"))
    assert page.url.endswith("/index.html")


def test_nav_link_click_navigates(new_page: Any) -> None:
    """Clicking the link itself follows it, and the target shows its children."""
    page = new_page("index.html", viewport=DESKTOP)
    page.click(f'{SIDEBAR} a[href="parent.html"] >> text=Parent')
    page.wait_for_url("**/parent.html")
    expect(page.locator(f'{SIDEBAR} a[href="child.html"]')).to_be_visible()


# Mobile drawer


def test_drawer_overlay_click_closes(new_page: Any) -> None:
    """Clicking outside the open drawer closes it."""
    page = new_page("index.html", viewport=MOBILE)
    expect(page.locator(OVERLAY)).to_be_hidden()
    open_drawer(page)
    expect(page.locator(OVERLAY)).to_be_visible()

    page.mouse.click(375, 400)
    page.wait_for_function(f"document.querySelector('{SIDEBAR}').inert")
    expect(page.locator(OVERLAY)).to_be_hidden()


def test_drawer_close_button(new_page: Any) -> None:
    """The close button inside the drawer closes it."""
    page = new_page("index.html", viewport=MOBILE)
    open_drawer(page)
    page.click(f"{SIDEBAR} > button")
    page.wait_for_function(f"document.querySelector('{SIDEBAR}').inert")


def test_drawer_locks_body_scroll(new_page: Any) -> None:
    """The page behind the open drawer can't scroll."""
    page = new_page("index.html", viewport=MOBILE)
    assert not body_scroll_locked(page)
    open_drawer(page)
    assert body_scroll_locked(page)
    page.keyboard.press("Escape")
    page.wait_for_function("getComputedStyle(document.body).overflow !== 'hidden'")


def test_drawer_state_reset_when_resizing_to_desktop(new_page: Any) -> None:
    """Growing the viewport closes the drawer and makes the sidebar usable."""
    page = new_page("index.html", viewport=MOBILE)
    open_drawer(page)

    page.set_viewport_size(DESKTOP)
    page.wait_for_function(f"!document.querySelector('{SIDEBAR}').inert")
    expect(page.locator(OVERLAY)).to_be_hidden()
    page.wait_for_function("getComputedStyle(document.body).overflow !== 'hidden'")

    # Shrinking again must not reopen it.
    page.set_viewport_size(MOBILE)
    page.wait_for_function(f"document.querySelector('{SIDEBAR}').inert")
    expect(page.locator(OVERLAY)).to_be_hidden()


def test_drawer_aria_hidden_follows_state(new_page: Any) -> None:
    """The closed drawer is hidden from assistive technology."""
    page = new_page("index.html", viewport=MOBILE)
    assert page.get_attribute(SIDEBAR, "aria-hidden") == "true"
    open_drawer(page)
    assert page.get_attribute(SIDEBAR, "aria-hidden") != "true"


def focus_in(page: Any, selector: str) -> bool:
    """Whether the focused element is inside the element matching `selector`."""
    return bool(page.evaluate(f"document.querySelector('{selector}').contains(document.activeElement)"))


def test_drawer_traps_focus(new_page: Any) -> None:
    """With the drawer open, Tab never reaches the page behind it."""
    page = new_page("index.html", viewport=MOBILE)
    open_drawer(page)
    assert focus_in(page, SIDEBAR), "focus should move into the drawer"
    for _ in range(12):
        page.keyboard.press("Tab")
        # Focus may leave the document for the browser UI, but never lands in the page.
        assert page.evaluate("document.activeElement === document.body") or focus_in(page, SIDEBAR)
    for _ in range(12):
        page.keyboard.press("Shift+Tab")
        assert page.evaluate("document.activeElement === document.body") or focus_in(page, SIDEBAR)


def test_drawer_returns_focus_on_close(new_page: Any) -> None:
    """Closing the drawer puts focus back on the menu button, and the page is usable again."""
    page = new_page("index.html", viewport=MOBILE)
    open_drawer(page)
    page.keyboard.press("Escape")
    page.wait_for_function(f"document.querySelector('{SIDEBAR}').inert")
    assert page.evaluate("document.activeElement.textContent.includes('Toggle navigation menu')")
    assert not page.evaluate("document.querySelector('main').closest('[inert]')")
    assert not page.evaluate("document.querySelector('header').closest('[inert]')")


def test_sidebar_links_reachable_by_keyboard_on_desktop(new_page: Any) -> None:
    """Tab visits the sidebar's links on desktop."""
    page = new_page("index.html", viewport=DESKTOP)
    visited = set()
    for _ in range(25):
        page.keyboard.press("Tab")
        if focus_in(page, SIDEBAR):
            visited.add(page.evaluate("document.activeElement.getAttribute('href')"))
    assert {"about.html", "a.html", "long.html", "parent.html"} <= visited


# Scroll to top


def test_scrolltop_button_follows_scroll(new_page: Any) -> None:
    """The button appears after scrolling down and returns to the top."""
    page = new_page("long.html", viewport=DESKTOP)
    page.wait_for_selector("#scrolltop", state="hidden")

    page.evaluate("window.scrollTo(0, 1000)")
    page.wait_for_selector("#scrolltop", state="visible")

    page.click("#scrolltop")
    page.wait_for_function("window.scrollY === 0")
    page.wait_for_selector("#scrolltop", state="hidden")


# Keyboard shortcut


def test_cmd_k_focuses_search(new_page: Any) -> None:
    """Cmd+K moves focus to the search field."""
    page = new_page("index.html", viewport=DESKTOP)
    page.evaluate("document.activeElement.blur()")
    page.keyboard.press("Meta+k")
    assert page.evaluate("document.activeElement.id") == "search-input"


def test_ctrl_k_focuses_search(new_page: Any) -> None:
    """Ctrl+K moves focus to the search field."""
    page = new_page("index.html", viewport=DESKTOP)
    page.evaluate("document.activeElement.blur()")
    page.keyboard.press("Control+k")
    assert page.evaluate("document.activeElement.id") == "search-input"


# Theme


def test_os_scheme_change_updates_theme(new_page: Any) -> None:
    """A live OS color scheme change is applied."""
    page = new_page("index.html", color_scheme="light")
    assert not page.evaluate("document.documentElement.classList.contains('dark')")
    page.emulate_media(color_scheme="dark")
    page.wait_for_function("document.documentElement.classList.contains('dark')")


# Copy buttons


def test_headerlink_copies_url(new_page: Any) -> None:
    """Clicking a heading permalink copies its URL and shows a tooltip."""
    page = new_page("long.html", viewport=DESKTOP)
    page.context.grant_permissions(["clipboard-read", "clipboard-write"])
    link = page.locator("#first-section a.headerlink")

    link.click(force=True)
    page.wait_for_function("document.querySelector('#first-section a.headerlink').dataset.tooltip === 'Copied!'")
    assert page.evaluate("navigator.clipboard.readText()").endswith("/long.html#first-section")
    assert page.url.endswith("/long.html")  # the click doesn't scroll or navigate

    page.wait_for_function(
        "document.querySelector('#first-section a.headerlink').dataset.tooltip === 'Copy link to this element'",
        timeout=5000,
    )


def test_code_copy_button(new_page: Any) -> None:
    """The copy button copies the code and confirms."""
    page = new_page("child.html", viewport=DESKTOP)
    page.context.grant_permissions(["clipboard-read", "clipboard-write"])
    button = page.locator("button.copy")
    button.click(force=True)
    page.wait_for_function("document.querySelector('button.copy').dataset.tooltip === 'Copied!'")
    assert page.evaluate("navigator.clipboard.readText()").strip() == 'print("copy me")'
