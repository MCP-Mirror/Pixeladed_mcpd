from enum import Enum
from typing import Protocol, Optional
from pydantic import BaseModel


class McpServerStatus(str, Enum):
    RUNNING = "running"
    STOPPED = "stopped"


class McpServer(BaseModel):
    id: str
    image_tag: str
    status: McpServerStatus
    env: dict[str, str]


class StateManager(Protocol):
    """Responsible for storing the metadata about the state of the system, including what MCP servers are running."""

    def list(self) -> list[McpServer]: ...
    def get(self, id: str) -> Optional[McpServer]: ...
    def set(self, id: str, server: McpServer) -> None: ...
    def delete(self, id: str) -> None: ...
