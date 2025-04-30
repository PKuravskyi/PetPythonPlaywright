from abc import ABC
from typing import TypeVar

from playwright.sync_api import Locator, Page


class BasePage(ABC):
    """
    Base class for all pages in the application.

    Provides common functionality like navigation and interacting with form fields.
    """

    def __init__(self, page: Page) -> None:
        """
        Initialize the BasePage with Playwright's Page object.

        Args:
            page (Page): Playwright page instance.
        """
        super().__init__()
        self._page: Page = page
        self._basket_counter_text_field: Locator = page.locator('[data-qa="header-basket-count"]')

    def _navigate_to(self, url: str) -> 'BasePage':
        """
        Navigate to the given URL.

        Args:
            url (str): The URL to navigate to.

        Returns:
            BasePage: Returns an instance of the current page after navigation.
        """
        self._page.goto(url)
        return self

    def _type(self, locator: Locator, text: str) -> 'BasePage':
        """
        Fill a text input field with the given text.

        Args:
            locator (Locator): The locator for the input field.
            text (str): The text to fill the input field with.

        Returns:
            BasePage: Returns an instance of the current page after interacting with the input field.
        """
        locator.fill(text)
        return self

    def get_basket_items_locator(self) -> Locator:
        """
        Returns:
            Locator: Playwright Locator for the basket counter element.
        """
        return self._basket_counter_text_field


BasePageT = TypeVar("BasePageT", bound=BasePage)
