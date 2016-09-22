#! /usr/bin/env python3

#   __author__    = "Praneesh Kataru"
#   __credits__   = []
#   __version__   = "0.1.1"
#   __maintainer__ = "Praneesh Kataru"
#   __email__ = "pranuvitmsse05@gmail.com"
#   __status__ = "Prototype"

from flask import jsonify, request
from qs_backend.dal.user_subscriptions_dal import UserSubscriptionsDAL
from qs_backend.dal.user_gcm_notifications_dal import UserGCMNotificationEndpointsDAL
from qs_backend.exceptions.http_custom_exception_handlers import *


class SubscriptionsAPI:
    def __init__(self):
        pass

    def register_qs_client(self, user_name):
        """
            Creates a subscription stream for accessing stock events
            ---
            tags:
              - Subscription
            responses:
              201:
                description: Returns an subscription object to receive stock events
        """

        # Create a unique session identifier for every client that calls this API
        # Create a publish URL for the same, update the object and return it.
        user_subscription_dict = dict()
        user_subscription_dal_obj = UserSubscriptionsDAL()
        fetch_exception, user_subscription = user_subscription_dal_obj.get_subscription_url_by_user_id(user_id=user_name)
        user_subscription_dict[user_name] = user_subscription
        if fetch_exception is not None:
            raise InternalServerException(exception_message=fetch_exception)
        return jsonify(user_subscription_dict)

    def update_gcm_notification_endpoint(self):
        """
            Updates a push notification stream for GCM endpoints
            ---
            tags:
              - Subscription
            responses:
              201:
                description: Returns status
        """

        user_gcm_notif_dal_obj = UserGCMNotificationEndpointsDAL()
        request_gcm_notif_endpoint = request.get_json()
        if request_gcm_notif_endpoint is None:
            raise JSONNotFoundException
        # To Do: Update the Notification Endpoint in DB
        return True

