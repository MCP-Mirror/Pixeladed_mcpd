import json
from pathlib import Path
from typing import Optional

from platformdirs import user_data_dir

from mcpd.config import APP_NAME, APP_AUTHOR
from .state import McpServer, StateManager

SERVERS_FILE = "servers.json"


class FileStateManager(StateManager):
    """File-based implementation of StateManager that persists state to the user's data directory."""

    @classmethod
    def from_user_data_dir(cls) -> "FileStateManager":
        """Create a FileStateManager from the user's data directory."""
        data_dir = Path(user_data_dir(APP_NAME, APP_AUTHOR))
        return cls(data_dir)
    
    def __init__(self, data_dir: Path | str):
        data_dir = Path(data_dir)
        data_dir.mkdir(parents=True, exist_ok=True)
        
        self.state_file = data_dir / SERVERS_FILE
        
        # Initialize empty state file if it doesn't exist
        if not self.state_file.exists():
            self._save_state({})
    
    def _load_state(self) -> dict[str, McpServer]:
        """Load the state from disk."""
        try:
            with open(self.state_file, 'r') as f:
                data = json.load(f)
                return {
                    name: McpServer.model_validate(server_data)
                    for name, server_data in data.items()
                }
        except (json.JSONDecodeError, FileNotFoundError):
            return {}

    def _save_state(self, state: dict[str, McpServer]) -> None:
        """Save the state to disk."""
        with open(self.state_file, 'w') as f:
            json.dump(
                {name: server.model_dump() for name, server in state.items()},
                f,
                indent=2
            )

    def list(self) -> list[McpServer]:
        return list(self._load_state().values())

    def get(self, name: str) -> Optional[McpServer]:
        return self._load_state().get(name)

    def set(self, name: str, server: McpServer) -> None:
        state = self._load_state()
        state[name] = server
        self._save_state(state)

    def delete(self, name: str) -> None:
        state = self._load_state()
        if name in state:
            del state[name]
            self._save_state(state) 