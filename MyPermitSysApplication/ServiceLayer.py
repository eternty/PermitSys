import datetime

from MyPermitSysApplication.forms import PersonForm, PermitForm
from MyPermitSysApplication.models import Person, Permit
from RequestSysApplication.classes import RequestGateway, PositionGateway, DepartGateway
from RequestSysApplication.models import MyRequest, Position, Department
from MyPermitSysApplication.classes import PersonGateway, PersonGateWay, TemporaryPermitEmplementation, \
    ContinuousPermitEmplementation, PermitGateway


class PermitSystemServiceLayer(object):               #SERVICE_LAYER
    @staticmethod
    def show_createcont(choice, pk):
        reqobject = RequestGateway.find_by_id(_id=pk)
        print(reqobject.lastname)
        if choice == u'show':
            print(0)
            reqobject.department = DepartGateway.find_by_id(reqobject.department_id).full_name()
            reqobject.position=PositionGateway.find_by_id(reqobject.position_id).name
            context = {
                'reqobject': reqobject,
                'answer': 1
            }
            return context

        if choice == u'createcont':               #ABSTRACT
            lastname = reqobject.lastname
            firstname = reqobject.firstname
            patronymic = reqobject.patronymic
            position_id = reqobject.position_id
            department_id = reqobject.department_id
            passport_serial = reqobject.passport_serial
            passport_number = reqobject.passport_number
            phone_number = reqobject.phone_number

            person = PersonGateway(lastname=lastname, firstname=firstname, patronymic=patronymic,
                                   position_id=position_id, department_id=department_id,
                                   passport_serial=passport_serial,
                                   passport_number=passport_number, phone_number=phone_number, is_active=True)
            person.save()

            position_id = person.position_id
            department_id = person.department_id

            permit = ContinuousPermitEmplementation.create_permit(person.id, reqobject.registration_date, reqobject.end_date,
                                                                  lastname, firstname, patronymic,
                                                             position_id, department_id)
            permit.position = PositionGateway.find_by_id(_id = permit.position_id).name
            permit.department = DepartGateway.find_by_id(_id= permit.department_id).full_name()

            reqobject.done()          #DOMAIN in request system

            context = {

                'permit': permit,
                'answer': u'cont'
            }
            return context
    @staticmethod
    def temp_permit(request,pk):
        person = PersonGateway.find_by_id(_id=pk)
        lastname = person.lastname
        firstname = person.firstname
        patronymic = person.patronymic
        registration_date = datetime.date.today()
        end_date = datetime.date.today()
        position_id = person.position_id
        department_id = person.department_id

        permit = TemporaryPermitEmplementation.create_permit(person.id, registration_date,
                                                              end_date,
                                                              lastname, firstname, patronymic,
                                                              position_id, department_id)
        permit.position = PositionGateway.find_by_id(_id=permit.position_id).name
        permit.department = DepartGateway.find_by_id(_id=permit.department_id).full_name()



        context = {

            'permit': permit,
            'answer': u'cont'
        }
        return context

class PermitSystemServiceLayerPerson(object):
    @staticmethod
    def permits_of_person(pk):
        person = PersonGateway.find_by_id(_id = pk)
        person.department = DepartGateway.find_by_id(_id= person.department_id).full_name()
        person.position = PositionGateway.find_by_id(_id = person.position_id).name
        permits = PermitGateway.find_by_fields(person = person)
        for permit in permits:
            permit.department = DepartGateway.find_by_id(_id= permit.department_id).full_name()
            permit.position = PositionGateway.find_by_id(_id = permit.position_id).name

        context = {
            'permits': permits,
            'person': person
        }
        return context


    @staticmethod
    def person(request, pk):
        if request.method == 'POST':
            form = PersonForm(request.POST)
            person = Person.objects.get(id=pk)
            if form.is_valid():

                person.lastname = form.cleaned_data['lastname']
                person.firstname = form.cleaned_data['firstname']
                person.patronymic = form.cleaned_data['patronymic']
                dep = form.cleaned_data['department']
                pos = form.cleaned_data['position']
                person.department = dep
                person.position = pos
                person.passport_serial = form.cleaned_data['passport_serial']
                person.passport_number = form.cleaned_data['passport_number']
                person.phone_number = form.cleaned_data['phone_number']
                person.save()

                new_form = PersonForm(instance = person)

                context = {
                    'form': new_form,
                    'error':8,
                    'method': 'post'

                }
                return  context

            else:
                context = {
                    'error': 1
                }
                return context
        else:
            person = PersonGateway.find_by_id(_id=pk)
            person.id = pk
            form = PersonForm(instance=Person.objects.get(id=pk))
            context = {
                'person':person,
                'form': form,
                'error':0,
                'method': 'get'
            }
            return  context


class PermitSystemSLRequests:

    @staticmethod
    def requests(request):
        requests = RequestGateway.all()
        for req in requests:
            req.position = PositionGateway.find_by_id(_id= req.position_id)
            depart = DepartGateway.find_by_id(_id = req.department_id)
            req.depart = depart.full_name()
        context = {
            'requests': requests,
        }
        return context

    @staticmethod
    def request_for_permit(id):
        req = RequestGateway.find_by_id(_id=id)


class PermitSystemSLPermits:
    @staticmethod
    def permits(request):
        permits = Permit.objects.all()
        context = {
            'permits': permits,
        }
        return context

    @staticmethod
    def print(request,pk):
        permit = PermitGateway.find_by_id(_id=pk)
        permit.status = u'PRI'
        permit.save()
        context = {
            'permit': permit,
        }
        return context


    @staticmethod
    def print_permit(pk):
        permit = PermitGateway.find_by_id(_id=pk)
        permit.position = PositionGateway.find_by_id(_id=permit.position_id).name
        permit.department = DepartGateway.find_by_id(_id=permit.department_id).full_name()
        permit.id= pk
        context = {
            'permit': permit,
        }
        return context

    @staticmethod
    def show_permit(request,pk):
        id = pk
        if request.method == 'POST':
            form = PermitForm(request.POST)
            permit = PermitGateway.find_by_id(_id=pk)
            if form.is_valid():
                permit.update_info(form)
                permit.save()
                perm= Permit.objects.get(id=id)

                permit_form = PermitForm(instance=perm)

                context = {
                    'permit': permit,
                    'form': permit_form,
                    'error': 0,
                    'method': 'post',
                    'id': id
                }
            else:
                context = {
                     'error': 1
                }
            return context
        else:
            permit = PermitGateway.find_by_id(_id=pk)
            permit_form = PermitForm(instance=Permit.objects.get(id=id))
            context = {
                'reqobject':  permit,
                'form':  permit_form,
                'error': 0,
                'method': 'get',
                'id': id

                }
            return context


class PermitSystemSLPersons:
    @staticmethod
    def persons(request):
        persons = PersonGateway.all()
        #for per in persons:
            #per.department = DepartGateway.find_by_id(per.department_id).full_name()
            #per.position = PositionGateway.find_by_id(per.position_id).name

        context = {
            'persons': persons,
        }
        return context

    @staticmethod
    def person_delete(pk):
        person = Person.objects.get(id=pk)
        permits = Permit.objects.filter(person=person)
        for per in permits:
            per.person = None
            per.status = u'OLD'
        Person.delete(person)

        return 1


b = PermitSystemSLRequests.requests(None)
a = 1 + 1
