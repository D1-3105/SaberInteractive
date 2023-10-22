from typing import Awaitable

from fastapi import FastAPI

from core.application.swagger import setup_swagger


class BaseAppFactory:
    lifespan_dependency: Awaitable

    def __init__(self, lifespan, router=None):
        self.api_router = router
        self.lifespan_dependency = lifespan

    def build_app(self):
        app = FastAPI(lifespan=self.lifespan_dependency)
        if self.api_router:
            app.include_router(self.api_router)
        app = setup_swagger(app)
        return app
