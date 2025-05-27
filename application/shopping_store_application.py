"""
shopping_store_application.py

Defines the specific pages and application logic for the Shopping Store application.
Extends the abstract application structure to register all page objects needed for this app.
"""

from dataclasses import dataclass

from application.abstract_application import AbstractApplication
from application.common import CommonPages, CommonEndpoints
from endpoints.sign_up_endpoint import SignUpEndpoint
from pages.arts_page import ArtsPage
from pages.basket_page import BasketPage
from pages.delivery_details_page import DeliveryDetailsPage
from pages.login_page import LoginPage
from pages.my_account_page import MyAccountPage
from pages.payment_page import PaymentPage
from pages.sign_up_page import SignUpPage
from pages.thank_you_page import ThankYouPage


@dataclass
class ShoppingStoreApplicationPages(CommonPages):
    """
    Concrete implementation of CommonPages for the Shopping Store application.

    Defines all specific pages that are part of this app.
    """

    # pylint: disable=too-many-instance-attributes
    arts_page: ArtsPage
    login_page: LoginPage
    my_account_page: MyAccountPage
    sign_up_page: SignUpPage
    basket_page: BasketPage
    delivery_details_page: DeliveryDetailsPage
    payment_page: PaymentPage
    thank_you_page: ThankYouPage


@dataclass
class ShoppingStoreApplicationEndpoints(CommonEndpoints):
    """
    Concrete implementation of CommonEndpoints for the Shopping Store application.

    Defines all specific endpoints that are part of this app.
    """

    sign_up_endpoint: SignUpEndpoint


class ShoppingStoreApplication(AbstractApplication):
    """
    Shopping Store-specific implementation of AbstractApplication.

    Provides access to all pages and endpoints.
    """

    @property
    def pages(self) -> ShoppingStoreApplicationPages:
        """
        Returns:
            ShoppingStoreApplicationPages: An instance of all pages for this app.
        """
        return self._page_factory.create_pages(ShoppingStoreApplicationPages)

    @property
    def endpoints(self) -> ShoppingStoreApplicationEndpoints:
        """
        Returns:
            ShoppingStoreApplicationEndpoints: An instance of all endpoints for this app.
        """
        return self._endpoint_factory.create_endpoints(
            ShoppingStoreApplicationEndpoints
        )
