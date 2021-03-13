from __future__ import annotations

from typing import Optional

import httpx

from .pr import PullRequest
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

    async def GetPullRequests(
        self, *, author: Optional[str], merged: bool = False
    ) -> PullRequest:
        apiEndpoint = f"{self.BASE_URL}/search/issues"
        query = self._PrepareSearchQuery(author, merged)
        async with httpx.AsyncClient() as client:
            response = await client.get(
                apiEndpoint, auth=self._auth, params={"q": query}
            )
        if response.status_code != 200:
            raise Exception(response.status_code)
        return PullRequest(**response.json())

    def _PrepareSearchQuery(self, author: Optional[str], merged: bool) -> str:
        query = ""
        if author:
            query = f"author:{author}"
        if merged:
            query = f"{query} is:merged"
        return query
