"""
conftest.py

Pytest configuration and fixtures for UI and API tests using Playwright.
"""

import logging
import pathlib
import shutil
from collections.abc import Generator
from typing import Any

import allure
import pytest
from _pytest.nodes import Item
from _pytest.runner import CallInfo
from playwright.sync_api import Playwright, Page, APIRequestContext

from application.shopping_store_application import ShoppingStoreApplication
from utils.constants import BASE_API_URL
from utils.logger import init_logger


@pytest.fixture(scope="session")
def browser_context_args(  # pylint: disable=redefined-outer-name
    browser_context_args: dict[str, Any],
) -> dict[str, Any]:
    """Configuring browser context to ignore https errors"""
    return {
        **browser_context_args,
        "ignore_https_errors": True,
        "viewport": {"width": 1920, "height": 1080},
        "permissions": ["clipboard-read", "clipboard-write"],
    }


@pytest.fixture
def ui_page(
    playwright: Playwright, browser_name: str, request: pytest.FixtureRequest
) -> Generator[Page, Any, None]:
    """
    Fixture to initialize and return a Playwright page for UI tests.

    This fixture launches a browser (Firefox, WebKit, or Chromium) based on
    the browser_name parameter and sets up video recording for the test.

    Args:
        playwright (Playwright): The Playwright instance used to launch the browser.
        browser_name (str): The browser to launch (firefox, webkit, chromium).
        request (pytest.FixtureRequest): The pytest request object to manage test metadata and resources.
    """
    video_path = pathlib.Path("videos") / request.node.name
    video_path.mkdir(parents=True, exist_ok=True)

    if browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False)
    elif browser_name == "webkit":
        browser = playwright.webkit.launch(headless=False)
    else:
        browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(record_video_dir=str(video_path))
    context.tracing.start(
        title=request.node.nodeid, screenshots=True, snapshots=True, sources=True
    )
    page = context.new_page()

    playwright.selectors.set_test_id_attribute("data-qa")

    yield page

    # Save trace ONLY if test failed
    if dict(request.node.user_properties).get("failed", True):
        trace_dir = pathlib.Path("traces")
        trace_dir.mkdir(parents=True, exist_ok=True)
        trace_path = trace_dir / f"trace_{request.node.name}.zip"
        context.tracing.stop(path=str(trace_path))
    else:
        context.tracing.stop()

    context.close()
    browser.close()


@pytest.fixture
def api_client(
    playwright: Playwright,
) -> Generator[APIRequestContext, Any, None]:
    """
    Fixture to provide an API context for API tests.

    Args:
        playwright (Playwright): The Playwright instance used to create the request context.
    """
    request_context = playwright.request.new_context(base_url=BASE_API_URL)
    yield request_context
    request_context.dispose()


@pytest.fixture
def logger(request: pytest.FixtureRequest, browser_name: str) -> logging.Logger:
    """
    Provides an instance of ShoppingStoreApplication initialized with shared Playwright UI and API clients.

    Args:
        request (pytest.FixtureRequest): The pytest request object used to retrieve other fixtures.
        browser_name (str): The browser name.

    Returns:
       Logger instance.
    """
    test_name = request.node.originalname
    return init_logger(test_name, browser_name)


@pytest.fixture
def shopping_store_app(request: pytest.FixtureRequest) -> ShoppingStoreApplication:
    """
    Provides an instance of ShoppingStoreApplication initialized with shared Playwright UI and API clients.

    Args:
        request (pytest.FixtureRequest): The pytest request object used to retrieve other fixtures.

    Returns:
        ShoppingStoreApplication: A fully initialized application object.
    """
    return ShoppingStoreApplication(
        request.getfixturevalue("ui_page"),
        request.getfixturevalue("api_client"),
        request.getfixturevalue("logger"),
    )


@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart() -> None:
    """
    Hook that runs before a test session starts.
    """
    videos_path = pathlib.Path("videos")
    if videos_path.exists() and videos_path.is_dir():
        shutil.rmtree(videos_path)

    logs_path = pathlib.Path("logs")
    if logs_path.exists() and logs_path.is_dir():
        shutil.rmtree(logs_path)

    traces_path = pathlib.Path("traces")
    if traces_path.exists() and traces_path.is_dir():
        shutil.rmtree(traces_path)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: Item, call: CallInfo) -> Generator[None, Any, None]:
    """
    Hook that runs after 'setup', 'call' and 'teardown' phases

    Args:
        item: The pytest item (test case).
        call: The result of the test call (includes information about the test result).
    """
    outcome = yield
    result = outcome.get_result()
    if call.when == "call":
        item.user_properties.append(("failed", result.failed))


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_teardown(item: Item) -> Generator[None, Any, None]:
    """
    Hook that runs after each test.

    Args:
        item: The pytest item (test case).
    """
    yield

    # Attach results to Allure only for failed tests
    if dict(item.user_properties).get("failed", True):
        artifacts_dir_path = pathlib.Path("videos") / item.name
        # Video recording
        if artifacts_dir_path.is_dir():
            for file in artifacts_dir_path.iterdir():
                if file.is_file() and file.suffix == ".webm":
                    allure.attach.file(
                        file,
                        name=file.name,
                        attachment_type=allure.attachment_type.WEBM,
                    )
        # Playwright trace
        trace_file = pathlib.Path("traces") / f"trace_{item.name}.zip"
        if trace_file.exists():
            allure.attach.file(trace_file, name=trace_file.name, extension="zip")
