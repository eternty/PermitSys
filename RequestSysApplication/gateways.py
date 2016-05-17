from RequestSysApplication.domain import MyRequestt
from RequestSysApplication.gateway import Gateway

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
        MyRequestt.deletion(pk)
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
    def done(self):
        self.status = 'DON'
        self.save()
        return self

    @staticmethod
    def creation(form):
        depart = form.save()
        return depart


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