#! /usr/bin/env python3

#   __author__    = "Praneesh Kataru"
#   __credits__   = []
#   __version__   = "0.1.1"
#   __maintainer__ = "Praneesh Kataru"
#   __email__ = "pranuvitmsse05@gmail.com"
#   __status__ = "Prototype"

from qs_backend.models.stock_model import StockModel
from qs_backend.dal.user_stock_pref_dal import UserStockPrefDAL
from qs_backend.decorators.temp.users_topic_manager import UserTopicManager


class StockPublishPayloadToDict:

    def __init__(self):
        self.user_stock_pref_dal = UserStockPrefDAL()
        pass

    def get_stock_payload_to_publish(self, stock_payload):
        stocks_to_publish_dict = dict()
        if type(stock_payload) is StockModel:
            stock_key = stock_payload.stock_unit
            # Step 1: Get the list of Users that prefer a Stock
            select_exception, stock_preference_users = self.user_stock_pref_dal.get_users_by_stock_preference(stock_key)
            if select_exception:
                # TO DO: Raise a custom exception here !
                pass
            stock_temp_user_index = 0
            for user in stock_preference_users:
                # Step 2: Iterate through the Users in the list and fetch their Publish URL
                stock_to_publish_dict = dict()
                stock_to_publish_dict['publish_queue'] = self.get_user_publish_queue(user_id=user)
                stock_to_publish_dict['stock_unit'] = stock_payload.stock_unit
                stock_to_publish_dict['stock_title'] = stock_payload.stock_title
                stock_to_publish_dict['stock_price'] = stock_payload.stock_price
                stock_to_publish_dict['stock_deviation'] = stock_payload.stock_deviation
                stock_to_publish_dict['stock_deviation_status'] = stock_payload.stock_deviation_status
                stock_to_publish_dict['stock_equity'] = stock_payload.stock_equity
                stock_to_publish_dict['stock_last_update_time'] = stock_payload.stock_last_update_time

                stock_to_publish_dict['stock_52wkrange'] = stock_payload.stock_52wkrange
                stock_to_publish_dict['stock_open'] = stock_payload.stock_open
                stock_to_publish_dict['stock_market_cap'] = stock_payload.stock_market_cap
                stock_to_publish_dict['stock_prev_close'] = stock_payload.stock_prev_close
                stock_to_publish_dict['stock_peratio_tte'] = stock_payload.stock_peratio_tte

                stocks_to_publish_dict[stock_temp_user_index] = stock_to_publish_dict
                stock_temp_user_index += 1
        return stocks_to_publish_dict

    def get_user_publish_queue(self, user_id):
        # This function does not belong here, should be a part of DAL
        user_topic_mgr_instance = UserTopicManager()
        user_topic = user_topic_mgr_instance.get_user_topic_endpoint(user_id=user_id)
        return user_topic
