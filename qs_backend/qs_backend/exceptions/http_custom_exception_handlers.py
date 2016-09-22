#! /usr/bin/env python3

#   __author__    = "Praneesh Kataru"
#   __credits__   = []
#   __version__   = "0.1.1"
#   __maintainer__ = "Praneesh Kataru"
#   __email__ = "pranuvitmsse05@gmail.com"
#   __status__ = "Prototype"

from werkzeug.exceptions import NotFound, BadRequest, InternalServerError


class JSONNotFoundException(BadRequest):
    def __init__(self):
        super(JSONNotFoundException, self).__init__()
        self.message = 'Content-Type should be application/json'


class ResourceNotFoundException(NotFound):
    def __init__(self, resource_id):
        super(ResourceNotFoundException, self).__init__()
        self.message = 'Could not find a resource with id = {}'.format(resource_id)


class InternalServerException(InternalServerError):
    def __init__(self, exception_message):
        super(InternalServerException, self).__init__()
        self.message = exception_message

