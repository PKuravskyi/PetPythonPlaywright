import pytest

from pages.login_page import LoginPage


@pytest.mark.visual
def test_login_visual(set_up, assert_snapshot) -> None:
    page = set_up
    login_page = LoginPage(page)
    login_page.open()

    assert_snapshot(page.screenshot(full_page=True))
