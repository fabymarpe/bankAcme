import logging
import os

from constants import LOG_DIR


class CustomFormatter(logging.Formatter):
    """ Custom Formatter does these 2 things:
    1. Overrides 'funcName' with the value of 'func_name_override', if it exists.
    2. Overrides 'filename' with the value of 'file_name_override', if it exists.
    """

    def format(self, record):
        if hasattr(record, 'func_name_override'):
            record.funcName = record.func_name_override
        if hasattr(record, 'file_name_override'):
            record.filename = record.file_name_override
        return super(CustomFormatter, self).format(record)


def get_logger(log_file_name):
    """ Creates a Log File and returns Logger object """
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    logPath = log_file_name if os.path.exists(log_file_name) else os.path.join(LOG_DIR, (str(log_file_name) + '.log'))

    logger = logging.Logger(log_file_name)
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(logPath, 'a+')
    handler.setFormatter(CustomFormatter('\n%(asctime)s - %(levelname)-10s - %(filename)s - %(funcName)s - %(message)s'))
    logger.addHandler(handler)

    # Return logger object
    return logger