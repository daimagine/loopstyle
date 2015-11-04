from django.contrib import admin


class LoopstyleUserAdmin(admin.ModelAdmin):
    readonly_fields = ('api_token', )
