# api/v1/ application

from core.application.AppFactory import BaseAppFactory
from core.v1.lifespan import lifespan
from core.v1.urls import setup_urls


class V1AppFactory(BaseAppFactory):
    def __init__(self):
        router = setup_urls()
        super().__init__(lifespan, router)


factory = V1AppFactory()

app = factory.build_app()
