from django.contrib import admin

# Register your models here.
from Localisation.models import Localisation

class localisationAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Localisation, localisationAdmin)