"""
base_page.py

Defines the BasePage class which serves as the foundation for all page objects.

Provides common actions such as navigation, form input handling, and locating shared elements.
"""

import logging
from abc import ABC, abstractmethod
from typing import TypeVar

import allure
from playwright.sync_api import Locator, Page


class BasePage(ABC):
    """
    Base class for all pages in the application.

    Provides shared functionality for navigation and form interaction,
    and holds commonly used locators.
    """

    def __init__(self, page: Page, logger: logging.Logger) -> None:
        """
        Initialize the BasePage with a Playwright Page instance.

        Args:
            page (Page): Playwright page object for browser interaction.
            logger (logging.Logger): Logger instance used across pages.
        """
        super().__init__()
        self.page: Page = page

        self.log = logger
        self.basket_counter_text_field: Locator = page.locator(
            '[data-qa="header-basket-count"]'
        )

    @property
    @abstractmethod
    def endpoint(self) -> str:
        """
        The URL endpoint for the specific page.

        This property should be overridden by each page class to return
        its own target URL for navigation.

        Returns:
            str: The full URL to navigate to this page.
        """
        ...

    def open(self: "BasePageT") -> "BasePageT":
        """
        Navigate to a specific URL using the Playwright page.

        Returns:
            BasePage: The current page object after navigation.
        """
        with allure.step(f"Open {self.endpoint} page"):
            self.page.goto(str(self.endpoint))
            self.log.debug(f"Opened {self.endpoint} page")
        return self


# Generic type variable used for type-safe operations on classes that extend BasePage
BasePageT = TypeVar("BasePageT", bound=BasePage)
