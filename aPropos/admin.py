from django.contrib import admin

# Register your models here.
from aPropos.models import APropos

class aProposAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return True
    def has_delete_permission(self, request, obj=None):
        return True
admin.site.register(APropos, aProposAdmin)