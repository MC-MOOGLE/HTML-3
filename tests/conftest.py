import os

os.environ["DATABASE_URL"] = "sqlite+aiosqlite:///./test_movies.db"

import pytest
from fastapi.testclient import TestClient

from src.main import app
from src.seed import reset_and_seed


@pytest.fixture
def client():
    reset_and_seed()
    with TestClient(app) as test_client:
        yield test_client
