import os

import pytest
from playwright.sync_api import expect

from pages.login_page import LoginPage

try:
    STUDENT_USERNAME = os.environ['STUDENT_USERNAME']
    STUDENT_PASSWORD = os.environ['STUDENT_PASSWORD']
except KeyError:
    import utils.secrets

    STUDENT_USERNAME = utils.secrets.STUDENT_USERNAME
    STUDENT_PASSWORD = utils.secrets.STUDENT_PASSWORD


@pytest.mark.login
@pytest.mark.negative
@pytest.mark.parametrize('username, password, expected_error_message',
                         [('incorrectUser', STUDENT_PASSWORD, 'Your username is invalid!'),
                          (STUDENT_USERNAME, 'incorrectPassword', 'Your password is invalid!')])
def test_negative_login(set_up, username, password, expected_error_message) -> None:
    page = set_up
    login_page = LoginPage(page)
    login_page.open()
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_on_submit()

    expect(login_page.retrieve_error()).to_have_text(
        expected_error_message), 'Correct error message should be present, but is not'
