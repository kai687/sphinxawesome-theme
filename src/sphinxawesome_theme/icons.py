"""Provide a central location for icons used in python code."""

from bs4 import BeautifulSoup

# icons are from Material Design icon set
ICONS = {
    # https://material.io/resources/icons/?icon=open_in_new
    "external_link": (
        '<svg xmlns="http://www.w3.org/2000/svg" '
        'height="0.875rem" '
        'viewBox="0 0 24 24" class="external-link-icon" aria-hidden="true">'
        '<path d="M19 19H5V5h7V3H5a2 2 0 00-2 2v14a2 2 0 '
        "002 2h14c1.1 0 2-.9 2-2v-7h-2v7zM14 "
        '3v2h3.59l-9.83 9.83 1.41 1.41L19 6.41V10h2V3h-7z"/></svg>'
    ),
    # https://material.io/resources/icons/?icon=expand_more
    "expand_more": (
        '<svg xmlns="http://www.w3.org/2000/svg" '
        'pointer-events="none" aria-hidden="true" viewBox="0 0 24 24">'
        '<path d="M16.59 8.59L12 13.17 7.41 8.59 6 10l6 6 6-6z"/></svg>'
    ),
    # https://material.io/resources/icons/?icon=chevron_right
    "chevron_right": (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">'
        '<path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/></svg>'
    ),
}


def html(icon: str) -> BeautifulSoup:
    """Return the icon as HTML tag."""
    return BeautifulSoup(icon, "html.parser")
