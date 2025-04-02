import os

import pytest
from playwright.sync_api import expect

from pages.logged_in_successfully_page import LoggedInSuccessfullyPage
from pages.login_page import LoginPage

try:
    STUDENT_USERNAME = os.environ['STUDENT_USERNAME']
    STUDENT_PASSWORD = os.environ['STUDENT_PASSWORD']
except KeyError:
    import utils.secrets

    STUDENT_USERNAME = utils.secrets.STUDENT_USERNAME
    STUDENT_PASSWORD = utils.secrets.STUDENT_PASSWORD


@pytest.mark.login
@pytest.mark.positive
def test_positive_login(set_up) -> None:
    page = set_up
    login_page = LoginPage(page)
    login_page.open()
    login_page.enter_username(STUDENT_USERNAME)
    login_page.enter_password(STUDENT_PASSWORD)
    login_page.click_on_submit()
    logged_in_successfully_page = LoggedInSuccessfullyPage(page)
    expect(logged_in_successfully_page.get_title_label()).to_be_visible()
    expect(logged_in_successfully_page.get_description_label()).to_be_visible()
