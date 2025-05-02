"""
my_account_page.py

Defines the MyAccountPage class for interacting with the user's account page.
"""

import allure
from playwright.sync_api import Locator, Page

from pages.abstracts.base_page import BasePage
from utils.constants import BASE_URL


class MyAccountPage(BasePage):
    """
    Page object for the "My Account" page.
    """

    def __init__(self, page: Page):
        """
        Initialize the MyAccountPage with a Playwright Page instance.

        Args:
            page (Page): The current browser page instance.
        """
        super().__init__(page)
        self.__url: str = f'{BASE_URL}/my-account'

        self.__my_account_label: Locator = page.get_by_role('heading', name='My Account')
        self.__your_addresses_label: Locator = page.get_by_role('heading', name='Your addresses')
        self.__email_address_label: Locator = page.get_by_text('Email')

    @allure.step('Open My Account page')
    def open(self) -> 'MyAccountPage':
        """
        Navigate to the "My Account" page.

        Returns:
            MyAccountPage: The current page object for method chaining.
        """
        super()._navigate_to(self.__url)
        return self

    def get_my_account_label(self) -> Locator:
        """
        Get the locator for the "My Account" heading.

        Returns:
            Locator: Locator for the "My Account" heading.
        """
        return self.__my_account_label

    def get_your_address_label(self) -> Locator:
        """
        Get the locator for the "Your addresses" heading.

        Returns:
            Locator: Locator for the "Your addresses" heading.
        """
        return self.__your_addresses_label

    def get_email_address_label(self) -> Locator:
        """
        Get the locator for the "Email" label.

        Returns:
            Locator: Locator for the email label.
        """
        return self.__email_address_label
