from django.forms import ModelForm
from django import forms
from RequestSysApplication.models import *
from MyPermitSysApplication.models import *

class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = ['firstname', 'lastname', 'patronymic', 'passport_serial', 'passport_number', 'phone_number',
                'position','department', 'end_date', 'status']


class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'number', 'phone_number']

class DepForm(forms.Form):
    name = forms.CharField(label = u'Тип отдела',max_length=30)
    number = forms.CharField(label = u'Номер отдела', max_length = 20)
    phone_number = forms.CharField(label = u'Номер телефона', max_length = 15)

