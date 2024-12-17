from typing import Protocol, Optional
from mcpd.state import McpServer


class Executor(Protocol):
    def create_and_run(
        self, spec_name: str, env: dict[str, str], server_name: Optional[str]
    ) -> McpServer:
        """Run an MCP server with the given specification and environment variables"""
        ...

    def stop(self, server_name: str) -> McpServer:
        """Stop the MCP server with the given name"""
        ...

    def run(self, server_name: str) -> McpServer:
        """Run the MCP server with the given name"""
        ...
