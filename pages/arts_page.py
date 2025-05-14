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
        self.__endpoint: str = BASE_URL
        self.sort_dropdown: Locator = page.get_by_test_id("sort-dropdown")
        self.products_cards: Locator = page.locator('[data-qa="product-card"]')
        self.products_prices: Locator = page.locator('[datatype="product-price"]')

    @property
    def endpoint(self) -> str:
        """Return the endpoint URL for the Arts page."""
        return self.__endpoint

    @allure.step("Sort arts by '{sort_option}'")
    def sort_arts_by(self, sort_option) -> "ArtsPage":
        """
        Select a sort option from the dropdown to reorder the product list.

        Args:
            sort_option (str): The value of the sort option (e.g., 'price-asc', 'price-desc').

        Returns:
            ArtsPage: The current page object for method chaining.
        """
        self.sort_dropdown.select_option(sort_option)
        return self

    @allure.step("Add '{art_name}' art to basket")
    def add_art_to_basket(self, art_name: str) -> "ArtsPage":
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
    def remove_art_from_basket(self, art_name: str) -> "ArtsPage":
        """
        Remove a specific art item from the basket by name.

        Args:
            art_name (str): The name of the art item.

        Returns:
            ArtsPage: The current page object for method chaining.
        """
        self._page.locator(f'//*[text()="{art_name}"]/..//button').click()
        return self
