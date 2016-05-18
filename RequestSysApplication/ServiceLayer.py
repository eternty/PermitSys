from RequestSysApplication.domain import PositionGateway,  RequestGateway, DepartGateway, MyRequestt, MyPosition, MyDepartment
from RequestSysApplication.forms import PositionForm, DepartmentForm, RequestForm, NewRequestForm
from RequestSysApplication.models import MyRequest, Department, Position
from RequestSysApplication.prototype import Prototype
from RequestSysApplication.values import kafedras, prot_for_kafedra


class RequestSystemSLPosition(object):
    @staticmethod
    def new_position(request):
        if request.method == "POST":
            form = PositionForm(request.POST)
            if form.is_valid():
                MyPosition.create(form)
                departs = DepartGateway.all()
                positions = PositionGateway.all()
                context = {
                    'departs': departs,
                    'positions': positions,
                    'method': 'post',
                    'error': 0,
                    'name_of_url': 'new_position'
                }
                return context
            else:
                context = {
                    'error': 1
                }
                return context

        else:
            position_form = PositionForm()
            context = {
                'form': position_form,
                'error': 0,
                'method': u'get',
                'name_of_url': u'new_position'
            }
            return context

    @staticmethod
    def position(request, pk):

        if request.method == 'POST':
            form = PositionForm(request.POST)
            if form.is_valid():
                position = MyPosition.find_by_id(pk)
                MyPosition.update_info(position, form)
                context = {
                    'form': form,
                    'error': 0,
                    'method': 'post',
                    'name_of_url': 'position'
                }
                return context

            else:
                context = {

                    'form': form,
                    'error': 1,
                    'name_of_url': 'position'
                }
                return context
        else:
            position_id = pk
            position = MyPosition.find_by_id(position_id)
            data = {
                'id': pk,
                'name': position.name,
                'info': position.info,

            }
            form = PositionForm(data)
            position.save()
            context = {

                'form': form,
                'id': pk,
                'error': 0,
                'method': 'get',
                'name_of_url': u'position'
            }
            return context

    @staticmethod
    def position_delete(request, pk):
        MyPosition.delete(pk)
        requests = MyRequestt.find_by_fields(position_id=pk)
        for req in requests:
            req.position_id = None
        return 1


class RequestSystemSLDepart(object):
    @staticmethod
    def new_depart(request):
        if request.method == "POST":
            our_form = DepartmentForm(request.POST)
            if our_form.is_valid():
                print('valid')
                number = our_form.cleaned_data['number']
                print(number)
                if number in kafedras:
                    print('need kaf')
                    prototype = Prototype()  # PROTOTYPE FOR Kafedra Department
                    prototype.register_object('kafedra', prot_for_kafedra)
                    phone_number = our_form.cleaned_data['phone_number']
                    depart_obj = prototype.clone('kafedra', number=number, phone_number=phone_number)
                    print(depart_obj.number)
                    print(depart_obj.phone_number)
                    print(depart_obj)
                    depart = MyDepartment(name=depart_obj.name, number=depart_obj.number, phone_number=depart_obj.phone_number, info=depart_obj.info)
                    depart.save()

                else:
                    print ('dont need kaf')
                    depart_obj = MyDepartment.creation(our_form)
                    #depart_obj.save()
                departs = Department.objects.all()
                positions = Position.objects.all()
                context = {
                    'departs': departs,
                    'positions': positions,
                    'error': 0,
                    'method': 'post',
                    'name_of_url': u'new_depart'
                }
                return context


            else:
                context = {
                    'error': 1,

                }
                return context

        else:
            depart_form = DepartmentForm()
            context = {
                'form': depart_form,
                'method': 'get',
                'error': 0,
                'name_of_url': u'new_depart'
            }
            return context

    @staticmethod
    def department(request, pk):
        depart_id = pk
        if request.method == 'POST':
            form = DepartmentForm(request.POST)

            if form.is_valid():
                depart = MyDepartment.find_by_id(depart_id)
                depart.update_info(form)
                context = {
                    'form': form,
                    'error': 0,
                    'method': 'post',
                    'name_of_url': u'depart'
                }
                return context

            else:
                context = {

                    'form': form,
                    'error': 1,
                    'name_of_url': u'depart'
                }
                return context
        else:

            depart = MyDepartment.find_by_id(depart_id)
            data = {
                'id': pk,
                'name': depart.name,
                'info': depart.info,
                'number': depart.number,
                'phone_number': depart.phone_number
            }
            form = DepartmentForm(data)
            depart.save()
            context = {
                'form': form,
                'id': pk,
                'error': 0,
                'method': 'get',
                'name_of_url': u'depart'
            }
            return context

    @staticmethod
    def departs(request):
        departs = Department.objects.all()
        positions = Position.objects.all()
        context = {
            'departs': departs,
            'positions': positions,
        }
        return context

    @staticmethod
    def department_delete(request, pk):
        department_id = pk
        depart = MyDepartment.find_by_id(department_id)
        MyDepartment.delete(depart)
        return 1


