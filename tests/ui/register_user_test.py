import allure
import pytest
from playwright.sync_api import expect

from pages.arts_page import ArtsPage
from pages.login_page import LoginPage
from pages.my_account_page import MyAccountPage
from pages.sign_up_page import SignUpPage


@pytest.mark.ui
@pytest.mark.smoke
def test_new_user_can_be_registered_via_ui(ui_page) -> None:
    page = ui_page
    sign_up_page = SignUpPage(page)
    (
        sign_up_page
        .open()
        .enter_random_email()
        .enter_random_password()
        .click_on_register()
    )

    arts_page = ArtsPage(page)
    with allure.step('Validate Arts page is opened'):
        expect(arts_page.get_product_cards()).to_have_count(5)


@pytest.mark.ui
def test_new_user_can_be_registered_via_be(api_client, ui_page) -> None:
    user = api_client.sign_up_endpoint.sign_up_random_user()

    page = ui_page
    login_page = LoginPage(page)
    (
        login_page
        .open()
        .enter_email(user['username'])
        .enter_password(user['password'])
        .click_on_login()
    )

    my_account_page = MyAccountPage(page)
    my_account_page.open()
    with allure.step('Validate user is logged into their account'):
        expect(my_account_page.get_my_account_label()).to_be_visible()
        expect(my_account_page.get_your_address_label()).to_be_visible()
