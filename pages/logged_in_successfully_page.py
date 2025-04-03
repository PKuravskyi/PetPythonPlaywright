from playwright.sync_api import Locator

from pages.base_page import BasePage


class LoggedInSuccessfullyPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page

        self.URL = 'https://practicetestautomation.com/logged-in-successfully/'

        self.title_label: Locator = page.get_by_role("heading", name="Logged In Successfully")
        self.logout_button: Locator = page.get_by_role("link", name="Log out")

    def get_title_label(self):
        return self.title_label

    def get_logout_button(self):
        return self.logout_button

    def click_on_logout(self):
        self.logout_button.click()
