import json

from django.utils.dateparse import parse_datetime
from rest_framework.response import Response
from rest_framework.views import APIView

from .mixins import RequestLogViewMixin
from core.serializers import CustomerPublicSerializer

from core import utils


class CustomerProfileRetrieve(RequestLogViewMixin, APIView):

    def get(self, request, format=None):
        """
        Return the customer's profile.
        """
        serializer = CustomerPublicSerializer(request.user.customer)
        return Response(serializer.data)
