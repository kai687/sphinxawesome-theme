"""Provide a central location for icons used in python code."""

from bs4 import BeautifulSoup

# icons are from Material Design icon set
ICONS = {
    # https://material.io/resources/icons/?icon=content_copy
    "copy": (
        "<svg xmlns='http://www.w3.org/2000/xvg' viewBox='0 0 24 24' "
        "aria-hidden='true'>"
        "<path d='M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 "
        "4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 "
        "0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z' /></svg>"
    ),
    # https://material.io/resources/icons/?icon=link
    "headerlink": (
        '<svg xmlns="http://www.w3.org/2000/svg" '
        'pointer-events="none" viewBox="0 0 24 24">'
        '<path d="M3.9 12c0-1.71 1.39-3.1 '
        "3.1-3.1h4V7H7c-2.76 0-5 2.24-5 5s2.24 "
        "5 5 5h4v-1.9H7c-1.71 0-3.1-1.39-3.1-3.1zM8 "
        "13h8v-2H8v2zm9-6h-4v1.9h4c1.71 0 3.1 1.39 3.1 "
        "3.1s-1.39 3.1-3.1 3.1h-4V17h4c2.76 0 5-2.24 "
        '5-5s-2.24-5-5-5z"/></svg>'
    ),
    # https://material.io/resources/icons/?icon=open_in_new
    "external_link": (
        '<svg xmlns="http://www.w3.org/2000/svg" '
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
        '<svg xmlns="http://www.w3.org/2000/svg" '
        'viewBox="0 0 24 24" class="expand" aria-hidden="true">'
        '<path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/></svg>'
    ),
}


def html(icon: str) -> BeautifulSoup:
    """Return the icon as HTML tag."""
    return BeautifulSoup(icon, "html.parser")
