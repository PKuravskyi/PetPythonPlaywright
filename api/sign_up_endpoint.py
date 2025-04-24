import time

import allure

from api.base_api import BaseAPI


class SignUpEndpoint(BaseAPI):
    """
    Handles API requests related to user sign-up.
    """

    SIGN_UP_ENDPOINT: str = 'signup'

    @allure.step('Register random user')
    def sign_up_random_user(self) -> dict[str, str]:
        """
        Registers a user with a unique username and password based on the current timestamp.

        Returns:
            dict[str, str]: A dictionary with 'username' and 'password' used for registration.
        """
        timestamp = str(int(time.time()))
        body = {
            'username': f"auto_user_{timestamp}",
            'password': timestamp
        }

        self._post(self.SIGN_UP_ENDPOINT, body)

        return body
