import abc
from django.http import HttpResponse, HttpResponseRedirect
from MyPermitSysApplication.models import  Person
from MyPermitSysApplication.gateway import Gateway
import datetime

class PermitAbstractFabric(metaclass=abc.ABCMeta):                                #ABSTRACTFABRIC

    @staticmethod
    @abc.abstractmethod
    def create_permit(person_id, begin, end,lastname,firstname,   patronymic,position_id, department_id):
        new_permit = PermitGateway(person_id = person_id, begin_date = datetime.datetime.now(),end_date = end, lastname = lastname, firstname = firstname,
                                   patronymic = patronymic, position_id = position_id, department_id = department_id, is_active = True, status = u'NEW', type = u'000' )
        new_permit.save()
        return new_permit

class TemporaryPermitEmplementation(PermitAbstractFabric):                 #ABSTRACTFABRIC
    @staticmethod
    def create_permit(person_id, begin, end,lastname,firstname,patronymic, position_id, department_id):
        new_permit = PermitGateway(person_id=person_id, begin_date = datetime.datetime.now(), end_date=end, lastname=lastname, firstname=firstname,
                                   patronymic=patronymic, position_id=position_id, department_id=department_id, is_active = True, status = u'NEW', type = u'000')
        new_permit.type = 'TEM'
        new_permit.save()

        return new_permit

class ContinuousPermitEmplementation(PermitAbstractFabric):               #ABSTRACTFABRIC
    @staticmethod
    def create_permit(person_id, begin, end, lastname, firstname, patronymic, position_id, department_id):
        new_permit = PermitGateway(person_id=person_id,begin_date = datetime.datetime.now(), end_date=end, lastname=lastname, firstname=firstname,
                                   patronymic=patronymic, position_id=position_id, department_id=department_id, is_active = True, status = u'NEW', type = u'000')
        new_permit.type = 'CON'
        new_permit.save()

        return new_permit

class PersonGateway(Gateway):
    TABLE_NAME = 'MyPermitSysApplication_person'
    FIELDS = {
        'id',
        'lastname',
        'firstname',
        'patronymic',
        'phone_number',
        'passport_serial',
        'passport_number',
        'position_id',
        'department_id',
        'is_active'
    }

    def update_info(self, our_form):
        self.lastname =  our_form.cleaned_data['lastname']
        self.firstname = our_form.cleaned_data['firstname']
        self.patronymic = our_form.cleaned_data['patronymic']
        dep = our_form.cleaned_data['department']
        pos = our_form.cleaned_data['position']
        self.department_id = dep.id
        self.position_id = pos.id
        self.passport_serial = our_form.cleaned_data['passport_serial']
        self.passport_number = our_form.cleaned_data['passport_number']
        self.phone_number = our_form.cleaned_data['phone_number']
        self.save()
        return self

class PermitGateway(Gateway):
    TABLE_NAME = 'MyPermitSysApplication_permit'
    FIELDS = {
        'id',
        'person_id',
        'begin_date',
        'end_date',
        'is_active',
        'lastname',
        'firstname',
        'patronymic',
        'position_id',
        'department_id',
        'status',
        'type'
    }
    def update_info(self, our_form):

        per = our_form.cleaned_data['person']
        self.person_id = per.id
        dep = our_form.cleaned_data['department']
        pos = our_form.cleaned_data['position']
        self.department_id = dep.id
        self.position_id = pos.id
        self.end_date = our_form.cleaned_data['end_date']
        self.status = our_form.cleaned_data['status']
        self.save()
        return self

