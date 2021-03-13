from pytest import mark
from portfolio_api.config import settings
from portfolio_api.github.api import GitHubAPI


class Test_GitHub_API_Integration:
    class Test_When_not_authenticated:
        @mark.asyncio
        async def test_it_cannot_get_my_number_of_private_repos(self):
            ghAPI = GitHubAPI()
            actualUserProfile = await ghAPI.GetProfile(settings.GITHUB_USERNAME)
            assert "total_private_repos" not in actualUserProfile

    class Test_When_authenticated:
        @mark.asyncio
        async def test_it_can_get_my_number_of_private_repos(self):
            ghAPI = GitHubAPI().Authenticate(
                token=settings.GITHUB_TOKEN, user=settings.GITHUB_USERNAME
            )
            actualUserProfile = await ghAPI.GetProfile(settings.GITHUB_USERNAME)
            assert actualUserProfile["total_private_repos"] > 1
