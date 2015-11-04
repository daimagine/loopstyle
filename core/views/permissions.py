import logging
from rest_framework import permissions

logger = logging.getLogger(__name__)


class IsContractorAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            contractor = request.user.contractor
            logger.debug("Contractor access %s " %
                         contractor.name)
            return True
        except:
            return False
