from typing import Generator

from fastapi.testclient import TestClient
from portfolio_api.main import app
from pytest import fixture


@fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c
