"""
basket_page.py

Defines the BasketPage class for interacting with the basket page.
"""

import logging

from playwright.sync_api import Locator, Page

from pages.abstracts.base_page import BasePage
from utils.constants import BASE_URL


class BasketPage(BasePage):
    """
    Page object for the "Basket" page.
    """

    def __init__(self, page: Page, logger: logging.Logger):
        """
        Initialize the BasketPage with a Playwright Page instance.

        Args:
            page (Page): The current browser page instance.
            logger (logging.Logger): Logger instance.
        """
        super().__init__(page, logger)
        self.__endpoint: str = f"{BASE_URL}/basket"

        self.continue_to_checkout_button: Locator = page.get_by_test_id(
            "continue-to-checkout"
        )

    @property
    def endpoint(self) -> str:
        """Return the endpoint URL for the Basket page."""
        return self.__endpoint
