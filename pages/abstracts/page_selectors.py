"""
page_selectors.py

Provides a base class to expose Playwright's Page object to child classes.
Useful for selector management and page-level actions.
"""

from playwright.sync_api import Page


class PageSelectors:
    """
    Base class to hold and expose the Playwright Page instance.

    Useful for classes that require access to the browser page for interactions.
    """

    def __init__(self, page: Page) -> None:
        """
        Initialize the PageSelectors with a Playwright Page.

        Args:
            page (Page): The Playwright page object.
        """
        self._page = page

    @property
    def page(self) -> Page:
        """
        Get the Playwright Page instance.

        Returns:
            Page: The current Playwright page.
        """
        return self._page
