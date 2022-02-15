from django.contrib import admin

# Register your models here.
from Email.models import Email

class emailAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
admin.site.register(Email, emailAdmin)