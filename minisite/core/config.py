import logging
import sys

from loguru import logger
from munch import Munch
from starlette.config import Config
from starlette.datastructures import Secret

from ..core.logging import InterceptHandler

config = Config(".env")

API_PREFIX = ""
VERSION = "0.1.0"
DEBUG: bool = config("DEBUG", cast=bool, default=False)
SECRET_KEY: Secret = config("SECRET_KEY", cast=Secret, default="")

PROJECT_NAME: str = config("PROJECT_NAME", default="minisite")

# logging configuration
LOGGING_LEVEL = logging.DEBUG if DEBUG else logging.INFO
logging.basicConfig(
    handlers=[InterceptHandler(level=LOGGING_LEVEL)], level=LOGGING_LEVEL
)
logger.configure(handlers=[{"sink": sys.stderr, "level": LOGGING_LEVEL}])


def all():
    keys = list(config.environ.keys()) + list(config.file_values.keys())
    data = Munch()
    for key in keys:
        data[key] = config.get(key)
    return data
