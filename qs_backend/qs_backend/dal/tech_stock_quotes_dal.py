#! /usr/bin/env python3

#   __author__    = "Praneesh Kataru"
#   __credits__   = []
#   __version__   = "0.1.1"
#   __maintainer__ = "Praneesh Kataru"
#   __email__ = "pranuvitmsse05@gmail.com"
#   __status__ = "Prototype"

import json
from os import path


class TechStockQuotesDAL:
    db_exception = None
    tech_stock_quotes = None

    def __init__(self):
        self.tech_stock_quotes_db_file = path.join(path.dirname(path.abspath(__file__)), 'database/TechStockQuotes.json')
        try:
            with open(self.tech_stock_quotes_db_file, 'r') as json_data:
                self.tech_stock_quotes = json.load(json_data)
        except Exception as general_exception:
            self.db_exception = general_exception

    def get_all_tech_stocks(self):
        """ Returns the available stock ticks """
        return self.db_exception, self.tech_stock_quotes

    def get_stock_quote_by_company_title(self, company_title):
        """ Returns the stock title of a company """
        ret_stock_key = None
        if company_title in self.tech_stock_quotes:
            ret_stock_key = self.tech_stock_quotes[company_title]
        return self.db_exception, ret_stock_key


