from playwright.sync_api import APIRequestContext

from api.sign_up_endpoint import SignUpEndpoint


class ApiClient:
    """
    A wrapper client to organize API endpoint classes.

    Attributes:
        sign_up_endpoint (SignUpEndpoint): Handles API calls related to user sign-up.
    """

    def __init__(self, request_context: APIRequestContext):
        """
        Initialize the ApiClient with a shared API request context.

        Args:
            request_context (APIRequestContext): The Playwright API request context for making HTTP requests.
        """
        self.sign_up_endpoint: SignUpEndpoint = SignUpEndpoint(request_context)
