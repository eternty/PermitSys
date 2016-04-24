from django.contrib import admin

# Register your models here.
from .models import *

class PersonAdmin(admin.ModelAdmin):
    list_display = ('lastname','firstname','patronymic', 'passport_serial', 'passport_number','position','department',
                     'phone_number', 'is_active')

class PermitAdmin(admin.ModelAdmin):
    list_display = ('person','begin_date','end_date', 'is_active', 'status', 'type')

admin.site.register(Permit, PermitAdmin),

admin.site.register(Person,PersonAdmin),

