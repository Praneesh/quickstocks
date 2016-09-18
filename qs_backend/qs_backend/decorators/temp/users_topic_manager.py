#! /usr/bin/env python3

#   __author__    = "Praneesh Kataru"
#   __credits__   = []
#   __version__   = "0.1.1"
#   __maintainer__ = "Praneesh Kataru"
#   __email__ = "pranuvitmsse05@gmail.com"
#   __status__ = "Prototype"


class UserTopicManager:
    def __init__(self):
        self.__topic_users_dict = dict()
        self.__topic_users_dict['praneesh'] = u'com.quickstocks.publisher.praneesh'
        self.__topic_users_dict['restofworld'] = u'com.quickstocks.publisher.restofworld'

    def get_user_topic_endpoint(self, user_id):
        # Return a generic queue, when no identifier is found !
        if user_id in self.__topic_users_dict:
            return self.__topic_users_dict[user_id]
        else:
            return self.__topic_users_dict['restofworld']
