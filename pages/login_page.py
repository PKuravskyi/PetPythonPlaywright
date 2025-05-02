"""
login_page.py

Defines the LoginPage class for interacting with the login screen.
"""

import allure
from playwright.sync_api import Locator, Page

from pages.abstracts.base_page import BasePage
from pages.arts_page import ArtsPage
from utils.constants import BASE_URL


class LoginPage(BasePage):
    """
    Page object for the login page of the application.
    """

    def __init__(self, page: Page):
        """
        Initialize the LoginPage with a Playwright Page instance.

        Args:
            page (Page): The current browser page instance.
        """
        super().__init__(page)
        self.__url: str = f'{BASE_URL}/login'

        self.__email_input: Locator = page.get_by_role('textbox', name='E-Mail')
        self.__password_input: Locator = page.get_by_role('textbox', name='Password')
        self.__login_button: Locator = page.get_by_role('button', name='Login')

    @allure.step('Open Login page')
    def open(self) -> 'LoginPage':
        """
        Navigate to the login page.

        Returns:
            LoginPage: The current page object for method chaining.
        """
        super()._navigate_to(self.__url)
        return self

    @allure.step("Enter '{value}' email")
    def enter_email(self, value: str) -> 'LoginPage':
        """
        Fill in the email input field.

        Args:
            value (str): Email address to enter.

        Returns:
            LoginPage: The current page object for method chaining.
        """
        super()._type(self.__email_input, value)
        return self

    @allure.step("Enter '{value}' password")
    def enter_password(self, value: str) -> 'LoginPage':
        """
        Fill in the password input field.

        Args:
            value (str): Password to enter.

        Returns:
            LoginPage: The current page object for method chaining.
        """
        super()._type(self.__password_input, value)
        return self

    @allure.step('Click on Login')
    def click_on_login(self) -> ArtsPage:
        """
        Click the login button and wait for redirect to the ArtsPage.

        Returns:
            ArtsPage: An instance of the ArtsPage after login is successful.
        """
        self.__login_button.click()
        self._page.wait_for_url(BASE_URL)
        return ArtsPage(self._page)
