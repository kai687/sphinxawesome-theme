"""A module for demonstrating how styles for docs produced by sphinx-autoapi look like."""

from __future__ import annotations


def prompt(message: str, default: str | None = None) -> str | None:
    """Prompt the user for a value.

    Parameters
    ----------
    message: str
        The message to prompt the user with.
    default: str | None
        The default value, by default None.

    Returns:
    --------
    str | None
        The value entered by the user or the default value,
        if the user didn't enter anything.
    """
    text = f"{message} [{default}]" if default else message
    return input(text).strip() or default


def add(a: int, b: int) -> int:
    """Returns the sum of two numbers.

    Parameters
    ----------
    a: int
        The first number.
    b: int
        The second number.

    Returns:
    --------
    int
        The sum of a and b.
    """
    return a + b
