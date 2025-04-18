import allure
import pytest
from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.my_account_page import MyAccountPage
from utils.file_reader import read_json


@pytest.mark.ui
@pytest.mark.smoke
def test_admin_user_can_login(ui_page) -> None:
    page = ui_page
    login_page = LoginPage(page)

    admin_user = read_json('admin_user.json')
    (
        login_page
        .open()
        .enter_email(admin_user['username'])
        .enter_password(admin_user['password'])
        .click_on_login()
    )

    my_account_page = MyAccountPage(page)
    my_account_page.open()
    with allure.step('Validate Admin user is logged in'):
        expect(my_account_page.get_email_address_label()).to_contain_text(admin_user['username'])
