from playwright.sync_api import APIRequestContext, APIResponse


class BaseAPI:
    """
    Base class for making API calls using Playwright's APIRequestContext.
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
        Send a POST request and validate the response.

        Args:
            endpoint (str): API endpoint URL.
            body (dict): Data to send in the request body.

        Returns:
            APIResponse: Validated response object.
        """
        return self.__validate_response(self._context.post(endpoint, data=body))

    def _get(self, endpoint: str) -> APIResponse:
        """
        Send a GET request and validate the response.

        Args:
            endpoint (str): API endpoint URL.

        Returns:
            APIResponse: Validated response object.
        """
        return self.__validate_response(self._context.get(endpoint))

    @staticmethod
    def __validate_response(response: APIResponse) -> APIResponse:
        """
        Validates an API response.

        Args:
            response (APIResponse): The response to validate.

        Returns:
            APIResponse: The original response if valid.

        Raises:
            Exception: If the response status is not OK.
        """
        if not response.ok:
            raise Exception(f"Request to '{response.url}' failed: {response.status} {response.status_text}")
        return response
