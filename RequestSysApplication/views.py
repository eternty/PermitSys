from RequestSysApplication.ServiceLayer import *
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from RequestSysApplication.forms import RequestForm


# Create your views here.
def index(request):
    return render(request,'index.html')

def request_sys(request):
    #usertype = request.user.usertype.name

    context = RequestSystemSLRequest.request_sys(request)
    return render (request, 'req_system_requests.html', context)

def new_position(request):
    context = RequestSystemSLPosition.new_position(request)
    if context['error'] == 1:
        return HttpResponse("Error!")
    else:
        if context['method']=='post':
            return render(request, 'req_system_departs.html', context)
        else:
            return render(request, 'new_position.html', context)


def position(request,pk):
    context = RequestSystemSLPosition.position(request,pk)
    if context['error'] == 1:
        return HttpResponse("Error!")
    else:
        return render(request, 'new_position.html', context)


def position_delete(request,pk):
    context = RequestSystemSLPosition.position_delete(request, pk)
    return HttpResponseRedirect('/requestsystem/depart')


def department(request,pk):
    context = RequestSystemSLDepart.department(request,pk)
    if context['error'] == 1:
        return HttpResponse("Error!")
    else:
        return render(request, 'new_depart.html', context)


def new_depart(request):
    context = RequestSystemSLDepart.new_depart(request)
    if context['error'] == 1:
        return HttpResponse("Error!")
    else:
        if context['method'] == 'post':
            return render(request, 'req_system_departs.html', context)
        else:
            return render(request, 'new_depart.html', context)

def departs(request):
    context = RequestSystemSLDepart.departs(request)
    return render(request, 'req_system_departs.html', context)

def department_delete(request,pk):
    context = RequestSystemSLDepart.department_delete(request, pk)
    return HttpResponseRedirect('/requestsystem/depart')

def request(request,pk):
    context = RequestSystemSLRequest.request(request,pk)
    if context['error'] == 1:
        return HttpResponse("Error!")
    else:
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
    context = RequestSystemSLRequest.new_request(request)
    if context['error'] == 1:
        return HttpResponse("Error!")
    else:
        if context['method'] == 'post':
            return HttpResponseRedirect('/requestsystem/')
        if context['method'] == 'get':
            return render(request, 'new_request.html', context)

def request_proceed(request,pk,choice):
    RequestSystemSLRequest.request_proceed(request,pk,choice)
    return HttpResponseRedirect('/requestsystem/')



