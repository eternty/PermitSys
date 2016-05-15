from MyPermitSysApplication.forms import PersonForm
from MyPermitSysApplication.models import Person, Permit
from RequestSysApplication.classes import RequestGateway, PositionGateway, DepartGateway
from RequestSysApplication.models import MyRequest, Position, Department
from MyPermitSysApplication.classes import PersonGateway, PersonGateWay, TemporaryPermitEmplementation, \
    ContinuousPermitEmplementation

class PermitSystemServiceLayer(object):               #SERVICE_LAYER
    @staticmethod
    def show_createcont(choice, pk):
        reqobject = RequestGateway.find_by_id(_id=pk)
        print(reqobject.lastname)
        if choice == u'show':
            context = {
                'reqobject': reqobject,
                'answer': u'show'
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
            context = {

                'permit': permit,
                'answer': u'cont'
            }
            return context


class PermitSystemServiceLayerPerson(object):
    @staticmethod
    def person(request, pk):
        if request.method == 'POST':
            form = PersonForm(request.POST)
            if form.is_valid():
                position_id = pk
                position = PersonGateway.find_by_id(position_id)
                position.name = form.cleaned_data['name']
                position.info = form.cleaned_data['info']
                position.save()
                context = {
                    # 'name': position.name,
                    # 'info': position.info,
                    'form': form,
                    'error': 0
                }
                return  context

            else:
                context = {
                    'error': 1
                }
                return context
        else:
            position_id = pk
            position = PersonGateway.find_by_id(position_id)
            data = {
                'id': pk,
                'name': position.name,
                'info': position.info
            }
            form = PersonForm(data)
            position.save()
            context = {
                # 'name': position.name,
                # 'info': position.info,
                'form': form,
                'id': pk,
                'error':0
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
class PermitSystemSLPersons:
    @staticmethod
    def persons(request):
        persons = Person.objects.all()
        context = {
            'persons': persons,
        }
        return context


b = PermitSystemSLRequests.requests(None)
a = 1 + 1
