import allure
import pytest
from playwright.sync_api import expect

from pages.arts_page import ArtsPage
from pages.my_account_page import MyAccountPage
from pages.sign_up_page import SignUpPage


@pytest.mark.ui
@pytest.mark.smoke
def test_new_user_can_be_registered_via_ui(ui_page) -> None:
    page = ui_page
    sign_up_page = SignUpPage(page)
    sign_up_page.open()
    sign_up_page.enter_random_email()
    sign_up_page.enter_random_password()
    sign_up_page.click_on_register()

    arts_page = ArtsPage(page)
    with allure.step('Check Arts page is opened'):
        expect(arts_page.get_product_cards()).to_have_count(5)


@pytest.mark.ui
def test_new_user_can_be_registered_via_be(api_client, ui_page) -> None:
    user = api_client.sign_up_endpoint.sign_up_random_user()

    page = ui_page
    my_account_page = MyAccountPage(page)
    my_account_page.open()
    my_account_page.enter_email(user['username'])
    my_account_page.enter_password(user['password'])
    my_account_page.click_on_login()

    with allure.step('Check user is logged into his account'):
        expect(my_account_page.get_my_account_label()).to_be_visible()
        expect(my_account_page.get_your_address_label()).to_be_visible()
