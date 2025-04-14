from playwright.sync_api import Locator

from pages.base_page import BasePage
from utils.constants import BASE_URL


class MyAccountPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.__url = f'{BASE_URL}/my-account'

        self.__email_input: Locator = page.get_by_role("textbox", name="E-Mail")
        self.__password_input: Locator = page.get_by_role("textbox", name="Password")
        self.__login_button: Locator = page.get_by_role("button", name="Login")
        self.__my_account_label = page.get_by_role("heading", name="My Account")
        self.__your_addresses_label = page.get_by_role("heading", name="Your addresses")

    def open(self) -> 'MyAccountPage':
        super()._navigate_to(self.__url)
        return self

    def enter_email(self, value) -> 'MyAccountPage':
        super()._type(self.__email_input, value)
        return self

    def enter_password(self, value) -> 'MyAccountPage':
        super()._type(self.__password_input, value)
        return self

    def click_on_login(self):
        self.__login_button.click()
        self._page.wait_for_url(self.__url)

    def get_my_account_label(self):
        return self.__my_account_label

    def get_your_address_label(self):
        return self.__your_addresses_label
