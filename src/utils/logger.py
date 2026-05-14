from loguru import logger
import sys

logger.remove()

logger.add(
        sys.stdout,
        format = '{time} | {level} | {message}',
        level = "INFO"
        )

logger.add(
        "logs/etl.log",
        rotation="5 MB",
        format='{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}',
        level="INFO"
)