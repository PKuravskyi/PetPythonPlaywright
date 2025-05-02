"""
shopping_store_application.py

Defines the specific pages and application logic for the Shopping Store application.
Extends the abstract application structure to register all page objects needed for this app.
"""

from dataclasses import dataclass

from application.abstract_application import AbstractApplication
from application.common import CommonPages
from pages.arts_page import ArtsPage
from pages.login_page import LoginPage
from pages.my_account_page import MyAccountPage
from pages.sign_up_page import SignUpPage


@dataclass
class ShoppingStoreApplicationPages(CommonPages):
    """
    Concrete implementation of CommonPages for the Shopping Store application.

    Defines all specific pages that are part of this app.
    """
    arts_page: ArtsPage
    login_page: LoginPage
    my_account_page: MyAccountPage
    sign_up_page: SignUpPage


class ShoppingStoreApplication(AbstractApplication):
    """
    Shopping Store-specific implementation of AbstractApplication.

    Provides access to all pages via the PageFactory.
    """

    @property
    def pages(self) -> ShoppingStoreApplicationPages:
        """
        Returns:
            ShoppingStoreApplicationPages: An instance of all pages for this app.
        """
        return self._page_factory.create_pages(ShoppingStoreApplicationPages)
