import json

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from .mixins import RequestLogViewMixin
from core.pagination import LargeResultsSetPagination


@api_view(('GET',))
def api_root(request, format=None):
    return Response({})
