from django.utils.decorators import decorator_from_middleware
from rest_framework.permissions import IsAuthenticated

from loopstyle.middlewares import RequestLogMiddleware
from .permissions import IsContractorAuthenticated


class RequestLogViewMixin(object):
    """
    Adds RequestLogMiddleware to any Django View by overriding as_view.
    """

    @classmethod
    def as_view(cls, *args, **kwargs):
        view = super(RequestLogViewMixin, cls).as_view(*args, **kwargs)
        view = decorator_from_middleware(RequestLogMiddleware)(view)
        return view


class ContractorViewMixin(object):
    permission_classes = (IsAuthenticated, IsContractorAuthenticated)

    @classmethod
    def as_view(cls, *args, **kwargs):
        view = super(ContractorViewMixin, cls).as_view(*args, **kwargs)
        view = decorator_from_middleware(RequestLogMiddleware)(view)
        return view
