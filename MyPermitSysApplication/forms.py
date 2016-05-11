from RequestSysApplication.models import Position, Department
from django import forms
from django.core.validators import RegexValidator
from MyPermitSysApplication.models import *
from django.forms import ModelForm
class PersonForm(ModelForm):
    class Meta:

        model = Person
        fields = ['firstname', 'lastname', 'patronymic', 'passport_serial', 'passport_number', 'phone_number',
                  'position', 'department']