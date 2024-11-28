# synda/logger.py
import logging
from synda.config import LOG_LEVEL, LOG_FORMAT, LOG_FILE


def setup_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(LOG_LEVEL)

    formatter = logging.Formatter(LOG_FORMAT)

    file_handler = logging.FileHandler(LOG_FILE, encoding='utf-8')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.stream = open(1, 'w', encoding='utf-8', closefd=False)
    logger.addHandler(console_handler)

    return logger
    