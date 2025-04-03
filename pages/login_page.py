from playwright.sync_api import Locator

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page

        self.URL = 'https://practicetestautomation.com/practice-test-login/'

        self.username_input: Locator = page.get_by_role("textbox", name="Username")
        self.password_input: Locator = page.get_by_role("textbox", name="Password")
        self.submit_button: Locator = page.get_by_role("button", name="Submit")
        self.error_label: Locator = page.locator("#error")

    def open(self):
        self.page.goto(self.URL)

    def enter_username(self, value):
        self.username_input.fill(value)

    def enter_password(self, value):
        self.password_input.fill(value)

    def click_on_submit(self):
        self.submit_button.click()

    def retrieve_error(self):
        return self.error_label
