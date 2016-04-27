import copy

from django.http import HttpResponse
from django.shortcuts import render,redirect
from RequestSysApplication.models import MyRequest, Department
from RequestSysApplication.forms import RequestForm, NewRequestForm
from RequestSysApplication.forms import DepartmentForm, DepForm
from RequestSysApplication.prototype import Prototype

# Create your views here.
def index(request):
    return render(request,'index.html')

def request_sys(request):
    #usertype = request.user.usertype.name
    requests = MyRequest.objects.exclude(status ="DON")
    context = {
        'requests': requests,
    }
    return render (request, 'main1.1.html', context)

def permit_sys(request):
    return render(request, 'main2.1.html')

def new_depart(request):
    if request.method == "POST":
        our_form = DepartmentForm(request.POST)

       # new_obj = our_form.save(commit=False)
        if our_form.is_valid():
            if our_form.cleaned_data['number'] == u'ИУ1' or u'ИУ2' or u'ИУ3' or u'ИУ4' or u'ИУ5':

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
            context = {
                'depart_obj': depart_obj,
                'form': our_form
            }
            return redirect(request, depart)


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
    context = {
        'departs': departs

    }
    return render(request, 'main1.2.html',context)

def permit(request):
    return render(request, 'new_permit.html')

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
    if choice==u'3':
        MyRequest.deletion(pk)
    else:
        reqobject.request_proceed(choice)

    requests = MyRequest.objects.exclude(status="DON")
    context = {
        'requests': requests,
    }
    return render(request,'main1.1.html', context)


def person(request):
    return render(request, 'new_person.html')

def permit_sys_req(request):
    return render(request, 'main2.1.html')

def permit_sys_permits(request):
    return render(request, 'main2.2.html')

def permit_sys_persons(request):
    return render(request, 'main2.3.html')
