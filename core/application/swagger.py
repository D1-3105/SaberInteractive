from urllib.request import Request

from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html


async def swagger_ui_route(request: Request):
    return get_swagger_ui_html(
        openapi_url='/openapi.json',
        title='V1 - Swagger UI',
        swagger_ui_parameters={
            "syntaxHighlight.theme": "obsidian",
            "defaultModelsExpandDepth": -1
        }
    )


def setup_swagger(app: FastAPI):
    app.add_route('/api/doc/', route=swagger_ui_route, methods=['get'], name='swagger_v1', include_in_schema=False)
    app.openapi_url = '/openapi.json'
    return app

