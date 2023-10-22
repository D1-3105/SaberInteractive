import os
import pathlib

from dotenv.main import load_dotenv


class Settings:
    storage_files: list

    def __init__(self):
        self.storage_files = os.getenv('STORAGES').split(',')


CORE_PATH = pathlib.Path(__file__).parent.parent
env_path = CORE_PATH.parent / '.env'
assert env_path.is_file()
if not os.getenv('STORAGES'):
    load_dotenv(env_path)

settings = Settings()

STORAGES = {
    'builds': None,
    'tasks': None
}
