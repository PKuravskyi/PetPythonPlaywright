import allure
import pytest
from playwright.sync_api import expect

from utils.file_reader import read_json


@pytest.mark.ui
@pytest.mark.smoke
def test_admin_user_can_login(shopping_store_app) -> None:
    admin_user = read_json('admin_user.json')

    (
        shopping_store_app
        .pages
        .login_page
        .open()
        .enter_email(admin_user['username'])
        .enter_password(admin_user['password'])
        .click_on_login()
    )

    shopping_store_app.pages.my_account_page.open()
    with allure.step('Validate Admin user is logged in'):
        expect(
            shopping_store_app
            .pages
            .my_account_page
            .get_email_address_label()
        ).to_contain_text(admin_user['username'])
