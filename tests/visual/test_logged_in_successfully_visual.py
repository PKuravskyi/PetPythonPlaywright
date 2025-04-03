import pytest

from conftest import STUDENT_USERNAME, STUDENT_PASSWORD
from pages.login_page import LoginPage


@pytest.mark.visual
def test_logged_in_successfully_visual(set_up, assert_snapshot) -> None:
    page = set_up
    login_page = LoginPage(page)
    login_page.open()
    login_page.enter_username(STUDENT_USERNAME)
    login_page.enter_password(STUDENT_PASSWORD)
    login_page.click_on_submit()

    assert_snapshot(page.screenshot(full_page=True))
