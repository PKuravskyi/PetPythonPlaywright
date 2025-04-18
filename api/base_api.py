from playwright.sync_api import APIRequestContext, APIResponse


class BaseAPI:
    def __init__(self, request_context: APIRequestContext):
        self._context: APIRequestContext = request_context

    def _post(self, endpoint: str, body: dict) -> APIResponse:
        return self.__validate_response(self._context.post(endpoint, data=body))

    def _get(self, endpoint: str) -> APIResponse:
        return self.__validate_response(self._context.get(endpoint))

    @staticmethod
    def __validate_response(response: APIResponse) -> APIResponse:
        if not response.ok:
            raise Exception(f"Request to '{response.url}' failed: {response.status} {response.status_text}")
        return response
