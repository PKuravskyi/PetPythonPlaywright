from dataclasses import fields
from typing import Generic, Type

from playwright.sync_api import Page

from application.common import CommonPagesT
from pages.abstracts.base_page import BasePageT
from pages.abstracts.page_selectors import PageSelectors


class PageFactory(PageSelectors, Generic[CommonPagesT]):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self._pages = None

    def create_pages(self, pages_type: Type[CommonPagesT]) -> CommonPagesT:
        """
        Creates pages dataclass. Every dataclass field must be BasePage or inherited from it.
        """
        if not self._pages:
            pages = []
            for field in fields(pages_type):
                page_type = field.type
                pages.append(self.create_page(page_type))
            self._pages = pages_type(*pages)
        return self._pages

    def create_page(self, page_type: Type[BasePageT]) -> BasePageT:
        """
        Creates an instance of BasePage object or inherited from it.
        """
        return page_type(self.page)
