from django.contrib import admin
from Messages.models import Message
# Register your models here.
class aProposAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False

admin.site.register(Message, aProposAdmin)