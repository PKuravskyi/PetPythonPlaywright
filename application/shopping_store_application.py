from dataclasses import dataclass

from playwright.sync_api import Page

from application.abstract_application import AbstractApplication
from application.common import CommonPages
from pages.arts_page import ArtsPage
from pages.login_page import LoginPage
from pages.my_account_page import MyAccountPage
from pages.sign_up_page import SignUpPage


@dataclass
class ShoppingStoreApplicationPages(CommonPages):
    arts_page: ArtsPage
    login_page: LoginPage
    my_account_page: MyAccountPage
    sign_up_page: SignUpPage


class ShoppingStoreApplication(AbstractApplication):
    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def pages(self) -> ShoppingStoreApplicationPages:
        return self.page_factory.create_pages(ShoppingStoreApplicationPages)
