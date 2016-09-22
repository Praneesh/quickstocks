#! /usr/bin/env python3

#   __author__    = "Praneesh Kataru"
#   __credits__   = []
#   __version__   = "0.1.1"
#   __maintainer__ = "Praneesh Kataru"
#   __email__ = "pranuvitmsse05@gmail.com"
#   __status__ = "Prototype"

import json
from os import path


class UserStockPrefDAL:
    db_exception = None
    user_all_prefs = None

    def __init__(self):
        self.user_stock_pref_db_file = path.join(path.dirname(path.abspath(__file__)), 'database/UserStockPref.json')
        try:
            with open(self.user_stock_pref_db_file,'r') as json_data:
                self.user_all_prefs = json.load(json_data)
        except Exception as general_exception:
            self.db_exception = general_exception

    def get_all_user_preferences(self):
        """ Returns the stock interests of all users """
        return self.db_exception, self.user_all_prefs

    def get_all_stock_preferences(self):
        """Gets all the stocks that users are interested in.."""
        ret_all_stock_keys = set()
        available_user_prefs = self.user_all_prefs
        for user_preference in available_user_prefs:
            user_pref_stocks = user_preference["userStocks"]
            for stockItem in user_pref_stocks:
                ret_all_stock_keys.add(stockItem['key'])
        return self.db_exception, ret_all_stock_keys

    def get_stock_preferences_by_user_id(self, user_id):
        """ Returns the stock interests of a user """
        ret_user_pref = None
        ret_select_exception = None
        available_preferences = self.user_all_prefs
        for user_preference in available_preferences:
            if user_id == user_preference['userID']:
                ret_user_pref = user_preference
                break
        return ret_select_exception, ret_user_pref

    def get_users_by_stock_preference(self, stock_key):
        """Returns the list of users who are interested in a particular stock item"""
        ret_stock_pref_user_list = list()
        ret_select_exception = None
        available_preferences = self.user_all_prefs
        for user_preference in available_preferences:
            user_preferred_stocks = user_preference['userStocks']
            for stock in user_preferred_stocks:
                if stock['key'] == stock_key:
                    ret_stock_pref_user_list.append(user_preference['userID'])
                    break
        return ret_select_exception, ret_stock_pref_user_list

    def update_stock_preference_for_user(self, user_id, stock_key):
        """Updates the stock preference of a user"""
        ret_update_exception = None
        ret_update_status = False
        user_all_current_prefs = self.user_all_prefs
        for user_preference in user_all_current_prefs:
            if user_id == user_preference['userID']:
                # Create a new stock key object
                user_new_stock = dict()
                user_new_stock['key'] = stock_key

                # Update the existing stock key object - check for existence of an element before updatinng
                user_preference['userStocks'].append(user_new_stock)
                break;
        print(user_all_current_prefs)

        # Now open the file in write mode and dump into it.
        try:
            stock_pref_json_file = open(self.user_stock_pref_db_file, "w+")
            stock_pref_json_file.write(json.dumps(user_all_current_prefs))
            ret_update_status = True
            stock_pref_json_file.close()
        except Exception as general_exception:
            ret_update_exception = general_exception
        finally:
            return ret_update_exception, ret_update_status


