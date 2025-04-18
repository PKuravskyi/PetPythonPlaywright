import allure
from playwright.sync_api import Locator, Page

from pages.base_page import BasePage
from utils.constants import BASE_URL


class ArtsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.__url: str = BASE_URL

        self.__products_cards: Locator = page.locator('[data-qa="product-card"]')

    @allure.step('Open Arts page')
    def open(self) -> 'ArtsPage':
        super()._navigate_to(self.__url)
        return self

    @allure.step("Add '{art_name}' art to basket")
    def add_art_to_basket(self, art_name: str) -> 'ArtsPage':
        self._page.locator(f'//*[text()="{art_name}"]/..//button').click()
        return self

    @allure.step("Remove '{art_name}' art from basket")
    def remove_art_from_basket(self, art_name: str) -> 'ArtsPage':
        self._page.locator(f'//*[text()="{art_name}"]/..//button').click()
        return self

    def get_product_cards(self) -> Locator:
        return self.__products_cards
