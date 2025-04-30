import allure
import pytest
from playwright.sync_api import expect


@pytest.mark.ui
@pytest.mark.smoke
def test_art_can_be_added_to_basket(shopping_store_app) -> None:
    shopping_store_app.pages.arts_page.open()

    with allure.step('Validate basket is empty'):
        expect(
            shopping_store_app
            .pages
            .arts_page
            .get_basket_items_locator()
        ).to_have_text('0')

    shopping_store_app.pages.arts_page.add_art_to_basket('Mountain Landscape')
    with allure.step('Validate basket has 1 item'):
        expect(
            shopping_store_app
            .pages
            .arts_page
            .get_basket_items_locator()
        ).to_have_text('1')

    shopping_store_app.pages.arts_page.add_art_to_basket('Baby Zebra with butterfly')
    with allure.step('Validate basket has 2 items'):
        expect(
            shopping_store_app
            .pages
            .arts_page
            .get_basket_items_locator()
        ).to_have_text('2')


@pytest.mark.ui
def test_art_can_be_removed_from_basket(shopping_store_app) -> None:
    shopping_store_app.pages.arts_page.open()

    (
        shopping_store_app
        .pages
        .arts_page
        .add_art_to_basket('Mountain Landscape')
        .add_art_to_basket('Baby Zebra with butterfly')
    )
    with allure.step('Validate basket has 2 items'):
        expect(
            shopping_store_app
            .pages
            .arts_page
            .get_basket_items_locator()
        ).to_have_text('2')

    shopping_store_app.pages.arts_page.remove_art_from_basket('Mountain Landscape')
    with allure.step('Validate basket has 1 item'):
        expect(
            shopping_store_app
            .pages
            .arts_page
            .get_basket_items_locator()
        ).to_have_text('1')

    shopping_store_app.pages.arts_page.add_art_to_basket('Baby Zebra with butterfly')
    with allure.step('Validate basket is empty'):
        expect(
            shopping_store_app
            .pages
            .arts_page
            .get_basket_items_locator()
        ).to_have_text('0')
