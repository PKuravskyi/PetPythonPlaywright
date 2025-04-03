from playwright.sync_api import Locator


class BasePage:
    def __init__(self, page):
        self.header2_label: Locator = page.locator('h2')

    def retrieve_header(self):
        return self.header2_label
