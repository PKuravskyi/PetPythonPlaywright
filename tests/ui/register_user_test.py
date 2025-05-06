"""
test_registration.py

UI and API tests to validate that a new user can be registered via the user interface (UI)
or via the backend (API), and then logged into the system.
"""

import allure
import pytest
from playwright.sync_api import expect

from application.shopping_store_application import ShoppingStoreApplication


@pytest.mark.ui
@pytest.mark.smoke
def test_new_user_can_be_registered_via_ui(shopping_store_app: ShoppingStoreApplication) -> None:
    """
    Test that validates a new user can be registered via the UI and redirected to the arts page.

    Steps:
    - Open the signup page.
    - Register user with random email and password.
    - Validate that the arts page is opened with product cards.
    """
    (shopping_store_app.pages.sign_up_page.open().register_random_user())

    with allure.step("Validate Arts page is opened"):
        expect(shopping_store_app.pages.arts_page.products_cards).to_have_count(5)


@pytest.mark.ui
def test_new_user_can_be_registered_via_be(shopping_store_app: ShoppingStoreApplication) -> None:
    """
    Test that validates a new user can be registered via the backend (API) and then logged in via the UI.

    Steps:
    - Register a user via the API.
    - Open the login page and enter the credentials from the API response.
    - Log in and validate the 'My Account' page is opened.
    - Validate the user is logged into their account by checking visibility of account-related labels.
    """
    user = shopping_store_app.endpoints.sign_up_endpoint.sign_up_random_user()

    (
        shopping_store_app.pages.login_page.open().login(
            user["username"], user["password"]
        )
    )

    shopping_store_app.pages.my_account_page.open()
    with allure.step("Validate user is logged into their account"):
        expect(
            shopping_store_app.pages.my_account_page.my_account_label
        ).to_be_visible()
        expect(
            shopping_store_app.pages.my_account_page.your_addresses_label
        ).to_be_visible()
