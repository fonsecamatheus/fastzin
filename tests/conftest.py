import pytest
from fastapi.testclient import TestClient

from fastzin.app import app


@pytest.fixture
def client():
    return TestClient(app)
