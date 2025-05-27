"""
delivery_details_page.py

Defines the DeliveryDetailsPage class for interacting with the Delivery details page.
"""

import logging

import allure
from playwright.sync_api import Locator, Page

from pages.abstracts.base_page import BasePage
from utils.constants import BASE_URL


class DeliveryDetailsPage(BasePage):
    """
    Page object for the "Delivery details" page.
    """

    def __init__(self, page: Page, logger: logging.Logger):
        """
        Initialize the DeliveryDetailsPage with a Playwright Page instance.

        Args:
            page (Page): The current browser page instance.
            logger (logging.Logger): Logger instance.
        """
        super().__init__(page, logger)
        self.__endpoint: str = f"{BASE_URL}/delivery-details"

        self.first_name_input: Locator = page.get_by_test_id("delivery-first-name")
        self.last_name_input: Locator = page.get_by_test_id("delivery-last-name")
        self.street_input: Locator = page.get_by_test_id("delivery-address-street")
        self.post_code_input: Locator = page.get_by_test_id("delivery-postcode")
        self.city_input: Locator = page.get_by_test_id("delivery-city")
        self.continue_to_payment_button: Locator = page.get_by_test_id(
            "continue-to-payment-button"
        )

    @property
    def endpoint(self) -> str:
        """Return the endpoint URL for the Delivery details page."""
        return self.__endpoint

    def enter_delivery_address(
        self, *, first_name: str, last_name: str, street: str, post_code: str, city: str
    ) -> "DeliveryDetailsPage":
        """
        Fills in the delivery address form with the provided user details.

        Args:
            first_name (str): First name of the recipient.
            last_name (str): Last name of the recipient.
            street (str): Street address.
            post_code (str): Postal code.
            city (str): City name.

        Returns:
            DeliveryDetailsPage: The current page object for chaining further actions.
        """
        with allure.step(
            f"Enter delivery address: {first_name}, {last_name}, {street}, {post_code}, {city}"
        ):
            self.first_name_input.fill(first_name)
            self.last_name_input.fill(last_name)
            self.street_input.fill(street)
            self.post_code_input.fill(post_code)
            self.city_input.fill(city)
            self.log.debug(
                f"Entered delivery address: "
                f"first_name - {first_name}, "
                f"last_name - {last_name}, "
                f"street - {street}, "
                f"post_code - {post_code}, "
                f"city - {city}"
            )

        return DeliveryDetailsPage(self.page, self.log)
