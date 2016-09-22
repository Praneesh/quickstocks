#! /usr/bin/env python3

#   __author__    = "Praneesh Kataru"
#   __credits__   = []
#   __version__   = "0.1.1"
#   __maintainer__ = "Praneesh Kataru"
#   __email__ = "pranuvitmsse05@gmail.com"
#   __status__ = "Prototype"
#
#   Step 1: Fetches the List of Subscribed Push Notification Clients
#   Step 2: Sends a notification to them in a set frequency regarding the stock ticks
#   To Do: Keep a track of stock changes, via an IPC - as soon as there is a change in stock, send a notification

import requests
import time
from qs_backend.dal.user_gcm_notifications_dal import UserGCMNotificationEndpointsDAL


class GoogleCloudMessageForwarderComponent:

    def __init__(self):
        pass

    def connect_pblish_gcm_message(self):

        # Step 1: Fetch all the GCM Notification Queue Endpoints - from qs-backend
        while True:
            gcm_push_endpoint = 'https://gcm-http.googleapis.com/gcm/send'

            # Headers
            gcm_push_headers = dict()
            gcm_push_headers["Authorization"] = "key=AIzaSyCMPx3wzGIObFxkASJ7mdu220_kwiEgWJM"
            gcm_push_headers["Content-Type"] = "application/json"

            # Payload
            destination_payload = dict()
            destination_payload_urls = list()

            # Fetch GCM Payloads
            user_gcm_notif_endpoints_obj = UserGCMNotificationEndpointsDAL()
            fetch_exception, gcm_endpoints = user_gcm_notif_endpoints_obj.get_all_gcm_endpoints()
            if fetch_exception is not None:
                break
            for endpoint in gcm_endpoints:
                endpoint_url = gcm_endpoints[endpoint]
                gcm_notif_url = endpoint + ":" + endpoint_url
                destination_payload_urls.append(gcm_notif_url)

            destination_payload["registration_ids"] = destination_payload_urls
            gcm_push_connection = requests.post(url=gcm_push_endpoint,
                                                json=destination_payload,
                                                headers=gcm_push_headers)
            print("Push Delivered To Web App {} at {}".format(gcm_push_connection.status_code, time.localtime()))
            time.sleep(300) # Deliver a push message once in 5 mins !


if __name__ == '__main__':
    gcm_forwarder_instance = GoogleCloudMessageForwarderComponent()
    gcm_forwarder_instance.connect_pblish_gcm_message()