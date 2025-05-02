"""
common.py

Defines shared page-related base structures for use across different application implementations.
"""

from dataclasses import dataclass
from typing import TypeVar


@dataclass
class CommonPages:
    """
    Base dataclass meant to be extended by specific applications to define their pages.

    Example usage:
        @dataclass
        class MyAppPages(CommonPages):
            login_page: LoginPage
            home_page: HomePage
    """
    ...


# Generic type variable used for type-safe operations on classes that extend CommonPages
CommonPagesT = TypeVar("CommonPagesT", bound=CommonPages)
