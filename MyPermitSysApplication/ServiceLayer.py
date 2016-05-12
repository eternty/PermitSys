from MyPermitSysApplication.models import Person
from RequestSysApplication.models import MyRequest
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
            global person
            if PersonGateway.find_by_fields(lastname = lastname, firstname = firstname, patronymic = patronymic, passport_number = passport_number) is None:
                person  = PersonGateway(lastname = lastname, firstname = firstname, patronymic = patronymic,
                                       position_id = reqobject.position_id, department_id = reqobject.department_id, passport_serial = reqobject.passport_serial,
                                       passport_number = passport_number, phone_number = reqobject.phone_number, is_active = True)

                person.save()
            else:
                persons = Person.objects.filter(lastname=reqobject.lastname, firstname=reqobject.firstname, patronymic=reqobject.patronymic,
                                         passport_number=reqobject.passport_number).order_by(id)
                person = persons[0]
            begin = reqobject.registration_date
            end = reqobject.end_date
            lastname = person.lastname  # ROW DATA GATEWAY
            firstname = person.firstname
            patronymic = person.patronymic
            position_id = person.position_id
            department_id = person.department_id


            if choice == u'createtemp':                    #ABSTRACTFABRIC
                permit = TemporaryPermitEmplementation.create_permit(person.id, begin, end,lastname,firstname,patronymic,
                                                                     position_id, department_id)
                context = {

                    'permit': permit,
                    'answer': u'temp'
                }
                return context

            if choice == u'createcont':
                permit = ContinuousPermitEmplementation.create_permit(person.id, begin, end, lastname, firstname, patronymic,
                                                                  position, department)
                context = {

                    'permit': permit,
                    'answer': u'cont'
                }
                return context
