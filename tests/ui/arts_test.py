import allure
import pytest
from playwright.sync_api import expect

from pages.arts_page import ArtsPage


@pytest.mark.ui
@pytest.mark.smoke
def test_art_can_be_added_to_basket(ui_page) -> None:
    page = ui_page
    arts_page = ArtsPage(page)
    arts_page.open()

    with allure.step('Check basket is empty'):
        expect(arts_page.get_basket_items_locator()).to_have_text('0')

    arts_page.add_art_to_basket('Mountain Landscape')
    with allure.step('Check basket has 1 item'):
        expect(arts_page.get_basket_items_locator()).to_have_text('1')

    arts_page.add_art_to_basket('Baby Zebra with butterfly')
    with allure.step('Check basket has 2 items'):
        expect(arts_page.get_basket_items_locator()).to_have_text('2')


@pytest.mark.ui
def test_art_can_be_removed_from_basket(ui_page) -> None:
    page = ui_page
    arts_page = ArtsPage(page)
    arts_page.open()

    (
        arts_page
        .add_art_to_basket('Mountain Landscape')
        .add_art_to_basket('Baby Zebra with butterfly')
    )
    with allure.step('Check basket has 2 items'):
        expect(arts_page.get_basket_items_locator()).to_have_text('2')

    arts_page.remove_art_from_basket('Mountain Landscape')
    with allure.step('Check basket has 1 item'):
        expect(arts_page.get_basket_items_locator()).to_have_text('1')

    arts_page.add_art_to_basket('Baby Zebra with butterfly')
    with allure.step('Check basket is empty'):
        expect(arts_page.get_basket_items_locator()).to_have_text('0')
