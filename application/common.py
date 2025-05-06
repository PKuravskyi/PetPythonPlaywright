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


@dataclass
class CommonEndpoints:
    """
    Base dataclass meant to be extended by specific applications to define their endpoints.

    Example usage:
        @dataclass
        class MyAppEndpoints(CommonEndpoints):
            sign_up_endpoint: SignUpEndpoint
    """

    ...


# Generic type variables used for type-safe operations
CommonPagesT = TypeVar("CommonPagesT", bound=CommonPages)
CommonEndpointsT = TypeVar("CommonEndpointsT", bound=CommonEndpoints)
