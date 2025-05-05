"""
base_endpoint.py

This module defines the BaseAPI class, which provides helper methods for sending
API requests using Playwright's APIRequestContext and validating responses.

Usage:
    Subclass or use BaseAPI directly to interact with web service endpoints in a test framework.
"""
from typing import TypeVar

import requests
from playwright.sync_api import APIRequestContext, APIResponse


class BaseEndpoint:
    """
    A base class for interacting with APIs using Playwright's synchronous APIRequestContext.
    """

    def __init__(self, request_context: APIRequestContext):
        """
        Initialize the BaseAPI with a shared request context.

        Args:
            request_context (APIRequestContext): The Playwright API request context for making HTTP requests.
        """
        self._context: APIRequestContext = request_context

    def _post(self, endpoint: str, body: dict) -> APIResponse:
        """
        Send a POST request to a given endpoint with the specified request body.

        Args:
            endpoint (str): The full URL of the API endpoint to send the request to.
            body (dict): Data to send in the request body as form-encoded.

        Returns:
            APIResponse: A validated API response object.
        """
        return self.__validate_response(self._context.post(endpoint, data=body))

    def _get(self, endpoint: str) -> APIResponse:
        """
        Send a GET request to a given endpoint.

        Args:
            endpoint (str): The full URL of the API endpoint to send the request to.

        Returns:
            APIResponse: A validated API response object.
        """
        return self.__validate_response(self._context.get(endpoint))

    @staticmethod
    def __validate_response(response: APIResponse) -> APIResponse:
        """
        Validate the response object to ensure it was successful (status code 2xx).

        Args:
            response (APIResponse): The response object to validate.

        Returns:
            APIResponse: The same response object if status is OK.

        Raises:
            HTTPError: If the response has a non-success status code.
        """
        if not response.ok:
            raise requests.exceptions.HTTPError(
                f"Request to '{response.url}' failed: {response.status} {response.status_text}"
            )
        return response


BaseEndpointT = TypeVar('BaseEndpointT', bound='BaseEndpoint')
