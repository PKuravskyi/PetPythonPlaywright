import time

import allure
from playwright.sync_api import Locator, Page

from pages.arts_page import ArtsPage
from pages.base_page import BasePage
from utils.constants import BASE_URL


class SignUpPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.__url: str = f'{BASE_URL}/signup'

        self.__email_input: Locator = page.get_by_role('textbox', name='E-Mail')
        self.__password_input: Locator = page.get_by_role('textbox', name='Password')
        self.__register_button: Locator = page.get_by_role('button', name='Register')

    @allure.step('Open Signup page')
    def open(self) -> 'SignUpPage':
        super()._navigate_to(self.__url)
        return self

    @allure.step('Enter random email')
    def enter_random_email(self) -> 'SignUpPage':
        username = f'{int(time.time())}@gmail.com'
        super()._type(self.__email_input, username)
        return self

    @allure.step('Enter random password')
    def enter_random_password(self) -> 'SignUpPage':
        password = str(int(time.time()))
        super()._type(self.__password_input, password)
        return self

    @allure.step('Click on Register')
    def click_on_register(self) -> ArtsPage:
        self.__register_button.click()
        self._page.wait_for_url(BASE_URL)
        return ArtsPage(self._page)
