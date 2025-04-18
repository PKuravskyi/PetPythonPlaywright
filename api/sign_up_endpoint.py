import time

import allure

from api.base_api import BaseAPI


class SignUpEndpoint(BaseAPI):
    SIGN_UP_ENDPOINT = 'signup'

    @allure.step('Register random user')
    def sign_up_random_user(self):
        timestamp = str(int(time.time()))
        body = {
            'username': f"auto_user_{timestamp}",
            'password': timestamp
        }

        response = self._post(self.SIGN_UP_ENDPOINT, body)
        assert response.status == 200

        return body
