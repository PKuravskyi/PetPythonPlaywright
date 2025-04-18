from playwright.sync_api import APIRequestContext, APIResponse


class BaseAPI:
    def __init__(self, request_context: APIRequestContext):
        self._context: APIRequestContext = request_context

    def _post(self, endpoint: str, body: dict) -> APIResponse:
        return self._context.post(endpoint, data=body)

    def _get(self, endpoint: str) -> APIResponse:
        return self._context.get(endpoint)
