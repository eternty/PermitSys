from django.forms import ModelForm
from RequestSysApplication.models import *
from MyPermitSysApplication.models import *

class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = ['firstname', 'lastname', 'patronymic', 'passport_serial', 'passport_number', 'phone_number',
                'position','department', 'end_date', 'status']

