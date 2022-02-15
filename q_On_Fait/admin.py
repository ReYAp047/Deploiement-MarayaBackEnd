from django.contrib import admin

# Register your models here.
from q_On_Fait.models import Q_On_Fait

class q_On_Fait(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return True
    def has_delete_permission(self, request, obj=None):
        return True
admin.site.register(Q_On_Fait, q_On_Fait)