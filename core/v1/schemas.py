from pydantic import BaseModel


class BuildInputSchema(BaseModel):
    build: str
