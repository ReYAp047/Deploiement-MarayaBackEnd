from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

# Register your models here.
from Facebook.models import Facebook
class facobookAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
admin.site.register(Facebook, facobookAdmin)