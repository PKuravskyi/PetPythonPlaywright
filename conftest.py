import pytest
from playwright.sync_api import Playwright


@pytest.fixture
def set_up(playwright: Playwright):
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page()

    yield page

    context.close()
    browser.close()
