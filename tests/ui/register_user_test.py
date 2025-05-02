import allure
import pytest
from playwright.sync_api import expect


@pytest.mark.ui
@pytest.mark.smoke
def test_new_user_can_be_registered_via_ui(shopping_store_app) -> None:
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
