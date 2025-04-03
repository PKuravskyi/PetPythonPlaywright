import pytest
from playwright.sync_api import expect

from conftest import STUDENT_USERNAME, STUDENT_PASSWORD
from pages.logged_in_successfully_page import LoggedInSuccessfullyPage
from pages.login_page import LoginPage


@pytest.mark.logout
@pytest.mark.positive
def test_logout(set_up) -> None:
    page = set_up
    login_page = LoginPage(page)
    login_page.open()
    login_page.enter_username(STUDENT_USERNAME)
    login_page.enter_password(STUDENT_PASSWORD)
    login_page.click_on_submit()

    logged_in_successfully_page = LoggedInSuccessfullyPage(page)
    logged_in_successfully_page.click_on_logout()
    expect(login_page.retrieve_header()).to_have_text('Test login')
