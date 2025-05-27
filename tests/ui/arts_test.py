"""
arts_test.py

UI test cases for validating functionality for Arts page.
"""

import allure
import pytest
from playwright.sync_api import expect

from application.shopping_store_application import ShoppingStoreApplication
from utils.file_reader import read_csv, read_json


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


@pytest.mark.ui
@pytest.mark.parametrize("sort_option", ["price-asc", "price-desc"])
def test_arts_can_be_sorted_by_price(
    shopping_store_app: ShoppingStoreApplication, sort_option: str
) -> None:
    """
    Test that validates arts are sorted correctly by price in ascending or descending order.

    Steps:
    - Open the Arts page.
    - Select the desired sort option (price ascending or descending).
    - Validate that the prices are sorted according to the selected option.
    """
    shopping_store_app.pages.arts_page.open().sort_arts_by(sort_option)
    prices = shopping_store_app.pages.arts_page.products_prices

    with allure.step(f"Validate arts are sorted by '{sort_option}'"):
        expect(prices).to_have_text(
            sorted(prices.all_text_contents(), reverse=sort_option == "price-desc")
        )


@pytest.mark.ui
@pytest.mark.smoke
def test_art_can_be_purchased(
    shopping_store_app: ShoppingStoreApplication,
) -> None:
    """
    Test that validates art can be successfully purchased.

    Steps:
    - Sign up a new random user and log in.
    - Add two specific art items to the basket on Arts page.
    - Enter delivery address on Checkout page.
    - Enter credit card details on Payment page.
    - Validate the thank-you page is displayed (purchase was successful).
    """

    user = shopping_store_app.endpoints.sign_up_endpoint.sign_up_random_user()
    (
        shopping_store_app.pages.login_page.open().login(
            user["username"], user["password"]
        )
    )

    shopping_store_app.pages.arts_page.open()

    (
        shopping_store_app.pages.arts_page.add_art_to_basket(
            "Mountain Landscape"
        ).add_art_to_basket("Baby Zebra with butterfly")
    )
    shopping_store_app.pages.basket_page.open().continue_to_checkout_button.click()

    delivery_address = read_csv("delivery_address.csv")[0]
    shopping_store_app.pages.delivery_details_page.enter_delivery_address(
        delivery_address["first_name"],
        delivery_address["last_name"],
        delivery_address["street"],
        delivery_address["post_code"],
        delivery_address["city"],
    )
    shopping_store_app.pages.delivery_details_page.continue_to_payment_button.click()

    cc_details = read_json("credit_card_details.json")
    shopping_store_app.pages.payment_page.enter_credit_card_details(
        cc_details["cc_owner"],
        cc_details["cc_number"],
        cc_details["valid_until"],
        cc_details["cc_cvc"],
    )
    shopping_store_app.pages.payment_page.pay_button.click()

    with allure.step(f"Validate Thank-you page is opened after successful purchase"):
        expect(
            shopping_store_app.pages.thank_you_page.back_to_shop_button
        ).to_be_visible()
