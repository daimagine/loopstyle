from rest_framework import serializers
from rest_framework.compat import unicode_to_repr

from .base import PublicModelSerializer
from core import utils
from core.models import Contractor


class CurrentContractorDefault(serializers.CurrentUserDefault):
    def set_context(self, serializer_field):
        self.contractor = serializer_field.context['request'].user.contractor

    def __call__(self):
        return self.contractor

    def __repr__(self):
        return unicode_to_repr('%s()' % self.__class__.__name__)


class ContractorPublicSerializer(PublicModelSerializer):
    first_name = serializers.CharField(read_only=True,
                                       source='user.first_name')
    last_name = serializers.CharField(read_only=True,
                                      source='user.last_name')

    class Meta:
        model = Contractor
        fields = ('first_name', 'last_name', 'mobile_num', 'rating',
                  'profile_image', )


class ContractorSelfStaffSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(read_only=True,
                                       source='user.first_name')
    last_name = serializers.CharField(read_only=True,
                                      source='user.last_name')
    email = serializers.CharField(read_only=True,
                                  source='user.email')

    class Meta:
        model = Contractor
        fields = ('first_name', 'last_name', 'mobile_num', 'rating',
                  'profile_image', 'balance', 'email', )
