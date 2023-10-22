import os
from contextlib import asynccontextmanager

from core.application.base_lifespan import AppLoadingYamlLifespanStep
from core.configs.config import settings


@asynccontextmanager
async def lifespan(app):
    storage_loader = AppLoadingYamlLifespanStep(on_load=settings.storage_files)
    storage_loader.load()
    yield

