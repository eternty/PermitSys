from RequestSysApplication.classes import PositionGateway, RequestServiceLayer
from RequestSysApplication.forms import PositionForm, DepartmentForm, RequestForm, NewRequestForm
from RequestSysApplication.models import MyRequest, Department, Position
from RequestSysApplication.prototype import Prototype


class RequestSystemServiceLayer(object):
    @staticmethod
    def request_sys(request):
        # usertype = request.user.usertype.name
        requests = MyRequest.objects.exclude(status="DON")
        context = {
            'requests': requests,
        }
        return context


class RequestSystemSLPosition(object):
    @staticmethod
    def new_position(request):
        if request.method == "POST":
            form = PositionForm(request.POST)
            if form.is_valid():
                position_object = PositionGateway(name=form.cleaned_data['name'],
                                                  info=form.cleaned_data['info'])
                position_object.save()
                departs = Department.objects.all()
                positions = Position.objects.all()
                context = {
                    'departs': departs,
                    'positions': positions,
                    'method': 'post',
                    'error': 0
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
                'method': u'get'
            }
            return context

    @staticmethod
    def position(request, pk):

        if request.method == 'POST':
            form = PositionForm(request.POST)
            if form.is_valid():
                position_id = pk
                position = PositionGateway.find_by_id(position_id)
                position.name = form.cleaned_data['name']
                position.info = form.cleaned_data['info']
                position.save()
                context = {
                    # 'name': position.name,
                    # 'info': position.info,
                    'form': form,
                    'error': 0,
                    'method': 'post'
                }
                return context

            else:
                context = {

                    'form': form,
                    'error': 1
                }
                return context
        else:
            position_id = pk
            position = PositionGateway.find_by_id(position_id)
            data = {
                'id': pk,
                'name': position.name,
                'info': position.info
            }
            form = PositionForm(data)
            position.save()
            context = {
                # 'name': position.name,
                # 'info': position.info,
                'form': form,
                'id': pk,
                'error': 0,
                'method': 'get'
            }
            return context

    @staticmethod
    def position_delete(request, pk):
        position_id = pk
        position = PositionGateway.find_by_id(position_id)
        position.delete()
        return 1


class RequestSystemSLDepart(object):
    @staticmethod
    def new_depart(request):
        if request.method == "POST":
            our_form = DepartmentForm(request.POST)

            # new_obj = our_form.save(commit=False)
            if our_form.is_valid():
                if our_form.cleaned_data['number'] == u'ИУ1' or u'ИУ2' or u'ИУ3' or u'ИУ4' or u'ИУ5' or u'ИУ6':

                    kafedra = Department.objects.create()
                    kafedra.name = u'Кафедра'
                    kafedra.number = u'ИУ5'
                    kafedra.phone_number = u'+4953453434'
                    prototype = Prototype()  # PROTOTYPE FOR Kafedra Department
                    prototype.register_object('kafedra', kafedra)
                    depart_obj = prototype.clone('kafedra', number=our_form.cleaned_data['number'],
                                                 phone_number=our_form.cleaned_data['phone_number'])


                else:
                    depart_obj = our_form.save(commit=False)
                depart_obj.save()
                departs = Department.objects.all()

                positions = Position.objects.all()
                context = {
                    'departs': departs,
                    'positions': positions,
                    'error': 0,
                    'method': 'post'
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
                'error': 0
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


class RequestSystemSLRequest(object):
    @staticmethod
    def request(request, pk):
        if request.method == 'POST':
            our_request = MyRequest.objects.get(id=pk)
            our_form = RequestForm(request.POST)
            if our_form.is_valid():
                our_request.update_info(our_form)

                request_form = RequestForm(instance=our_request)
                context = {
                    'reqobject': our_request,
                    'form': request_form,
                    'error': 0,
                    'method': 'post'
                }
            else:
                context = {
                    'error': 1
                }
                return context
        else:
            reqobject = MyRequest.objects.get(id=pk)
            our_form = RequestForm(instance=reqobject)
            context = {
                'reqobject': reqobject,
                'form': our_form,
                'error': 0,
                'method': 'get'
            }
        return context

    @staticmethod
    def request_creation(request, form):
        form = RequestForm(request.POST)
        if form.is_valid():
            our_request = form.save(commit=False)
            our_request.save()
        else:
            return None

        return our_request

    @staticmethod
    def new_request(request):
        if request.method == "POST":
            form = NewRequestForm(request.POST)
            if form.is_valid():

                our_request = MyRequest.creation(form)
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
        reqobject = MyRequest.objects.get(id=pk)
        RequestServiceLayer.parse(choice, reqobject, pk)  # SERVICE LAYER
        if choice == u'delete':
            MyRequest.deletion(pk)  # DOMAIN
        else:
            reqobject.request_proceed(choice)  # DOMAIN

        requests = MyRequest.objects.exclude(status="DON")
        context = {
            'requests': requests,
        }
        return context

