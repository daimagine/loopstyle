from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .mixins import RequestLogViewMixin
from core.serializers import ContractorSelfStaffSerializer


class ContractorProfileRetrieve(RequestLogViewMixin, APIView):

    def get(self, request, format=None):
        """
        Return the contractor's profile.
        """
        serializer = ContractorSelfStaffSerializer(request.user.contractor)
        return Response(serializer.data)