class RequestSystemSLRequest(object):
    def request_sys(request):
        # usertype = request.user.usertype.name
        requests = MyRequestt.all()
        for req in requests:
            req.position = MyPosition.find_by_id(req.position_id)
            depart = MyDepartment.find_by_id(req.department_id)
            if depart != None:
                req.depart = depart.full_name()
        context = {
            'requests': requests,
        }
        return context

    @staticmethod
    def request(request, pk):
        id=pk
        if request.method == 'POST':
            form = RequestForm(request.POST)
            our_request = MyRequestt.find_by_id(_id =pk)
            if form.is_valid():
                print(form.cleaned_data['department'])
                our_request.save()
                MyRequestt.update_info(our_request, form)
                req = MyRequest.objects.get(id = id)
                request_form = RequestForm(instance=req)
                context = {
                    'reqobject': our_request,
                    'form': request_form,
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
            reqobject = MyRequestt.find_by_id(_id=pk)
            our_form = RequestForm(instance=MyRequest.objects.get(id =id))
            context = {
                'reqobject': reqobject,
                'form': our_form,
                'error': 0,
                'method': 'get',
                'id': id

            }
        return context

    @staticmethod
    def request_creation(request, form):
        form = RequestForm(request.POST)
        if form.is_valid():
            our_request = RequestGateway.create(lastname =form.cleaned_data['lastname'], firstname =  form.cleaned_data['firstname'],
                            patronymic =form.cleaned_data['patronymic'],department = form.cleaned_data['department'],
                            position = form.cleaned_data['position'],end_date = form.cleaned_data['end_date'],
                            passport_number = form.cleaned_data['passport_number'],
                            passport_serial = form.cleaned_data['passport_serial'],
                            phone_number = form.cleaned_data['phone_number'],
                            status = form.cleaned_data['status'])
            our_request.save()
        else:
            return None

        return our_request

    @staticmethod
    def new_request(request):
        if request.method == "POST":
            form = NewRequestForm(request.POST)
            if form.is_valid():
                our_request = MyRequestt.creation(form)
                context = {
                    'reqobject': our_request,
                    'form': form,
                    'method': 'post',
                    'error':0,
                    'id': our_request.id

                }
                return context
            else:
                context = {

                    'error': 1
                }
                return context

        else:
            request_form = NewRequestForm()
            context = {
                'form': request_form,
                'method': 'get',
                'error':0
            }
            return context

    @staticmethod
    def request_proceed(request, pk, choice):
        reqobject = MyRequestt.find_by_id(_id=pk)
        #RequestServiceLayer.parse(choice, reqobject, pk)  # SERVICE LAYER
        if choice == u'delete':
            MyRequestt.deletion(pk)  # DOMAIN
        else:
            reqobject = MyRequestt.request_proceed(reqobject,choice)  # DOMAIN change status

        requests = MyRequest.objects.exclude(status="DON")
        context = {
            'requests': requests,
        }
        return context

