from playwright.sync_api import APIRequestContext


class BaseAPI:
    def __init__(self, request_context: APIRequestContext):
        self._context = request_context

    def _post(self, endpoint: str, body: dict):
        return self._context.post(endpoint, data=body)

    def _get(self, endpoint: str):
        return self._context.get(endpoint)
