import pytest
from playwright.sync_api import expect

from pages.arts_page import ArtsPage
from pages.sign_up_page import SignUpPage


@pytest.mark.ui
@pytest.mark.smoke
def test_new_user_can_be_registered_via_ui(set_up) -> None:
    page = set_up
    sign_up_page = SignUpPage(page)
    sign_up_page.open()
    sign_up_page.enter_random_email()
    sign_up_page.enter_random_password()
    sign_up_page.click_on_register()

    arts_page = ArtsPage(page)
    expect(arts_page.get_product_cards()).to_have_count(5)
