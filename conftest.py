import os

import pytest
from playwright.sync_api import Playwright

STUDENT_USERNAME = os.environ['STUDENT_USERNAME']
STUDENT_PASSWORD = os.environ['STUDENT_PASSWORD']


@pytest.fixture
def set_up(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    yield page

    context.close()
    browser.close()
