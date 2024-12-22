from typing import Protocol, Optional
from mcpd.state import McpServer
from pydantic import BaseModel

class MCPServerSpec(BaseModel):
    """
    A specificaiton for an MCP server that can be run by an executor.
    """

    name: str
    package: str
    dockerfile_content: str
    env: dict[str, str]


class Executor(Protocol):
    def create_and_run(
        self, spec: MCPServerSpec, server_name: Optional[str]
    ) -> McpServer:
        """Run an MCP server with the given specification and environment variables"""
        ...

    def stop(self, server_name: str) -> McpServer:
        """Stop the MCP server with the given name"""
        ...

    def run(self, server_name: str) -> McpServer:
        """Run the MCP server with the given name"""
        ...
