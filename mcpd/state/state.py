from enum import Enum
from typing import Protocol, Optional
from pydantic import BaseModel


class McpServerStatus(str, Enum):
    RUNNING = "running"
    STOPPED = "stopped"


class McpServer(BaseModel):
    name: str
    package: str
    docker_image_id: str
    container_id: str
    status: McpServerStatus
    env: dict[str, str]


class StateManager(Protocol):
    """Responsible for storing the metadata about the state of the system, including what MCP servers are running."""

    def list(self) -> list[McpServer]: ...
    def get(self, name: str) -> Optional[McpServer]: ...
    def set(self, name: str, server: McpServer) -> None: ...
    def delete(self, name: str) -> None: ...
