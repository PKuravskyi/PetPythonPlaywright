"""
signup_page.py

Defines the SignUpPage class for interacting with the signup page.
"""

import time

import allure
from playwright.sync_api import Locator, Page

from pages.abstracts.base_page import BasePage
from pages.arts_page import ArtsPage
from utils.constants import BASE_URL


class SignUpPage(BasePage):
    """
    Page object for the "Sign Up" page.
    """

    def __init__(self, page: Page):
        """
        Initialize the SignUpPage with a Playwright Page instance.

        Args:
            page (Page): The current browser page instance.
        """
        super().__init__(page)
        self.__url: str = f'{BASE_URL}/signup'

        self.__email_input: Locator = page.get_by_role('textbox', name='E-Mail')
        self.__password_input: Locator = page.get_by_role('textbox', name='Password')
        self.__register_button: Locator = page.get_by_role('button', name='Register')

    @allure.step('Open Signup page')
    def open(self) -> 'SignUpPage':
        """
        Navigate to the "Sign Up" page.

        Returns:
            SignUpPage: The current page object for method chaining.
        """
        super()._navigate_to(self.__url)
        return self

    @allure.step('Enter random email')
    def enter_random_email(self) -> 'SignUpPage':
        """
        Fill in the email field with a randomly generated email address.

        Returns:
            SignUpPage: The current page object for method chaining.
        """
        username = f'{int(time.time())}@gmail.com'
        super()._type(self.__email_input, username)
        return self

    @allure.step('Enter random password')
    def enter_random_password(self) -> 'SignUpPage':
        """
        Fill in the password field with a randomly generated password.

        Returns:
            SignUpPage: The current page object for method chaining.
        """
        password = str(int(time.time()))
        super()._type(self.__password_input, password)
        return self

    @allure.step('Click on Register')
    def click_on_register(self) -> ArtsPage:
        """
        Click the Register button and wait for redirect to ArtsPage.

        Returns:
            ArtsPage: New instance of ArtsPage after successful registration.
        """
        self.__register_button.click()
        self._page.wait_for_url(BASE_URL)
        return ArtsPage(self._page)
