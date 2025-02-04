# This file was generated by liblab | https://liblab.com/

from .services.authorize import AuthorizeService
from .services.token import TokenService
from .services.refresh import RefreshService
from .net.environment import Environment


class Ups0authCode:
    def __init__(
        self,
        username: str = None,
        password: str = None,
        base_url: str = Environment.DEFAULT.value,
    ):
        """
        Initializes Ups0authCode the SDK class.
        """
        self.authorize = AuthorizeService(base_url=base_url)
        self.token = TokenService(base_url=base_url)
        self.refresh = RefreshService(base_url=base_url)
        self.set_basic_auth(username=username, password=password)

    def set_base_url(self, base_url):
        """
        Sets the base URL for the entire SDK.
        """
        self.authorize.set_base_url(base_url)
        self.token.set_base_url(base_url)
        self.refresh.set_base_url(base_url)

        return self

    def set_basic_auth(self, username: str, password: str):
        """
        Sets the username and password for the entire SDK.
        """
        self.authorize.set_basic_auth(username=username, password=password)
        self.token.set_basic_auth(username=username, password=password)
        self.refresh.set_basic_auth(username=username, password=password)

        return self


# c029837e0e474b76bc487506e8799df5e3335891efe4fb02bda7a1441840310c
