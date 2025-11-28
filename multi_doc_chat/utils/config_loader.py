from pathlib import Path
import yaml
import os

def _project_root() -> Path:
    return Path(__file__).resolve().parents[1]

def load_config(config_path: str | None = None) -> dict:
    """ 
    Helps us resolve the config path reliabliy and load the YAML config file. 
    Priority: explicit arg > CONFIG_PATH env var > <project_root>/config/config.yaml 
    """

    env_path = os.getenv("CONFIG_PATH")
    if config_path is None:
        config_path = env_path or str(_project_root() / "config" / "config.yaml")

    path = Path(config_path)

    if not path.is_absolute():
        path = _project_root() / path
    
    if not path.exists():
        raise FileNotFoundError(f"Config file not found at: {path}")
    
    with open(path, "r", encoding="utf8") as f:
        return yaml.safe_load(f) or {}