#! /usr/bin/env python3

#   __author__    = "Praneesh Kataru"
#   __credits__   = []
#   __version__   = "0.1.1"
#   __maintainer__ = "Praneesh Kataru"
#   __email__ = "pranuvitmsse05@gmail.com"
#   __status__ = "Prototype"

import json
from os import path


class UserGCMNotificationEndpointsDAL:
    db_exception = None
    user_all_gcm_endpoints = None

    def __init__(self):
        self.user_gcm_endpoints_db_file = path.join(path.dirname(path.abspath(__file__)), 'database/UserGCMNotificationEndpoints.json')
        try:
            with open(self.user_gcm_endpoints_db_file, 'r') as json_data:
                self.user_all_gcm_endpoints = json.load(json_data)
        except Exception as general_exception:
            self.db_exception = general_exception

    def get_all_gcm_endpoints(self):
        """ Returns the GCM endpoints available """
        return self.db_exception, self.user_all_gcm_endpoints

    def update_gcm_endpoints(self, gcm_key, gcm_url):
        """Updates a new GCM endpoint in the database"""
        ret_update_exception = None
        ret_update_status = False
        existing_gcm_endpoints = self.user_all_gcm_endpoints
        existing_gcm_endpoints[gcm_key] = gcm_url
        print(existing_gcm_endpoints)

        # Now open the file in write mode and dump into it.
        try:
            gcm_pref_json_file = open(self.user_gcm_endpoints_db_file, "w+")
            gcm_pref_json_file.write(json.dumps(existing_gcm_endpoints))
            ret_update_status = True
            gcm_pref_json_file.close()
        except Exception as general_exception:
            ret_update_exception = general_exception
        finally:
            return ret_update_exception, ret_update_status




