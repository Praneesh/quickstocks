#! /usr/bin/env python3

#   __author__    = "Praneesh Kataru"
#   __credits__   = []
#   __version__   = "0.1.1"
#   __maintainer__ = "Praneesh Kataru"
#   __email__ = "pranuvitmsse05@gmail.com"
#   __status__ = "Prototype"

import json
from os import path


class UserSubscriptionsDAL:
    db_exception = None
    user_subscriptions = None

    def __init__(self):
        self.user_subscription_db_file = path.join(path.dirname(path.abspath(__file__)), 'database/UserSubscriptions.json')
        try:
            with open(self.user_subscription_db_file, 'r') as json_data:
                self.user_subscriptions = json.load(json_data)
        except Exception as general_exception:
            self.db_exception = general_exception

    def get_subscription_url_by_user_id(self, user_id):
        """ Returns the subscription URL for stock quotes """
        if user_id in self.user_subscriptions:
            ret_subscribe_url = self.user_subscriptions[user_id]
        else:
            ret_subscribe_url = self.user_subscriptions['restofworld']
        return self.db_exception, ret_subscribe_url


