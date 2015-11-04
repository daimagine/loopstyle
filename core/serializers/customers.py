from rest_framework import serializers

from base import PublicModelSerializer
from core.models import Customer
from core import utils


class CustomerPublicSerializer(PublicModelSerializer):
    first_name = serializers.CharField(read_only=True,
                                       source='user.first_name')
    last_name = serializers.CharField(read_only=True,
                                      source='user.last_name')
    email = serializers.CharField(read_only=True,
                                  source='user.email')

    class Meta:
        model = Customer
        fields = ('id', 'first_name', 'last_name', 'mobile_num', 'email',
                  'profile_image', )


class CustomerStaffSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(read_only=True,
                                       source='user.first_name')
    last_name = serializers.CharField(read_only=True,
                                      source='user.last_name')

    class Meta:
        model = Customer
        fields = ('id', 'first_name', 'last_name', 'mobile_num')
