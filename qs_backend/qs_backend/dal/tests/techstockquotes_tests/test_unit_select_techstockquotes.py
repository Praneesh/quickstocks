#! /usr/bin/env python3

#   __author__    = "Praneesh Kataru"
#   __credits__   = []
#   __version__   = "0.1.1"
#   __maintainer__ = "Praneesh Kataru"
#   __email__ = "pranuvitmsse05@gmail.com"
#   __status__ = "Prototype"

import unittest
from pprint import pprint
from qs_backend.dal.tech_stock_quotes_dal import TechStockQuotesDAL


class TechStockQuotesTests(unittest.TestCase):
    """
        Unit Test Case for Validating ``TechStockQuotes`` table Selects
    """

    def setUp(self):
        self.stock_company_name = 'Honeywell International Inc.'
        self.stock_company_name_wrong = 'Honeywell International Inc.23'
        self.stock_company_key = 'HON'

    def tearDown(self):
        pass

    def test_db_tech_stock_pref_select_all(self):
        tech_stock_quotes_obj = TechStockQuotesDAL()
        print("Executing Test Case : Fetch All Tech Quotes")
        select_exception, all_tech_quotes = tech_stock_quotes_obj.get_all_tech_stocks()

        self.assertEqual(select_exception, None)
        self.assertGreater(all_tech_quotes.__len__(), 0, msg='Some records received')

    def test_db_tech_stockkey_company_title_positive(self):
        tech_stock_quotes_obj = TechStockQuotesDAL()
        print("Executing Test Case : Fetch Company Stock Key By  Company Name")
        select_exception, stock_key = tech_stock_quotes_obj.get_stock_quote_by_company_title(self.stock_company_name)
        self.assertEqual(select_exception, None)
        self.assertEqual(stock_key, self.stock_company_key)

    def test_db_tech_stockkey_company_title_negative(self):
        tech_stock_quotes_obj = TechStockQuotesDAL()
        print("Executing Test Case : Fetch Wrong Company Stock Key By  Company Name")
        select_exception, stock_key = tech_stock_quotes_obj.get_stock_quote_by_company_title(self.stock_company_name_wrong)
        self.assertEqual(select_exception, None)
        self.assertEqual(stock_key, None)