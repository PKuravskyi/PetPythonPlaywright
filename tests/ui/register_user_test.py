"""
test_registration.py

UI and API tests to validate that a new user can be registered via the user interface (UI)
or via the backend (API), and then logged into the system.
"""

import allure
import pytest
from playwright.sync_api import expect


@pytest.mark.ui
@pytest.mark.smoke
def test_new_user_can_be_registered_via_ui(shopping_store_app) -> None:
    """
    Test that validates a new user can be registered via the UI and redirected to the arts page.

    Steps:
    - Open the signup page.
    - Enter random email and password.
    - Click on the register button.
    - Validate that the arts page is opened with product cards.
    """
    (
        shopping_store_app
        .pages
        .sign_up_page
        .open()
        .enter_random_email()
        .enter_random_password()
        .click_on_register()
    )

    with allure.step('Validate Arts page is opened'):
        expect(
            shopping_store_app
            .pages
            .arts_page
            .get_product_cards()
        ).to_have_count(5)


@pytest.mark.ui
def test_new_user_can_be_registered_via_be(shopping_store_app, api_client) -> None:
    """
    Test that validates a new user can be registered via the backend (API) and then logged in via the UI.

    Steps:
    - Register a user via the API.
    - Open the login page and enter the credentials from the API response.
    - Log in and verify the 'My Account' page is opened.
    - Validate the user is logged into their account by checking visibility of account-related labels.
    """
    user = api_client.sign_up_endpoint.sign_up_random_user()

    (
        shopping_store_app
        .pages
        .login_page
        .open()
        .enter_email(user['username'])
        .enter_password(user['password'])
        .click_on_login()
    )

    shopping_store_app.pages.my_account_page.open()
    with allure.step('Validate user is logged into their account'):
        expect(
            shopping_store_app
            .pages
            .my_account_page
            .get_my_account_label()
        ).to_be_visible()
        expect(
            shopping_store_app
            .pages
            .my_account_page
            .get_your_address_label()
        ).to_be_visible()
