from playwright.sync_api import APIRequestContext

from api.sign_up_endpoint import SignUpEndpoint


class ApiClient:
    def __init__(self, request_context: APIRequestContext):
        self.sign_up_endpoint: SignUpEndpoint = SignUpEndpoint(request_context)
