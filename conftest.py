import pathlib
import shutil

import allure
import pytest
from playwright.sync_api import Playwright

from api.api_client import ApiClient
from utils.constants import BASE_API_URL


@pytest.fixture
def ui_page(playwright: Playwright, request):
    video_path = pathlib.Path('videos') / request.node.name
    video_path.mkdir(parents=True, exist_ok=True)

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
    request_context = playwright.request.new_context(base_url=BASE_API_URL)
    yield ApiClient(request_context)
    request_context.dispose()


@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart():
    videos_path = pathlib.Path('videos')
    if videos_path.exists() and videos_path.is_dir():
        shutil.rmtree(videos_path)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    if call.when == 'call':
        item.failed = result.failed


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_teardown(item):
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
