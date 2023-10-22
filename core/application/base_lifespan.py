import pathlib

import yaml

from core.BL.storage import DefaultStorageFactory, load_storage
from core.configs.config import STORAGES


class BaseLifespanStep:

    def __init__(self, *args, **kwargs):
        ...

    async def load(self, *args, **kwargs):
        ...


class AppLoadingYamlLifespanStep(BaseLifespanStep):

    def __init__(self, on_load: list[pathlib.Path | str]):
        super().__init__()
        self.on_load = on_load

    def load(self):
        for file in self.on_load:
            name, storage = load_storage(file)
            STORAGES.update({name: storage})
