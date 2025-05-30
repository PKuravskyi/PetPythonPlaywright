"""
page_factory.py

Provides a PageFactory class responsible for creating instances of page objects
defined in a CommonPages dataclass. This helps decouple page construction from usage,
ensuring reusable, type-safe, and structured page management.
"""

import logging
from dataclasses import fields
from typing import Generic, cast

from playwright.sync_api import Page

from application.common import CommonPagesT
from pages.abstracts.base_page import BasePage
from pages.abstracts.page_selectors import PageSelectors


class PageFactory(PageSelectors, Generic[CommonPagesT]):
    """
    Factory class for creating and caching page objects defined in a CommonPages dataclass.

    Inherits:
        PageSelectors: Provides access to the shared Playwright page instance.
        Generic[CommonPagesT]: Enforces that only types extending CommonPages can be used.
    """

    def __init__(self, page: Page, logger: logging.Logger) -> None:
        """
        Initializes the PageFactory with the given Playwright Page object.

        Args:
            page (Page): The Playwright page used to initialize all page objects.
            logger (logging.Logger): Logger instance used across pages.
        """
        super().__init__(page)
        self._pages: CommonPagesT | None = None
        self._logger = logger

    def create_pages(self, pages_type: type[CommonPagesT]) -> CommonPagesT:
        """
        Instantiates the pages defined in a given CommonPages dataclass.

        Args:
            pages_type (Type[CommonPagesT]): The class of the dataclass holding page definitions.

        Returns:
            CommonPagesT: An instance of the dataclass with all page fields initialized.
        """
        if not self._pages:
            pages = []
            for field in fields(pages_type):
                page_type = cast(type[BasePage], field.type)
                pages.append(self.create_page(page_type))
            self._pages = pages_type(*pages)
        return self._pages

    def create_page(self, page_type: type[BasePage]) -> BasePage:
        """
        Creates an instance of a page class that inherits from BasePage.

        Args:
            page_type (Type[BasePage]): The class of the page to instantiate.

        Returns:
            BasePage: An instance of the requested page class.
        """
        return page_type(self.page, self._logger)
