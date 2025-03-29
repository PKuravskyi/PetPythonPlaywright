import pytest
from playwright.sync_api import Playwright, expect

from pages.login_page import LoginPage


@pytest.mark.login
@pytest.mark.negative
@pytest.mark.parametrize('username, password, expected_error_message',
                         [('incorrectUser', 'Password123', 'Your username is invalid!'),
                          ('student', 'incorrectPassword', 'Your password is invalid!')])
def test_negative_login(playwright: Playwright, username, password, expected_error_message) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    login_page = LoginPage(page)
    login_page.open()
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_on_submit()

    expect(login_page.retrieve_error()).to_have_text(
        expected_error_message), 'Correct error message should be present, but is not'

    context.close()
    browser.close()
