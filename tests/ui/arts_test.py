"""
arts_test.py

UI test cases for validating functionality for Arts page.
"""

import allure
import pytest
from playwright.sync_api import expect

from application.shopping_store_application import ShoppingStoreApplication


@pytest.mark.ui
@pytest.mark.smoke
def test_art_can_be_added_to_basket(
    shopping_store_app: ShoppingStoreApplication,
) -> None:
    """
    Test that validates an art item can be successfully added to the basket.

    Steps:
    - Open the Arts page.
    - Ensure the basket is initially empty.
    - Add one item and validate the basket count updates to 1.
    - Add a second item and validate the basket count updates to 2.
    """
    shopping_store_app.pages.arts_page.open()

    with allure.step("Validate basket is empty"):
        expect(
            shopping_store_app.pages.arts_page.basket_counter_text_field
        ).to_have_text("0")

    shopping_store_app.pages.arts_page.add_art_to_basket("Mountain Landscape")
    with allure.step("Validate basket has 1 item"):
        expect(
            shopping_store_app.pages.arts_page.basket_counter_text_field
        ).to_have_text("1")

    shopping_store_app.pages.arts_page.add_art_to_basket("Baby Zebra with butterfly")
    with allure.step("Validate basket has 2 items"):
        expect(
            shopping_store_app.pages.arts_page.basket_counter_text_field
        ).to_have_text("2")


@pytest.mark.ui
def test_art_can_be_removed_from_basket(
    shopping_store_app: ShoppingStoreApplication,
) -> None:
    """
    Test that validates art items can be successfully removed from the basket.

    Steps:
    - Open the Arts page.
    - Add two items to the basket.
    - Remove one and validate count is 1.
    - Remove the other and validate the basket is empty.
    """
    shopping_store_app.pages.arts_page.open()

    (
        shopping_store_app.pages.arts_page.add_art_to_basket(
            "Mountain Landscape"
        ).add_art_to_basket("Baby Zebra with butterfly")
    )
    with allure.step("Validate basket has 2 items"):
        expect(
            shopping_store_app.pages.arts_page.basket_counter_text_field
        ).to_have_text("2")

    shopping_store_app.pages.arts_page.remove_art_from_basket("Mountain Landscape")
    with allure.step("Validate basket has 1 item"):
        expect(
            shopping_store_app.pages.arts_page.basket_counter_text_field
        ).to_have_text("1")

    shopping_store_app.pages.arts_page.remove_art_from_basket(
        "Baby Zebra with butterfly"
    )
    with allure.step("Validate basket is empty"):
        expect(
            shopping_store_app.pages.arts_page.basket_counter_text_field
        ).to_have_text("0")
