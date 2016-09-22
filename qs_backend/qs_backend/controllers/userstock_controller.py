#! /usr/bin/env python3

#   __author__    = "Praneesh Kataru"
#   __credits__   = []
#   __version__   = "0.1.1"
#   __maintainer__ = "Praneesh Kataru"
#   __email__ = "pranuvitmsse05@gmail.com"
#   __status__ = "Prototype"

from flask import jsonify, request
from qs_backend.dal.user_stock_pref_dal import UserStockPrefDAL
from qs_backend.dal.tech_stock_quotes_dal import TechStockQuotesDAL
from qs_backend.exceptions.http_custom_exception_handlers import *


class UserstockController:
    def __init__(self):
        pass

    def update_stock_preference(self, user_name):
        """
            Updates stock preferences for a give user
            ---
            tags:
              - Stocks
            responses:
              201:
                description: Returns updated preferences
        """

        user_stock_pref_dal_obj = UserStockPrefDAL()
        tech_stock_quote_dal_obj = TechStockQuotesDAL()

        request_stock_pref = request.get_json()
        if request_stock_pref is None:
            raise JSONNotFoundException
        stock_company_title = request_stock_pref['stock_company']

        # Fetch the stock key
        fetch_exception, stock_key = tech_stock_quote_dal_obj.get_stock_quote_by_company_title(company_title=stock_company_title)
        if stock_key is None:
            raise ResourceNotFoundException(resource_id=stock_company_title)

        update_exception, update_status = user_stock_pref_dal_obj.update_stock_preference_for_user(user_id=user_name,
                                                                                                   stock_key=stock_key)
        if update_exception is not None:
            raise InternalServerError

        if update_status is False:
            raise InternalServerError

        fetch_exception, updated_stock_pref = user_stock_pref_dal_obj.get_stock_preferences_by_user_id(user_id=user_name)
        if fetch_exception is not None:
            raise InternalServerException(exception_message=fetch_exception)
        return jsonify(updated_stock_pref)


