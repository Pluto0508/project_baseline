import logging
import os
from dataclasses import dataclass
from pathlib import Path

@dataclass
class BaseConfig:
    PROJECT_NAME: str='MyProject'
    VERSION: str='0.0.0'

    DEBUG: bool=False
    TEST: bool=False
    LOG_LEVEL: int=logging.INFO

    BASE_DIR: str=os.path.dirname(os.path.dirname(__file__))
    LOG_DIR: str=os.path.join(BASE_DIR,"logs")

    API_TIMEOUT: int=30


