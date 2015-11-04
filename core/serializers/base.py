from rest_framework import serializers


class PublicModelSerializer(serializers.ModelSerializer):
    id = serializers.CharField(max_length=100,
                               source='hashed_id',
                               read_only=True)
