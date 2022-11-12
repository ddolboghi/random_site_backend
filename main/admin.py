from atexit import register
from django.contrib import admin
from .models import Alldata, Result

admin.site.register(Alldata)
admin.site.register(Result)