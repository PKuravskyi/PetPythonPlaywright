import allure
from playwright.sync_api import Locator, Page

from pages.base_page import BasePage
from utils.constants import BASE_URL


class MyAccountPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.__url: str = f'{BASE_URL}/my-account'

        self.__my_account_label: Locator = page.get_by_role('heading', name='My Account')
        self.__your_addresses_label: Locator = page.get_by_role('heading', name='Your addresses')

    @allure.step('Open My Account page')
    def open(self) -> 'MyAccountPage':
        super()._navigate_to(self.__url)
        return self

    def get_my_account_label(self) -> Locator:
        return self.__my_account_label

    def get_your_address_label(self) -> Locator:
        return self.__your_addresses_label
