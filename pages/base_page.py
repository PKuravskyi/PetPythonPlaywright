from playwright.sync_api import Locator


class BasePage:
    def __init__(self, page):
        self._page = page
        self._BASE_URL = 'http://localhost:2221'

    def _navigate_to(self, url):
        self._page.goto(url)

    def _type(self, locator: Locator, text: str):
        locator.fill(text)
        return self

