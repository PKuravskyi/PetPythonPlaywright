"""
abstract_application.py

Defines an abstract base class for an application, encapsulating shared setup logic.
Intended to be extended by specific application implementations.
"""
import logging
from abc import ABC, abstractmethod
from typing import Any

from playwright.sync_api import Page, APIRequestContext

from application.factories.endpoint_factory import EndpointFactory
from application.factories.page_factory import PageFactory


class AbstractApplication(ABC):
    """
    Abstract base class for application objects.

    Provides shared setup logic.
    """

    def __init__(self, page: Page, request_context: APIRequestContext, logger: logging.Logger):
        """
        Initialize the AbstractApplication.

        Args:
            page (Page): Playwright Page instance for browser automation.
            request_context (APIRequestContext): Playwright request context for API testing.
            logger (logging.Logger): Logger instance used across application.
        """
        super().__init__()
        self._app_page_factory: PageFactory = PageFactory(page, logger)
        self._app_endpoint_factory: EndpointFactory = EndpointFactory(request_context, logger)

    @property
    @abstractmethod
    def pages(self) -> Any:
        """
        Abstract property to access application-specific page objects.

        Returns:
            An object containing all page instances for the application.
        """
        ...

    @property
    @abstractmethod
    def endpoints(self) -> Any:
        """
        Abstract property to access application-specific endpoint objects.

        Returns:
            An object containing all API endpoint instances for the application.
        """
        ...

    @property
    def _page_factory(self) -> PageFactory:
        """
        Internal accessor for the PageFactory instance.

        Returns:
            PageFactory: Factory used to create and retrieve page objects.
        """
        return self._app_page_factory

    @property
    def _endpoint_factory(self) -> EndpointFactory:
        """
        Internal accessor for the EndpointFactory instance.

        Returns:
            EndpointFactory: Factory used to create and retrieve endpoint objects.
        """
        return self._app_endpoint_factory
