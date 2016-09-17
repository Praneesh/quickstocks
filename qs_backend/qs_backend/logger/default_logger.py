#! /usr/bin/env python3

#   __author__    = "Praneesh Kataru"
#   __credits__   = []
#   __version__   = "0.1.1"
#   __maintainer__ = "Praneesh Kataru"
#   __email__ = "pranuvitmsse05@gmail.com"
#   __status__ = "Prototype"

import logging
from logging.config import fileConfig
from os import path


class QSDefaultLogger(object):
    _instance = None
    __logging = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(QSDefaultLogger, cls).__new__(cls, *args, **kwargs)
            cls.__logging = cls.__create_logging(cls)
        return cls._instance

    def __create_logging(self):
        log_file_path = path.join(path.dirname(path.abspath(__file__)), 'defaultLoggingConfig.ini')
        logging.config.fileConfig(fname=log_file_path, disable_existing_loggers=False)

        return logging

    def get_logger(self, name):
        default_logging = self.__logging
        logger = default_logging.getLogger(name)
        return logger
