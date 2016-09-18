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


class UserStockPrefUpdateTests(unittest.TestCase):
    """
        Unit Test Case for Validating ``UserStockPrefs`` table Updates
    """

    def setUp(self):
        self.update_key = 'YHOO'
        self.user_id = 'restofworld'

    def tearDown(self):
        pass

    def test_db_insert_stock_by_user_id(self):
        user_stock_pref_obj = UserStockPrefDAL()
        print("Executing Test Case : Insert Stock Preferences By User ID : {} : {} ".format(self.user_id,
                                                                                            self.update_key))
        update_exception, update_status = user_stock_pref_obj.update_stock_preference_for_user(user_id=self.user_id,
                                                                                               stock_key=self.update_key)

        self.assertEqual(update_exception, None)