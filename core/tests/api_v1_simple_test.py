import json
import pathlib

from fastapi.testclient import TestClient

from core.application.base_lifespan import AppLoadingYamlLifespanStep
from core.configs.config import settings
from core.v1 import app
import pytest

TEST_RESPONSES_PATH = pathlib.Path(__file__).parent


@pytest.fixture()
def load_storages():
    storage_loader = AppLoadingYamlLifespanStep(on_load=settings.storage_files)
    storage_loader.load()


@pytest.fixture
def correct_forward_interest():
    with open(TEST_RESPONSES_PATH / 'correct_forward_interest.json', 'r') as f:
        yield json.load(f)


def test_200_gettasks_route(load_storages, correct_forward_interest):
    url = '/api/v1/get_tasks/'
    client = TestClient(app=app)
    response = client.post(url, json={'build': 'forward_interest'})
    assert response.status_code == 200, response.content.decode()
    assert response.json() == correct_forward_interest
    response = client.post(url, json={'build': 'nothing'})
    assert response.status_code == 404
