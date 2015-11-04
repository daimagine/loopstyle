from rest_framework_mongoengine.serializers import DocumentSerializer

from core.models import Product


class ProductSerializer(DocumentSerializer):
    class Meta:
        model = Product
        depth = 2
