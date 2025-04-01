import pytest
from playwright.sync_api import Playwright, expect

from pages.logged_in_successfully_page import LoggedInSuccessfullyPage
from pages.login_page import LoginPage


@pytest.mark.login
@pytest.mark.positive
def test_positive_login(set_up) -> None:
    page = set_up
    login_page = LoginPage(page)
    login_page.open()
    login_page.enter_username('student')
    login_page.enter_password('Password123')
    login_page.click_on_submit()
    logged_in_successfully_page = LoggedInSuccessfullyPage(page)
    expect(logged_in_successfully_page.get_title_label()).to_be_visible()
    expect(logged_in_successfully_page.get_description_label()).to_be_visible()
