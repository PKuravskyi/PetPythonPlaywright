"""
my_account_page.py

Defines the MyAccountPage class for interacting with the user's account page.
"""
import logging

from playwright.sync_api import Locator, Page

from pages.abstracts.base_page import BasePage
from utils.constants import BASE_URL


class MyAccountPage(BasePage):
    """
    Page object for the "My Account" page.
    """

    def __init__(self, page: Page, logger: logging.Logger):
        """
        Initialize the MyAccountPage with a Playwright Page instance.

        Args:
            page (Page): The current browser page instance.
            logger (logging.Logger): Logger instance.
        """
        super().__init__(page, logger)
        self.__endpoint: str = f"{BASE_URL}/my-account"

        self.my_account_label: Locator = page.get_by_role("heading", name="My Account")
        self.your_addresses_label: Locator = page.get_by_role(
            "heading", name="Your addresses"
        )
        self.email_address_label: Locator = page.get_by_text("Email")

    @property
    def endpoint(self) -> str:
        """Return the endpoint URL for the My Account page."""
        return self.__endpoint
