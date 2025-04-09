from playwright.sync_api import Locator

from pages.base_page import BasePage


class ArtsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.__URL = self._BASE_URL

        self.__products_cards: Locator = page.locator('[data-qa="product-card"]')
        self.__sort_dropdown = page.locator('.sort-dropdown')
        self.__arts_price_text_fields = page.locator('.product-price')

    def open(self) -> 'ArtsPage':
        super()._navigate_to(self.__URL)
        return self

    def get_product_cards(self):
        return self.__products_cards

    def add_art_to_basket(self, art_name: str):
        self._page.locator(f'//*[text()="{art_name}"]/..//button').click()

    remove_art_from_basket = add_art_to_basket
