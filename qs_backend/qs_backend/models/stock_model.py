#! /usr/bin/env python3

#   __author__    = "Praneesh Kataru"
#   __credits__   = []
#   __version__   = "0.1.1"
#   __maintainer__ = "Praneesh Kataru"
#   __email__ = "pranuvitmsse05@gmail.com"
#   __status__ = "Prototype"


class StockModel(object):

    def __init__(self):
        self._stock_unit = None
        self._stock_price = None
        self._stock_deviation = None
        self._stock_deviation_status = None
        self._stock_equity = None
        self._stock_last_update_time = None

    @property
    def stock_unit(self):
        return self._stock_unit

    @stock_unit.setter
    def stock_unit(self, value):
        self._stock_unit = value

    @property
    def stock_price(self):
        return self._stock_price

    @stock_price.setter
    def stock_price(self, value):
        self._stock_price = value

    @property
    def stock_deviation(self):
        return self._stock_deviation

    @stock_deviation.setter
    def stock_deviation(self, value):
        self._stock_deviation = value

    @property
    def stock_deviation_status(self):
        return self._stock_deviation_status

    @stock_deviation_status.setter
    def stock_deviation_status(self, value):
        self._stock_deviation_status = value

    @property
    def stock_equity(self):
        return self._stock_equity

    @stock_equity.setter
    def stock_equity(self, value):
        self._stock_equity = value

    @property
    def stock_last_update_time(self):
        return self._stock_last_update_time

    @stock_last_update_time.setter
    def stock_last_update_time(self, value):
        self._stock_last_update_time = value
