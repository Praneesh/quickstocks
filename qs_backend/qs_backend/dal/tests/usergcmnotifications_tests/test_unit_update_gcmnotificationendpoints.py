#! /usr/bin/env python3

#   __author__    = "Praneesh Kataru"
#   __credits__   = []
#   __version__   = "0.1.1"
#   __maintainer__ = "Praneesh Kataru"
#   __email__ = "pranuvitmsse05@gmail.com"
#   __status__ = "Prototype"

import unittest
from pprint import pprint
from qs_backend.dal.user_gcm_notifications_dal import UserGCMNotificationEndpointsDAL


class UserGCMNotificationEndpointTests(unittest.TestCase):
    """
        Unit Test Case for Validating ``GCMNotificationEndpoints`` table Selects
    """

    def setUp(self):
        self.gcm_notification_endpoint_key = 'clQbfM537UE'
        self.gcm_notification_endpoint_url = 'APA91bGsnKHPzZDiLo4MB59iC8gHYUOk8J9I1Y3LgNwRv6zPVzH_kxgUATkGHAmFYYkmkhbyNmtj5Nt1d8lzSI4rptk3gnLLd9yjhMtMFqXulZtVbJ86HMmwnERFOJpi25lVCDzfQQJL'

    def tearDown(self):
        pass

    def test_db_insert_gcm_notification_endpoint(self):
        user_gcm_notification_obj = UserGCMNotificationEndpointsDAL()
        print("Executing Test Case : Insert GCM Notification Endpoint")
        update_exception, update_status = user_gcm_notification_obj.update_gcm_endpoints(self.gcm_notification_endpoint_key,
                                                                                         self.gcm_notification_endpoint_url)
        self.assertEqual(update_exception, None)
        self.assertEqual(update_status, True)