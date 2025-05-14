"""
endpoint_factory.py

Provides an EndpointFactory class responsible for creating instances of endpoint objects
defined in a CommonEndpoints dataclass. This helps decouple endpoint construction from usage,
ensuring reusable, type-safe, and structured endpoint management.
"""
import logging
from dataclasses import fields
from typing import Generic, cast

from playwright.sync_api import APIRequestContext

from application.common import CommonEndpointsT
from endpoints.abstracts.base_endpoint import BaseEndpoint


class EndpointFactory(Generic[CommonEndpointsT]):
    """
    Factory class for creating and caching endpoint objects defined in a CommonEndpoints dataclass.

    Inherits:
        Generic[CommonEndpointsT]: Enforces that only types extending CommonEndpoints can be used.

    Attributes:
        _endpoints (CommonEndpointsT | None): Cached instance of the created endpoints.
    """

    def __init__(self, request_context: APIRequestContext, logger: logging.Logger) -> None:
        """
        Initializes the EndpointFactory with the given Playwright Page object.

        Args:
            request_context (APIRequestContext): Playwright request context for API testing.
            logger (logging.Logger): Logger instance used across endpoints.
        """
        super().__init__()
        self._request_context: APIRequestContext = request_context
        self._endpoints: CommonEndpointsT | None = None
        self._logger = logger

    def create_endpoints(
            self, endpoints_type: type[CommonEndpointsT]
    ) -> CommonEndpointsT:
        """
        Instantiates the endpoints defined in a given CommonEndpoints dataclass.

        Args:
            endpoints_type (Type[CommonEndpointsT]): The class of the dataclass holding endpoint definitions.

        Returns:
            CommonEndpointsT: An instance of the dataclass with all endpoint fields initialized.
        """
        if not self._endpoints:
            endpoints = []
            for field in fields(endpoints_type):
                endpoint_type = cast(type[BaseEndpoint], field.type)
                endpoints.append(self.create_endpoint(endpoint_type))
            self._endpoints = endpoints_type(*endpoints)
        return self._endpoints

    def create_endpoint(self, endpoint_type: type[BaseEndpoint]) -> BaseEndpoint:
        """
        Creates an instance of an endpoint class that inherits from BaseEndpoint.

        Args:
            endpoint_type (Type[BaseEndpoint]): The class of the endpoint to instantiate.

        Returns:
            BaseEndpoint: An instance of the requested endpoint class.
        """
        return endpoint_type(self._request_context, self._logger)
