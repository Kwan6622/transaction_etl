import yaml
from pathlib import Path

# Compute the absolute path to the project root (2 levels up from src/utils/config.py)
PROJECT_ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = PROJECT_ROOT / "config" / "settings.yaml"

def load_config():
    with open(CONFIG_PATH) as file:
        config = yaml.safe_load(file)
    
    # Make paths absolute
    if "paths" in config:
        for key, val in config["paths"].items():
            config["paths"][key] = str(PROJECT_ROOT / val)
    
    if "database" in config and "db_file" in config["database"]:
        config["database"]["db_file"] = str(PROJECT_ROOT / config["database"]["db_file"])
        
    return config

config = load_config()
