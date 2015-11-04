from django.contrib import admin
from django.core import urlresolvers

from .base import LoopstyleUserAdmin
from core.models import Contractor


class ContractorAdmin(LoopstyleUserAdmin):
    list_display = ('id', 'name', 'mobile_num', 'tag', )
    readonly_fields = ('api_token', )


admin.site.register(Contractor, ContractorAdmin)
