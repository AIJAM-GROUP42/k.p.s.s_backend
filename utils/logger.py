import logging
from datetime import datetime

# Log formatı
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# Log ayarları
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format=LOG_FORMAT,
    datefmt=DATE_FORMAT
)

def log_info(message: str):
    logging.info(message)

def log_warning(message: str):
    logging.warning(message)

def log_error(message: str):
    logging.error(message)
