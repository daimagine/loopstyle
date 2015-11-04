from django.contrib import admin

from base import LoopstyleUserAdmin
from core.models import Customer


class CustomerAdmin(LoopstyleUserAdmin):
    list_display = ('id', 'name', 'mobile_num', 'status', 'verified_email',
                    'verified_mobile', )


admin.site.register(Customer, CustomerAdmin)
