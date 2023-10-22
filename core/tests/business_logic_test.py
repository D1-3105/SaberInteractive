import os

import pytest
from dotenv.main import load_dotenv

from core.BL.storage import load_storage
from core.BL.traversal import TraversalBuild
from core.configs.config import CORE_PATH, settings, STORAGES


@pytest.fixture()
def setup_storages():
    load_dotenv(CORE_PATH)
    settings.storage_files = os.getenv('TEST_STORAGES').split(',')
    for i in settings.storage_files:
        st_name, st = load_storage(i)
        STORAGES[st_name] = st


def test_dfs_traversal(setup_storages):
    build_instance = STORAGES['builds'].get_build('reach_wind')
    traversal_instance = TraversalBuild(build_instance)
    assert traversal_instance.traversal_build_tasks() == [
        'build_teal_leprechauns',
        'build_black_golems',
        'bring_maroon_golems'
    ]

