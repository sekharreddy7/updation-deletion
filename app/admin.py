from django.contrib import admin

# Register your models here.
from app.models import *
admin.site.register(Topic)
admin.site.register(cinema)
admin.site.register(acc_record)