"""
sign_up_endpoint.py

This module provides the SignUpEndpoint class for sending API requests related to user registration.
"""
import time
from uuid import uuid4

import allure

from api.base_api import BaseAPI


class SignUpEndpoint(BaseAPI):
    """
    API endpoint class for handling user sign-up actions.

    Inherits from BaseAPI to utilize shared HTTP methods and response validation.
    """

    SIGN_UP_ENDPOINT: str = 'signup'

    @allure.step('Register random user')
    def sign_up_random_user(self) -> dict[str, str]:
        """
        Sends a POST request to the sign-up endpoint with randomly generated credentials.

        The credentials are generated using the current timestamp to ensure uniqueness.

        Returns:
            dict[str, str]: A dictionary containing the 'username' and 'password' used for registration.
        """
        timestamp = str(int(time.time()))
        body = {
            'username': f"auto_user_{timestamp}_{uuid4().hex[:12]}",
            'password': timestamp
        }

        self._post(self.SIGN_UP_ENDPOINT, body)

        return body
