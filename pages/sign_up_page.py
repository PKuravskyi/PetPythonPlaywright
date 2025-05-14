"""
signup_page.py

Defines the SignUpPage class for interacting with the signup page.
"""
import logging
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

    def __init__(self, page: Page, logger: logging.Logger):
        """
        Initialize the SignUpPage with a Playwright Page instance.

        Args:
            page (Page): The current browser page instance.
            logger (logging.Logger): Logger instance.
        """
        super().__init__(page, logger)
        self.__endpoint: str = f"{BASE_URL}/signup"

        self.email_input: Locator = page.get_by_role("textbox", name="E-Mail")
        self.password_input: Locator = page.get_by_role("textbox", name="Password")
        self.register_button: Locator = page.get_by_role("button", name="Register")

    @property
    def endpoint(self) -> str:
        """Return the endpoint URL for the Sign-Up page."""
        return self.__endpoint

    @allure.step("Register random user")
    def register_random_user(self) -> "ArtsPage":
        """
        Fill in the email field with a randomly generated email address.

        Returns:
            SignUpPage: The current page object for method chaining.
        """
        username = f"{int(time.time())}@gmail.com"
        password = str(int(time.time()))

        self.email_input.fill(username)
        self.password_input.fill(password)
        self.register_button.click()
        self._page.wait_for_url(BASE_URL)

        self.log.debug(f"Registered user '{username}' with password '{password}'")

        return ArtsPage(self._page, self.log)
