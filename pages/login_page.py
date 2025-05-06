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
        self.__endpoint: str = f"{BASE_URL}/login"

        self.email_input: Locator = page.get_by_role("textbox", name="E-Mail")
        self.password_input: Locator = page.get_by_role("textbox", name="Password")
        self.login_button: Locator = page.get_by_role("button", name="Login")

    @property
    def endpoint(self) -> str:
        """Return the endpoint URL for the Login page."""
        return self.__endpoint

    def login(self, email: str, password: str) -> ArtsPage:
        """
        Log in to the application using the provided email and password.

        Fills in the email and password fields, submits the login form,
        and waits for the page to navigate to the Arts page.

        Args:
            email (str): The user's email address.
            password (str): The user's password.

        Returns:
            ArtsPage: The ArtsPage object.
        """
        with allure.step(f"Login user with email '{email}' and password '{password}'"):
            self.email_input.fill(email)
            self.password_input.fill(password)
            self.login_button.click()
            self._page.wait_for_url(BASE_URL)

        return ArtsPage(self._page)
