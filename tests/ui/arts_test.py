import pytest
from playwright.sync_api import expect

from pages.arts_page import ArtsPage


@pytest.mark.ui
@pytest.mark.smoke
def test_art_can_be_added_to_basket(set_up) -> None:
    page = set_up
    arts_page = ArtsPage(page)
    arts_page.open()

    expect(arts_page.get_basket_items_locator()).to_have_text('0')
    arts_page.add_art_to_basket('Mountain Landscape')
    expect(arts_page.get_basket_items_locator()).to_have_text('1')
    arts_page.add_art_to_basket('Baby Zebra with butterfly')
    expect(arts_page.get_basket_items_locator()).to_have_text('2')
