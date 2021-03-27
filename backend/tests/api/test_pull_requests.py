from fastapi.testclient import TestClient
from portfolio_api.config import settings


def test_get_featured_pull_requests(client: TestClient):
    response = client.get(f"{settings.API_V1_STR}/pull-requests/featured")
    actualPRs = response.json()
    expectedKeys = ["project", "issueNum", "link", "title", "contribIcon"]
    assert all(list(actualPR.keys()) == expectedKeys for actualPR in actualPRs)


def test_get_other_pull_requests(client: TestClient):
    response = client.get(f"{settings.API_V1_STR}/pull-requests/other")
    actualPRs = response.json()
    expectedKeys = ["project", "count", "contribIcon"]
    assert all(list(actualPR.keys()) == expectedKeys for actualPR in actualPRs)
