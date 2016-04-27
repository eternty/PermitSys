from django.contrib import admin
from .models import *
# Register your models here.


class PositionAdmin(admin.ModelAdmin):
    list_display = ('name','info')


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name','phone_number')


class RequestAdmin(admin.ModelAdmin):
    list_display = (
    'lastname', 'firstname', 'patronymic', 'passport_serial', 'passport_number', 'position', 'department',
    'phone_number', 'registration_date', 'end_date', 'status')


admin.site.register(Position, PositionAdmin),
admin.site.register(Department, DepartmentAdmin),
admin.site.register(MyRequest, RequestAdmin)