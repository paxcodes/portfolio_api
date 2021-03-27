from fastapi.testclient import TestClient
from portfolio_api.config import settings


def test_get_projects(client: TestClient):
    response = client.get(f"{settings.API_V1_STR}/projects")
    actualProjects = response.json()
    expectedKeys = [
        "title",
        "builtWith",
        "description",
        "screenshots",
        "github",
        "link",
    ]
    assert all(
        list(actualProject.keys()) == expectedKeys for actualProject in actualProjects
    )
