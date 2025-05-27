"""
thank_you_page.py

Defines the ThankYouPage class for interacting with the payment screen.
"""

import logging

from playwright.sync_api import Locator, Page

from pages.abstracts.base_page import BasePage
from utils.constants import BASE_URL


class ThankYouPage(BasePage):
    """
    Page object for the Thank-you page of the application.
    """

    def __init__(self, page: Page, logger: logging.Logger):
        """
        Initialize the ThankYouPage with a Playwright Page instance.

        Args:
            page (Page): The current browser page instance.
            logger (logging.Logger): Logger instance.
        """
        super().__init__(page, logger)
        self.__endpoint: str = f"{BASE_URL}/thank-you"

        self.back_to_shop_button: Locator = page.get_by_role(
            "button", name="Back to shop"
        )

    @property
    def endpoint(self) -> str:
        """Return the endpoint URL for the Thank-you page."""
        return self.__endpoint
