import abc
from django.http import HttpResponse, HttpResponseRedirect

from MyPermitSysApplication.models import Permit, Person
from MyProject10Sem.gateway import Gateway
class PersonGateWay(object):                                        #ROW DATA GATEWAY
    @staticmethod
    def create(reqobject):
        new_person=Person()
        new_person.lastname = reqobject.lastname
        new_person.firstname = reqobject.firstname
        new_person.patronymic = reqobject.patronymic
        new_person.phone_number = reqobject.phone_number
        new_person.passport_number = reqobject.passport_number
        new_person.passport_serial = reqobject.passport_serial
        new_person.department = reqobject.department
        new_person.position = reqobject.position
        new_person.save()
        return new_person.id

    @staticmethod
    def update(person,form):
        person.save()

    @staticmethod
    def get_by_id(id):
        person = Person.objects.get(id=id)
        info = {
            'lastname': person.lastname,
            'firstname': person.firstname,
            'patronymic': person.patronymic,
            'passport_serial': person.passport_serial,
            'passport_number': person.passport_number,
            'phone_number': person.phone_number,
            'department': person.department,
            'position': person.position,
        }
        return info

    @staticmethod
    def get_lastname(id):
        person = Person.objects.get(id=id)
        return person.lastname

    @staticmethod
    def get_firstname(id):
        person = Person.objects.get(id=id)
        return person.firstname

    @staticmethod
    def get_patronymic(id):
        person = Person.objects.get(id=id)
        return person.patronymic

    @staticmethod
    def get_department(id):
        person = Person.objects.get(id=id)
        return person.department.id

    @staticmethod
    def get_position(id):
        person = Person.objects.get(id=id)
        return person.position.id

class PermitAbstractFabric(metaclass=abc.ABCMeta):                                #ABSTRACTFABRIC

    @staticmethod
    @abc.abstractmethod
    def create_permit(person_id, begin, end,lastname,firstname,patronymic,position_id, department_id):
        new_permit = Permit.objects.create()
        new_permit.begin_date = begin
        new_permit.end_date = end
        new_permit.person_id = person_id
        new_permit.lastname = lastname
        new_permit.firstname = firstname
        new_permit.patronymic = patronymic
        new_permit.department_id = department_id
        new_permit.position_id = position_id
        new_permit.save()
        return new_permit

class TemporaryPermitEmplementation(PermitAbstractFabric):                 #ABSTRACTFABRIC
    @staticmethod
    def create_permit(id, begin, end,lastname,firstname,patronymic, position, department):
        new_permit = Permit()
        new_permit.begin_date = begin
        new_permit.end_date = end
        new_permit.person_id = id
        new_permit.type = 'TEM'
        new_permit.lastname = lastname
        new_permit.firstname = firstname
        new_permit.patronymic = patronymic
        new_permit.department_id = department
        new_permit.position_id = position
        new_permit.save()

        return new_permit

class ContinuousPermitEmplementation(PermitAbstractFabric):               #ABSTRACTFABRIC
    @staticmethod
    def create_permit(id, begin, end,lastname,firstname,patronymic, position, department):
        new_permit = Permit()
        new_permit.begin_date = begin
        new_permit.end_date = end
        new_permit.person_id = id
        new_permit.type = 'CON'
        new_permit.lastname = lastname
        new_permit.firstname = firstname
        new_permit.patronymic = patronymic
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
class PermitGateway(Gateway):
    TABLE_NAME = 'MyPermitSysApplication_permit'
    FIELDS = {
        'id',
        'person',
        'begin_date',
        'end_date',
        'is_active',
        'lastname',
        'firstname',
        'patronymic',
        'position',
        'department',
        'status',
        'type'
    }