import copy

from MyPermitSysApplication.classes import PermitSystemServiceLayer, PersonGateWay
from MyPermitSysApplication.models import Permit
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from RequestSysApplication.models import MyRequest, Department, Position
from RequestSysApplication.forms import RequestForm, NewRequestForm, PositionForm, PositionFForm
from RequestSysApplication.forms import DepartmentForm, DepForm
from RequestSysApplication.prototype import Prototype
from RequestSysApplication.classes import RequestServiceLayer, PositionGateWay, PositionGateway


# Create your views here.
def index(request):
    return render(request,'index.html')

def request_sys(request):
    #usertype = request.user.usertype.name
    requests = MyRequest.objects.exclude(status ="DON")
    context = {
        'requests': requests,
    }
    return render (request, 'req_system_requests.html', context)

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
                'positions': positions
            }
            return render(request, 'req_system_departs.html', context)
        else:
            return HttpResponse("Error!")

    else:
        position_form = PositionForm()
        context = {
            'form': position_form
        }
        return render(request, 'new_position.html', context)

def position(request,pk):

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
                'form': form
            }
            return render(request, 'position.html', context)

        else:
            return HttpResponse("Error!")
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
            #'name': position.name,
            #'info': position.info,
            'form': form,
            'id': pk
            }
        return render(request, 'position.html', context)
def position_delete(request,pk):
    position_id = pk
    position = PositionGateway.find_by_id(position_id)
    position.delete()
    return HttpResponseRedirect('/requestsystem/depart')

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
                prototype = Prototype()                                 #PROTOTYPE FOR Kafedra Department
                prototype.register_object('kafedra', kafedra)
                depart_obj = prototype.clone('kafedra', number = our_form.cleaned_data['number'],
                                             phone_number = our_form.cleaned_data['phone_number'])


            else:
                depart_obj = our_form.save(commit=False)
            depart_obj.save()
            departs = Department.objects.all()

            positions = Position.objects.all()
            context = {
                'departs': departs,
                'positions': positions
            }
            return render(request, 'req_system_departs.html', context)


        else:
            return HttpResponse("Error!")

    else:
        depart_form = DepartmentForm()
        context = {
            'form': depart_form
        }
        return render(request, 'new_depart.html', context)

def depart(request):
    departs = Department.objects.all()

    positions = Position.objects.all()
    context = {
        'departs': departs,
        'positions': positions
    }
    return render(request, 'req_system_departs.html', context)

def request(request,pk):
    if request.method== 'POST':
        our_request = MyRequest.objects.get(id=pk)
        our_form = RequestForm(request.POST)
        if our_form.is_valid():
            our_request.update_info(our_form)

            request_form = RequestForm(instance=our_request)
            context = {
                'reqobject': our_request,
                'form': request_form
            }
        else:
            return HttpResponse("Error!")
    else:
        reqobject = MyRequest.objects.get(id=pk)
        our_form = RequestForm(instance=reqobject)
        context={
            'reqobject': reqobject,
            'form': our_form
        }
    return render(request, 'request.html', context)

def request_creation(request, form):
    form = RequestForm(request.POST)
    if form.is_valid():
        our_request = form.save(commit=False)
        our_request.save()
    else:
        return None

    return our_request

def parse_form(request, our_form):
    lastname = our_form.cleaned_data['lastname'],
    firstname = our_form.cleaned_data['firstname'],
    patronymic = our_form.cleaned_data['patronymic'],
    department = our_form.cleaned_data['department'],
    position = our_form.cleaned_data['position'],
    passport_serial = our_form.cleaned_data['passport_serial'],
    passport_number = our_form.cleaned_data['passport_number'],
    phone_number = our_form.cleaned_data['phone_number'],
    end_date = our_form.cleaned_data['end_date']
    context = {
        'lastname': lastname,
        'firstname': firstname,
        'patronymic': patronymic,
        'passport_number': passport_number,
        'passport_serial': passport_serial,
        'phone_number': phone_number,
        'department': department,
        'position': position,
        'end_date': end_date
    }
    return context

def new_request(request):
    if request.method == "POST":
        our_form = NewRequestForm(request.POST)
        if our_form.is_valid():

            our_request = MyRequest.creation(our_form)
            context2 = {
                'reqobject': our_request,
                'form': our_form
            }
            return render(request, 'request.html', context2)
        else:
            HttpResponse ("Error!")

    else:
        request_form = NewRequestForm()
        context = {
            'form': request_form
        }
        return render(request, 'new_request.html', context)

def request_proceed(request,pk,choice):
    reqobject = MyRequest.objects.get(id = pk)
    RequestServiceLayer.parse(choice,reqobject,pk)               #SERVICE LAYER
    requests = MyRequest.objects.exclude(status="DON")
    context = {
        'requests': requests,
    }
    return HttpResponseRedirect('/requestsystem/')



