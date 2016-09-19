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

        self._52wkrange = None
        self._open = None
        self._prev_close = None
        self._market_cap = None
        self._peratio_tte = None

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

    @property
    def stock_52wkrange(self):
        return self._52wkRange

    @stock_52wkrange.setter
    def stock_52wkrange(self, value):
        self._52wkRange = value

    @property
    def stock_open(self):
        return self._open

    @stock_open.setter
    def stock_open(self, value):
        self._open = value

    @property
    def stock_prev_close(self):
        return self._prev_close

    @stock_prev_close.setter
    def stock_prev_close(self, value):
        self._prev_close = value

    @property
    def stock_market_cap(self):
        return self._market_cap

    @stock_market_cap.setter
    def stock_market_cap(self, value):
        self._market_cap = value

    @property
    def stock_peratio_tte(self):
        return self._peratio_tte

    @stock_peratio_tte.setter
    def stock_peratio_tte(self, value):
        self._peratio_tte = value
