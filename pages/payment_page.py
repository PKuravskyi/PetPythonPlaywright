"""
payment_page.py

Defines the PaymentPage class for interacting with the payment screen.
"""

import logging

import allure
from playwright.sync_api import Locator, Page

from pages.abstracts.base_page import BasePage
from utils.constants import BASE_URL


class PaymentPage(BasePage):
    """
    Page object for the payment page of the application.
    """

    def __init__(self, page: Page, logger: logging.Logger):
        """
        Initialize the PaymentPage with a Playwright Page instance.

        Args:
            page (Page): The current browser page instance.
            logger (logging.Logger): Logger instance.
        """
        super().__init__(page, logger)
        self.__endpoint: str = f"{BASE_URL}/payment"

        self.credit_card_owner_input: Locator = page.get_by_test_id("credit-card-owner")
        self.credit_card_number_input: Locator = page.get_by_test_id(
            "credit-card-number"
        )
        self.valid_until_input_input: Locator = page.get_by_test_id("valid-until")
        self.credit_card_cvc_input: Locator = page.get_by_test_id("credit-card-cvc")
        self.pay_button: Locator = page.get_by_test_id("pay-button")

    @property
    def endpoint(self) -> str:
        """Return the endpoint URL for the Payment page."""
        return self.__endpoint

    def enter_credit_card_details(
        self, cc_owner: str, cc_number: str, valid_until: str, cc_cvc: str
    ) -> "PaymentPage":
        """
        Fills in the credit card payment form with the provided card details.

        Args:
            cc_owner (str): Name of the credit card owner.
            cc_number (str): Credit card number.
            valid_until (str): Expiry date of the card (e.g., MM/YY).
            cc_cvc (str): Card security code (CVC/CVV).

        Returns:
            PaymentPage: The current page object for chaining further actions.
        """
        with allure.step(
            f"Enter credit card details: {cc_owner}, {cc_number}, {valid_until}, {cc_cvc}"
        ):
            self.credit_card_owner_input.fill(cc_owner)
            self.credit_card_number_input.fill(cc_number)
            self.valid_until_input_input.fill(valid_until)
            self.credit_card_cvc_input.fill(cc_cvc)
            self.log.debug(
                f"Entered credit card details: cc_owner - {cc_owner}, cc_number - {cc_number}, valid_until - {valid_until}, cc_cvc - {cc_cvc}"
            )

        return PaymentPage(self.page, self.log)
