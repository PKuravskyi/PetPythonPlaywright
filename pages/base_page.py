from playwright.sync_api import Locator


class BasePage:
    def __init__(self, page):
        self._page = page
        self._BASE_URL = 'http://localhost:2221'

        self._basket_counter_text_field: Locator = page.locator('[data-qa="header-basket-count"]')

    def _navigate_to(self, url):
        self._page.goto(url)

    def _type(self, locator: Locator, text: str):
        locator.fill(text)
        return self

    def get_basket_items_locator(self) -> Locator:
        return self._basket_counter_text_field

