from abc import ABC, abstractmethod

from playwright.sync_api import Page

from application.factories.page_factory import PageFactory


class AbstractApplication(ABC):
    def __init__(self, page: Page):
        super().__init__()
        self._page_factory = PageFactory(page)

    @property
    @abstractmethod
    def pages(self):
        ...

    @property
    def page_factory(self) -> PageFactory:
        return self._page_factory
