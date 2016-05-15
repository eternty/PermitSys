import datetime

from django.forms import ModelForm
from django import forms
from RequestSysApplication.models import *
from MyPermitSysApplication.models import *


class DepartmentForm(ModelForm):
    class Meta:

        model = Department
        fields = ['name', 'number', 'phone_number']


class DepForm(forms.Form):
    name = forms.CharField(label=u'Тип отдела', max_length=30)
    number = forms.CharField(label=u'Номер отдела', max_length=20)
    phone_number = forms.CharField(label=u'Номер телефона', max_length=15)

class PositionFForm(forms.Form):
    class Meta:

        model = Position
        fiels = [ 'name', 'info']

class RequestForm(ModelForm):

    class Meta:

        model = MyRequest
        fields = ['id','firstname', 'lastname', 'patronymic', 'passport_serial', 'passport_number', 'phone_number',
                  'position', 'department', 'end_date', 'status']

class NewRequestForm(ModelForm):

    class Meta:

        model = MyRequest
        fields = ['firstname', 'lastname', 'patronymic', 'passport_serial', 'passport_number', 'phone_number',
                  'position', 'department', 'end_date']

class PositionForm(forms.Form):
    id = forms.IntegerField(label=u'Номер')
    name = forms.CharField(label=u'Название должности', max_length=30)
    info = forms.CharField(label=u'Описание', max_length=200)

class RequestMyForm(forms.Form):
    id = forms.IntegerField(label=u'Номер')
    firstname = forms.CharField(label=u'Имя', max_length=20)
    lastname = forms.CharField(label=u'Фамилия', max_length=20)
    patronymic = forms.CharField(label='Отчество',max_length=20)
    passport_serial = forms.IntegerField(label=u'Серия паспорта')
    passport_number = forms.IntegerField(label=u'Номер паспорта')
    registration_date = forms.DateField(label=u'Дата создания заявки')
    end_date = forms.DateField(label=u'Срок действия пропуска')
    phone_number = forms.CharField(label=u'Номер телефона', max_length=15)
    department = forms.IntegerField(label=u'Отдел')
    position =forms.IntegerField( label = 'Должность')
    status = forms.CharField(label=u'Статус')

