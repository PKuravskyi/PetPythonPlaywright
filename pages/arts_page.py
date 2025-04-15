import allure
from playwright.sync_api import Locator

from pages.base_page import BasePage
from utils.constants import BASE_URL


class ArtsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.__url = BASE_URL

        self.__products_cards: Locator = page.locator('[data-qa="product-card"]')

    @allure.step('Open Arts page')
    def open(self) -> 'ArtsPage':
        super()._navigate_to(self.__url)
        return self

    def get_product_cards(self):
        return self.__products_cards

    @allure.step("Add '{art_name}' art to basket")
    def add_art_to_basket(self, art_name: str):
        self._page.locator(f'//*[text()="{art_name}"]/..//button').click()

    @allure.step("Remove '{art_name}' art from basket")
    def remove_art_from_basket(self, art_name: str):
        self._page.locator(f'//*[text()="{art_name}"]/..//button').click()
