#! /usr/bin/env python3

#   __author__    = "Praneesh Kataru"
#   __credits__   = []
#   __version__   = "0.1.1"
#   __maintainer__ = "Praneesh Kataru"
#   __email__ = "pranuvitmsse05@gmail.com"
#   __status__ = "Prototype"

import unittest
from pprint import pprint
from qs_backend.dal.user_stock_pref_dal import UserStockPrefDAL


class UserStockPrefSelectTests(unittest.TestCase):
    """
        Unit Test Case for Validating ``UserStockPrefs`` table Selects
    """

    def setUp(self):
        self.user_id = 'praneesh'
        self.stock_key = 'HON'

        self.insert_key = 'YHOO'

    def tearDown(self):
        pass

    def test_db_user_stock_pref_select_all(self):
        user_stock_pref_obj = UserStockPrefDAL()
        print("Executing Test Case : Fetch All User Preferences")
        select_exception, all_user_prefs = user_stock_pref_obj.get_all_user_preferences()
        pprint(all_user_prefs)

        self.assertEqual(select_exception, None)
        self.assertGreater(all_user_prefs.__len__(), 0, msg='Some records received')

    def test_db_get_all_stock_preferences(self):
        user_stock_pref_obj = UserStockPrefDAL()
        print("Executing Test Case : Fetch All Users Stock Keys")
        select_exception, all_stock_keys = user_stock_pref_obj.get_all_stock_preferences()
        pprint(all_stock_keys)
        self.assertEqual(select_exception, None)
        self.assertGreater(all_stock_keys.__len__(), 0, msg='Some records received')

    def test_db_fetch_stock_pref_by_user_id(self):
        user_stock_pref_obj = UserStockPrefDAL()
        print("Executing Test Case : Fetch Stock Preferences By User ID: {}".format(self.user_id))
        select_exception, stock_prefs = user_stock_pref_obj.get_stock_preferences_by_user_id(user_id=self.user_id)
        pprint(stock_prefs)

        self.assertEqual(stock_prefs['userID'], self.user_id)
        self.assertEqual(select_exception, None)

    def test_db_fetch_users_by_stock_key(self):
        user_stock_pref_obj = UserStockPrefDAL()
        print("Executing Test Case : Fetch Stock Preferences By Stock Key : {}".format(self.stock_key))
        select_exception, user_prefs = user_stock_pref_obj.get_users_by_stock_preference(stock_key=self.stock_key)
        pprint(user_prefs)

        self.assertEqual(select_exception, None)