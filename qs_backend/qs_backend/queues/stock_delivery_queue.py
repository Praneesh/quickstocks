#! /usr/bin/env python3

#   __author__    = "Praneesh Kataru"
#   __credits__   = []
#   __version__   = "0.1.1"
#   __maintainer__ = "Praneesh Kataru"
#   __email__ = "pranuvitmsse05@gmail.com"
#   __status__ = "Prototype"

import queue


class StockDeliveryQueue(object):
    _instance = None
    __stock_delivery_queue = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(StockDeliveryQueue, cls).__new__(cls, *args, **kwargs)
            cls.__stock_delivery_queue = queue.Queue(0)
        return cls._instance

    def get_queue(self):
        return self.__stock_delivery_queue