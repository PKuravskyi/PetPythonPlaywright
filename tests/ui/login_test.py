"""
test_login.py

UI test to validate log in functionality.
"""

import allure
import pytest
from playwright.sync_api import expect

from utils.file_reader import read_json


@pytest.mark.ui
@pytest.mark.smoke
def test_admin_user_can_login(shopping_store_app) -> None:
    """
    Test that validates the admin user can log into the application successfully.

    Steps:
    - Load admin credentials from JSON file.
    - Open the login page and perform login.
    - Navigate to 'My Account' page.
    - Validate the logged-in user's email is displayed.
    """
    admin_user = read_json("admin_user.json")

    (
        shopping_store_app.pages.login_page.open().login(
            admin_user["username"], admin_user["password"]
        )
    )

    shopping_store_app.pages.my_account_page.open()
    with allure.step("Validate 'admin' user is logged in"):
        expect(





            shopping_store_app.pages.my_account_page.email_address_label
        ).to_contain_text(admin_user["username"])
