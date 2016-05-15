import datetime
from RequestSysApplication.models import MyRequest, Position
from RequestSysApplication.gateway import Gateway
from MyProject10Sem.utils import Connection


class PositionGateWay(object):                         #GATEWAY
    @staticmethod
    def create(name, info):
        new_position = Position()
        new_position.name = name
        new_position.info = info
        new_position.save()
        return new_position.id

    @staticmethod
    def delete(id):
        Position.objects.get(id = id).delete()
        return

    @staticmethod
    def get(id):
        position = Position.objects.get(id =id)
        fieldes = {
            'name': position.name,
            'info': position.info
        }
        return fieldes

    @staticmethod
    def update_info(id,name,info):
        position = Position.objects.get(id=id)
        position.name = name
        position.info = info
        position.save()
        return id

class DepartGateway(Gateway):
    TABLE_NAME = 'RequestSysApplication_department'
    FIELDS = {
        'id',
        'name',
        'number',
        'info',
        'phone_number'
    }

    def full_name(self):
        full_name = '%s %s' % (self.name, self.number)
        return full_name.strip()

    @staticmethod
    def creation(form):
        myrequest = form.save()
        return myrequest

    @staticmethod
    def deletion(pk):
        reqobject = RequestGateway.find_by_id(pk)
        # print(reqobject.id)
        reqobject.delete()
        # MyRequest.objects.get(id=req_id).delete()
        return 0

    def update_info(self, our_form):
        self.name = our_form.cleaned_data['name']
        self.number = our_form.cleaned_data['number']
        self.phone_number = our_form.cleaned_data['phone_number']
        self.info = our_form.cleaned_data['info']
        self.save()
        return self

class RequestGateway(Gateway):
    TABLE_NAME = 'RequestSysApplication_myrequest'
    FIELDS = {
        'id',
        'lastname',
        'firstname',
        'patronymic',
        'passport_serial',
        'passport_number',
        'phone_number',
        'registration_date',
        'end_date',
        'department_id',
        'position_id',
        'createtime',
        'status',

    }





    @staticmethod
    def creation(form):
        depart = form.save()
        return depart

    @staticmethod
    def deletion(pk):
        reqobject = RequestGateway.find_by_id(pk)
        #print(reqobject.id)
        reqobject.delete()
        #MyRequest.objects.get(id=req_id).delete()
        return 0

    def request_proceed(self, choice):
        if choice == u'approve':
            self.status = u'APR'
        if choice == u'decline':
            self.status = u'DEC'
        print(self.status)
        self.save()
        return self

    def update_info(self, our_form):

        self.firstname = our_form.cleaned_data['firstname']
        self.lastname = our_form.cleaned_data['lastname']
        self.patronymic = our_form.cleaned_data['patronymic']
        dep = our_form.cleaned_data['department']
        pos = our_form.cleaned_data['position']
        self.department_id = dep.id
        self.position_id = pos.id
        self.end_date = our_form.cleaned_data['end_date']
        self.passport_number = our_form.cleaned_data['passport_number']
        self.passport_serial = our_form.cleaned_data['passport_serial']
        self.phone_number = our_form.cleaned_data['phone_number']
        self.status = our_form.cleaned_data['status']
        self.save()
        return self

class PositionGateway(Gateway):
    TABLE_NAME = 'RequestSysApplication_position'
    FIELDS = {
        'id',
        'name',
        'info'
    }

    def update_info(self, our_form):
        self.name = our_form.cleaned_data['name']
        self.info = our_form.cleaned_data['info']
        self.save()
        return self

    @staticmethod
    def position_deletion(id):
        position = PositionGateway.find_by_id(_id=id)
        position.delete()





