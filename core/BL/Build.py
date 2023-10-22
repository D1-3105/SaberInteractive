from pydantic import BaseModel, Field


class Build(BaseModel):
    """
        Object for build validation
    """
    name: str
    dependencies: list = Field(alias='tasks')
