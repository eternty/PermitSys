from RequestSysApplication.gateways import *


class MyPosition(PositionGateway):
    @staticmethod
    def find_by_id(pk):
        position = PositionGateway.find_by_id(_id = pk)
        return position

    @staticmethod
    def update_info(position, form):

        position.name = form.cleaned_data['name']
        position.info = form.cleaned_data['info']
        position.save()
        return position

    @staticmethod
    def create(form):
        position_object = PositionGateway(name=form.cleaned_data['name'],
                                          info=form.cleaned_data['info'])

        position_object.save()
        return position_object


    @staticmethod
    def delete(pk):
        position_id = pk
        position = PositionGateway.find_by_id(_id = position_id)
        position.delete()
        return 1

    @staticmethod
    def all(cls):
        return RequestGateway.all()


class MyRequestt(RequestGateway):

    @staticmethod
    def save(req):
        req.save()
        return req

    @staticmethod
    def done(pk):
        req = MyRequestt.find_by_id(pk)
        req.status = u'DON'
        req.save()
        return req

    @staticmethod
    def deletion(pk):
        reqobject = RequestGateway.find_by_id(pk)
        reqobject.delete()
        return 0

    @staticmethod
    def request_proceed(reqobject, choice):
        if choice == u'approve':
            reqobject.status = u'APR'
        if choice == u'decline':
            reqobject.status = u'DEC'
        print(reqobject.status)
        reqobject.save()
        return reqobject

    @staticmethod
    def update_info(req,our_form):
        req.firstname = our_form.cleaned_data['firstname']
        req.lastname = our_form.cleaned_data['lastname']
        req.patronymic = our_form.cleaned_data['patronymic']
        dep = our_form.cleaned_data['department']
        pos = our_form.cleaned_data['position']
        req.department_id = dep.id
        req.position_id = pos.id
        req.end_date = our_form.cleaned_data['end_date']
        req.passport_number = our_form.cleaned_data['passport_number']
        req.passport_serial = our_form.cleaned_data['passport_serial']
        req.phone_number = our_form.cleaned_data['phone_number']
        req.status = our_form.cleaned_data['status']
        req.save()
        return req


class MyDepartment(DepartGateway):
    @staticmethod
    def find_by_id(pk):
        depart = DepartGateway.find_by_id(pk)
        return depart

    @staticmethod
    def update_info(depart, form):
        depart.update_info(form)     #DOMAIN
        return depart

    @staticmethod
    def create(our_form):
        depart_obj = DepartGateway(name=our_form.cleaned_data['name'], number=our_form.cleaned_data['number'],
                                   phone_number=our_form.cleaned_data['phone_number'],
                                   info=our_form.cleaned_data['info'])
        depart_obj.save()

        return depart_obj.save


    @staticmethod
    def delete(depart):
        depart.delete()
        return 1


    @staticmethod
    def all():
        pass








