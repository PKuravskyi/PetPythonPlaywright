from playwright.sync_api import Locator

from pages.base_page import BasePage
from utils.constants import BASE_URL


class ArtsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.__url = BASE_URL

        self.__products_cards: Locator = page.locator('[data-qa="product-card"]')

    def open(self) -> 'ArtsPage':
        super()._navigate_to(self.__url)
        return self

    def get_product_cards(self):
        return self.__products_cards

    def add_art_to_basket(self, art_name: str):
        self._page.locator(f'//*[text()="{art_name}"]/..//button').click()

    remove_art_from_basket = add_art_to_basket
