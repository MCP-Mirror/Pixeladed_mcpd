from typing import Protocol, Optional
from pydantic import BaseModel


class MCPPackage(BaseModel):
    name: str
    github_repo: Optional[str]
    default_dockerfile_content: Optional[str]
    env: dict[str, str]


class Registry(Protocol):
    """
    A registry of MCP packages, how to find and retrieve them. It is not responsible for installing them.
    """

    def get(self, name: str) -> MCPPackage: ...
    def lookup_github_repo(self, repo: str) -> Optional[MCPPackage]: ...
    def search(self, query: str) -> list[MCPPackage]: ...
