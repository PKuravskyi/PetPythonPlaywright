import allure
from playwright.sync_api import Locator, Page

from pages.arts_page import ArtsPage
from pages.base_page import BasePage
from utils.constants import BASE_URL


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.__url: str = f'{BASE_URL}/login'

        self.__email_input: Locator = page.get_by_role('textbox', name='E-Mail')
        self.__password_input: Locator = page.get_by_role('textbox', name='Password')
        self.__login_button: Locator = page.get_by_role('button', name='Login')

    @allure.step('Open Login page')
    def open(self) -> 'LoginPage':
        super()._navigate_to(self.__url)
        return self

    @allure.step("Enter '{value}' email")
    def enter_email(self, value: str) -> 'LoginPage':
        super()._type(self.__email_input, value)
        return self

    @allure.step("Enter '{value}' password")
    def enter_password(self, value: str) -> 'LoginPage':
        super()._type(self.__password_input, value)
        return self

    @allure.step('Click on Login')
    def click_on_login(self) -> ArtsPage:
        self.__login_button.click()
        self._page.wait_for_url(BASE_URL)
        return ArtsPage(self._page)
