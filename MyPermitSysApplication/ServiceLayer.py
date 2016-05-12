from MyPermitSysApplication.forms import PersonForm
from MyPermitSysApplication.models import Person, Permit
from RequestSysApplication.models import MyRequest, Position, Department
from MyPermitSysApplication.classes import PersonGateway, PersonGateWay, TemporaryPermitEmplementation, \
    ContinuousPermitEmplementation

class PermitSystemServiceLayer(object):               #SERVICE_LAYER
    @staticmethod
    def parse(choice, pk):
        reqobject = MyRequest.objects.get(id=pk)

        if choice == u'show':
            context = {
                'reqobject': reqobject,
                'answer': u'show'

            }
            return context
        else:
            lastname = reqobject.lastname
            firstname = reqobject.firstname
            patronymic = reqobject.patronymic
            passport_number = reqobject.passport_number
            person  = PersonGateway(lastname = lastname, firstname = firstname, patronymic = patronymic,
                                       position_id = reqobject.position_id, department_id = reqobject.department_id, passport_serial = reqobject.passport_serial,
                                       passport_number = passport_number, phone_number = reqobject.phone_number, is_active = True)
            person.save()

            begin = reqobject.registration_date
            end = reqobject.end_date
            lastname = person.lastname  # ROW DATA GATEWAY
            firstname = person.firstname
            patronymic = person.patronymic
            position_id = person.position_id
            department_id = person.department_id
            department = Department.objects.get(id = department_id)
            position = Position.objects.get(id = position_id)
            if choice == u'createtemp':                    #ABSTRACTFABRIC
                permit = TemporaryPermitEmplementation.create_permit(person.id, begin, end,lastname,firstname,patronymic,
                                                                     position_id, department_id)
                context = {

                    'permit': permit,
                    'answer': u'temp',
                    'department': department.get_name(),
                    'position': position.get_name()
                }
                return context

            if choice == u'createcont':
                permit = ContinuousPermitEmplementation.create_permit(person.id, begin, end, lastname, firstname, patronymic,
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
                    'error':0
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
        requests = MyRequest.objects.filter(status='APR')
        context = {
            'requests': requests,
        }
        return context

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
