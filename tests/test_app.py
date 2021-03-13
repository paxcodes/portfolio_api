from fastapi.testclient import TestClient
from portfolio_api.main import app

client = TestClient(app)


def test_home_should_return_hello_world():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
