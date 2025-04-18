from playwright.sync_api import Locator, Page


class BasePage:
    def __init__(self, page: Page):
        self._page: Page = page

        self._basket_counter_text_field: Locator = page.locator('[data-qa="header-basket-count"]')

    def _navigate_to(self, url: str) -> 'BasePage':
        self._page.goto(url)
        return self

    def _type(self, locator: Locator, text: str) -> 'BasePage':
        locator.fill(text)
        return self

    def get_basket_items_locator(self) -> Locator:
        return self._basket_counter_text_field
