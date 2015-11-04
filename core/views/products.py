from rest_framework_mongoengine.generics import ListAPIView

from .mixins import RequestLogViewMixin
from core.serializers import ProductSerializer
from core.models import Product


class ProductsRetrieve(RequestLogViewMixin, ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
