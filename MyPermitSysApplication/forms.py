from RequestSysApplication.models import Position, Department
from django import forms
from django.core.validators import RegexValidator
from MyPermitSysApplication.models import *
from django.forms import ModelForm
class PersonForm(ModelForm):
    class Meta:

        model = Person
        fields = ['lastname','firstname',  'patronymic', 'passport_serial', 'passport_number', 'phone_number',
                  'position', 'department','is_active']
class PermitForm(ModelForm):
    class Meta:

        model= Permit
        fields = ['person', 'department', 'position',
                  'end_date',  'status', 'is_active']
