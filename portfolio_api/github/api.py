from __future__ import annotations

import httpx

from .user import GitHubUser


class GitHubAPI:
    BASE_URL = "https://api.github.com"

    def __init__(self):
        self._auth = None

    def Authenticate(self, *, token: str, user: str) -> GitHubAPI:
        """Save credentials to authenticate requests.

        Args:
            token (str): The personal access token. Since this API is expected to be
                used only for Pax's purposes, a personal access token is sufficient.
            user (str): The owner of the access token.
        """
        self._auth = (user, token)
        return self

    async def GetProfile(self, username: str) -> GitHubUser:
        apiEndpoint = f"{self.BASE_URL}/users/{username}"
        async with httpx.AsyncClient() as client:
            response = await client.get(apiEndpoint, auth=self._auth)
        if response.status_code != 200:
            raise Exception(response.status_code)
        return GitHubUser(**response.json())
