"""
base_page.py

Defines the BasePage class which serves as the foundation for all page objects.

Provides common actions such as navigation, form input handling, and locating shared elements.
"""

from abc import ABC
from typing import TypeVar

from playwright.sync_api import Locator, Page


class BasePage(ABC):
    """
    Base class for all pages in the application.

    Provides shared functionality for navigation and form interaction,
    and holds commonly used locators.
    """

    def __init__(self, page: Page) -> None:
        """
        Initialize the BasePage with a Playwright Page instance.

        Args:
            page (Page): Playwright page object for browser interaction.
        """
        super().__init__()
        self._page: Page = page
        self._basket_counter_text_field: Locator = page.locator('[data-qa="header-basket-count"]')

    def _navigate_to(self, url: str) -> 'BasePage':
        """
        Navigate to a specific URL using the Playwright page.

        Args:
            url (str): The destination URL.

        Returns:
            BasePage: The current page object after navigation.
        """
        self._page.goto(url)
        return self

    def _type(self, locator: Locator, text: str) -> 'BasePage':
        """
        Fill a text input field with the given text.

        Args:
            locator (Locator): The locator for the input element.
            text (str): Text to input into the field.

        Returns:
            BasePage: The current page object after input interaction.
        """
        locator.fill(text)
        return self

    def get_basket_items_locator(self) -> Locator:
        """
        Get the locator for the basket counter element in the header.

        Returns:
            Locator: Playwright locator pointing to the basket counter.
        """
        return self._basket_counter_text_field


# Generic type variable used for type-safe operations on classes that extend BasePage
BasePageT = TypeVar("BasePageT", bound=BasePage)
