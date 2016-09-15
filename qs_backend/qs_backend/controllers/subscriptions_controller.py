#! /usr/bin/env python3

#   __author__    = "Praneesh Kataru"
#   __credits__   = []
#   __version__   = "0.1.1"
#   __maintainer__ = "Praneesh Kataru"
#   __email__ = "pranuvitmsse05@gmail.com"
#   __status__ = "Prototype"

from flask import jsonify


class SubscriptionsAPI:
    def __init__(self):
        pass

    def register_qs_client(self):
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

        sample_response = dict()
        sample_response['session_id'] = 'Test Session'
        return jsonify(sample_response)
