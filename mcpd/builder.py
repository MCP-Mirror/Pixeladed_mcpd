from typing import Protocol, Optional
from pydantic import BaseModel, Field


class BuildSpec(BaseModel):
    name: str
    tag: Optional[str] = Field(..., default="latest")
    dockerfile_content: str


class Builder(Protocol):
    def build(self, spec: BuildSpec) -> str:
        """Given a specification of an MCP server, create a Docker image locally and return it's tag"""
        ...
