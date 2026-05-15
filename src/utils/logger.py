from loguru import logger
import sys
import time
from contextlib import contextmanager
from src.utils.config import config, PROJECT_ROOT

# Load the logging level from settings.yaml
LOG_LEVEL = config.get("logging", {}).get("level", "INFO")

logger.remove()

logger.add(
        sys.stdout,
        format = '{time} | {level} | {message}',
        level = LOG_LEVEL
        )

logger.add(
        str(PROJECT_ROOT / "logs" / "etl.log"),
        rotation="5 MB",
        format='{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}',
        level=LOG_LEVEL
)

@contextmanager
def log_action_time(action_name):
    """Context manager to log the duration of an action to log.txt"""
    start_time = time.time()
    time_logger = logger.bind(time_log=True)
    time_logger.info(f"Starting action: {action_name}")
    try:
        yield
    finally:
        duration = time.time() - start_time
        time_logger.info(f"Completed action: {action_name} | Duration: {duration:.2f} seconds")