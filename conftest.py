import pytest
from playwright.sync_api import Playwright

from api.api_client import ApiClient
from utils.constants import BASE_API_URL


@pytest.fixture
def ui_page(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    yield page

    context.close()
    browser.close()


@pytest.fixture(scope='session')
def api_client(playwright: Playwright):
    request_context = playwright.request.new_context(base_url=BASE_API_URL)
    yield ApiClient(request_context)
    request_context.dispose()
