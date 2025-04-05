from playwright.sync_api import Locator
import time
from pages.base_page import BasePage


class SignUpPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.__URL = f'{self._BASE_URL}/signup'

        self.__email_input: Locator = page.get_by_role("textbox", name="E-Mail")
        self.__password_input: Locator = page.get_by_role("textbox", name="Password")
        self.__register_button: Locator = page.get_by_role("button", name="Register")

    def open(self) -> 'SignUpPage':
        super()._navigate_to(self.__URL)
        return self

    def enter_random_email(self) -> 'SignUpPage':
        username = f'{int(time.time())}@gmail.com'
        super()._type(self.__email_input, username)
        return self

    def enter_random_password(self) -> 'SignUpPage':
        password = str(int(time.time()))
        super()._type(self.__password_input, password)
        return self

    def click_on_register(self):
        self.__register_button.click()
        self._page.wait_for_url(f'{self._BASE_URL}')
