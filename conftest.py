import pathlib
import shutil

import allure
import pytest
from playwright.sync_api import Playwright

from api.api_client import ApiClient
from application.shopping_store_application import ShoppingStoreApplication
from utils.constants import BASE_API_URL


@pytest.fixture
def ui_page(playwright: Playwright, browser_name, request):
    """
    Fixture to initialize and return a Playwright page for UI tests.

    This fixture launches a browser (Firefox, WebKit, or Chromium) based on
    the browser_name parameter and sets up video recording for the test.

    Args:
        playwright (Playwright): The Playwright instance to launch the browser.
        browser_name (str): The browser to launch (firefox, webkit, chromium).
        request: Pytest fixture request to manage test metadata and resources.
    """
    video_path = pathlib.Path('videos') / request.node.name
    video_path.mkdir(parents=True, exist_ok=True)

    if browser_name == 'firefox':
        browser = playwright.firefox.launch(headless=False)
    elif browser_name == 'webkit':
        browser = playwright.webkit.launch(headless=False)
    else:
        browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(
        record_video_dir=str(video_path)
    )
    page = context.new_page()

    yield page

    context.close()
    browser.close()


@pytest.fixture(scope='session')
def api_client(playwright: Playwright):
    """
    Fixture to provide an instance of ApiClient for API tests.

    This fixture creates a new API request context using the base URL and
    provides an ApiClient instance for interaction with the API.

    Args:
        playwright (Playwright): The Playwright instance to create the request context.
    """
    request_context = playwright.request.new_context(base_url=BASE_API_URL)
    yield ApiClient(request_context)
    request_context.dispose()


@pytest.fixture
def shopping_store_app(ui_page):
    """
    Fixture that returns a CustomApplication instance initialized with the shared Playwright page.
    """
    return ShoppingStoreApplication(ui_page)


@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart():
    """
    Hook to clean up old video recordings before a test session starts.

    This hook removes any existing video directory to ensure fresh video recordings
    for each session.
    """
    videos_path = pathlib.Path('videos')
    if videos_path.exists() and videos_path.is_dir():
        shutil.rmtree(videos_path)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to mark the test item as failed if the test execution fails.

    This hook captures the result of a test execution and sets the `failed` attribute
    on the item if the test fails.

    Args:
        item: The pytest item (test case).
        call: The result of the test call.
    """
    outcome = yield
    result = outcome.get_result()
    if call.when == 'call':
        item.failed = result.failed


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_teardown(item):
    """
    Hook to attach video files as artifacts if a test fails.

    This hook attaches video files recorded during the test to the Allure report if
    the test fails. The video is retrieved from the 'videos' directory.

    Args:
        item: The pytest item (test case).
    """
    yield

    if getattr(item, 'failed', False):
        artifacts_dir_path = pathlib.Path('videos') / item.name
        if artifacts_dir_path.is_dir():
            for file in artifacts_dir_path.iterdir():
                if file.is_file() and file.suffix == '.webm':
                    allure.attach.file(
                        file,
                        name=file.name,
                        attachment_type=allure.attachment_type.WEBM,
                    )
