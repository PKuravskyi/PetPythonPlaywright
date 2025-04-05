from playwright.sync_api import Locator

from pages.base_page import BasePage


class ArtsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.__URL = self._BASE_URL

        self.__products_cards: Locator = page.locator('[data-qa="product-card"]')

    def open(self) -> 'ArtsPage':
        super()._navigate_to(self.__URL)
        return self

    def get_product_cards(self):
        return self.__products_cards
