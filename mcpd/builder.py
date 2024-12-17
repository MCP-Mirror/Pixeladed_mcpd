from typing import Protocol
from pydantic import BaseModel


class BuildSpec(BaseModel):
    github_repo: str


class Builder(Protocol):
    def build(self, spec: BuildSpec) -> str:
        """Given a specification of an MCP server, create a Docker image locally and return it's tag"""
        ...
