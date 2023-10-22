from fastapi import Body, HTTPException

from core.BL.traversal import TraversalBuild
from core.configs.config import STORAGES
from core.v1.schemas import BuildInputSchema


async def make_builds(
        post_params: BuildInputSchema = Body(BuildInputSchema)
) -> list[str]:
    build_instance = STORAGES['builds'].get_build(post_params.build)
    if not build_instance:
        raise HTTPException(status_code=404, detail="Build not found")
    return TraversalBuild(build_instance).traversal_build_tasks()
