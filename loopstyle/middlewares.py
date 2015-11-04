import json
import logging
import pytz

from django.core.urlresolvers import reverse
from django.utils import timezone


logger = logging.getLogger(__name__)


class AdminTimezoneMiddleware(object):
    def process_request(self, request):
        if request.path.startswith(reverse('admin:index')):
            timezone.activate(pytz.timezone('Asia/Jakarta'))
        else:
            timezone.deactivate()


class RequestLogMiddleware(object):
    def process_request(self, request):
        self.request_body = request.body

    def process_response(self, request, response):
        content_type = response.get('content-type')
        if content_type == 'application/json':
            if getattr(response, 'streaming', False):
                response_body = '<<<Streaming>>>'
            else:
                response_body = response.content
        else:
            response_body = '<<<Not JSON>>>'

        log_data = {
            'request_body': self.request_body,
        }

        if request.user.is_anonymous():
            username = 'NONE'
        else:
            username = request.user.username

        extra = {
            'user': username,
            'requestmethod': request.method,
            'responsestatus': response.status_code,
            'requestpath': request.get_full_path(),
        }

        logger.info(json.dumps(log_data), extra=extra)

        return response
