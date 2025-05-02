"""
abstract_application.py

Defines an abstract base class for an application, encapsulating shared setup logic
such as page factory initialization. Intended to be extended by specific application implementations.
"""

from abc import ABC, abstractmethod

from playwright.sync_api import Page

from application.factories.page_factory import PageFactory


class AbstractApplication(ABC):
    """
    Abstract base class for application objects.

    Provides common functionality such as initializing the PageFactory used
    to create and manage page objects. Subclasses must implement the `pages` property.
    """

    def __init__(self, page: Page):
        """
        Initialize the AbstractApplication.

        Args:
            page (Page): Playwright Page instance used to drive the browser.
        """
        super().__init__()
        self._app_page_factory = PageFactory(page)

    @property
    @abstractmethod
    def pages(self):
        """
        Abstract property that must return an object containing all page instances.

        Must be implemented by subclasses to provide access to application-specific pages.
        """
        ...

    @property
    def _page_factory(self) -> PageFactory:
        """
        Returns the internal PageFactory instance used to create page objects.

        Returns:
            PageFactory: The factory responsible for creating page instances.
        """
        return self._app_page_factory
