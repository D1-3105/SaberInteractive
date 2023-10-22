from fastapi import APIRouter
from .controllers import make_builds


def setup_urls():
    api_router = APIRouter(
        prefix='/api/v1'
    )
    api_router.add_api_route(
        '/get_tasks',
        methods=['POST'],
        endpoint=make_builds
    )
    return api_router
