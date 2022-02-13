from django.contrib import admin

# Register your models here.
from Actions.models import *

admin.site.register([Partonaire,FontImages ,Images, Videos, Actions])