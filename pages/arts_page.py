"""
arts_page.py

Contains the ArtsPage class, which represents the main product listing page.
"""

import allure
from playwright.sync_api import Locator, Page

from pages.abstracts.base_page import BasePage
from utils.constants import BASE_URL


class ArtsPage(BasePage):
    """
    Page object for the Arts page of the shopping store application.
    """

    def __init__(self, page: Page):
        """
        Initialize the ArtsPage with a Playwright Page.

        Args:
            page (Page): The current browser page instance.
        """
        super().__init__(page)
        self.__url: str = BASE_URL
        self.__products_cards: Locator = page.locator('[data-qa="product-card"]')

    @allure.step('Open Arts page')
    def open(self) -> 'ArtsPage':
        """
        Navigate to the Arts page using the base URL.

        Returns:
            ArtsPage: The current page object for method chaining.
        """
        super()._navigate_to(self.__url)
        return self

    @allure.step("Add '{art_name}' art to basket")
    def add_art_to_basket(self, art_name: str) -> 'ArtsPage':
        """
        Add a specific art item to the basket by name.

        Args:
            art_name (str): The name of the art item.

        Returns:
            ArtsPage: The current page object for method chaining.
        """
        self._page.locator(f'//*[text()="{art_name}"]/..//button').click()
        return self

    @allure.step("Remove '{art_name}' art from basket")
    def remove_art_from_basket(self, art_name: str) -> 'ArtsPage':
        """
        Remove a specific art item from the basket by name.

        Args:
            art_name (str): The name of the art item.

        Returns:
            ArtsPage: The current page object for method chaining.
        """
        self._page.locator(f'//*[text()="{art_name}"]/..//button').click()
        return self

    def get_product_cards(self) -> Locator:
        """
        Get the locator for all product cards on the page.

        Returns:
            Locator: The locator for product card elements.
        """
        return self.__products_cards
