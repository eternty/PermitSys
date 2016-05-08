import copy

from MyPermitSysApplication.classes import PermitSystemServiceLayer, PersonGateWay
from MyPermitSysApplication.models import Permit, Person
from django.shortcuts import render
from RequestSysApplication.models import MyRequest

def permit_sys(request):
    return render(request, 'permit_system_requests.html')

def permit(request):
    return render(request, 'new_permit.html')

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

def permit_console(request,pk,choice):
    reqobject = MyRequest.objects.get(id=pk)
    PermitSystemServiceLayer.parse(request, choice, reqobject)
    return PermitSystemServiceLayer.parse(request, choice, reqobject)

def person(request):
    return render(request, 'new_person.html')

def permit_sys_req(request):
    print(0)
    requests = MyRequest.objects.filter(status = 'APR')
    context={
        'requests':requests,
    }

    return render(request, 'permit_system_requests.html', context)


def permit_sys_permits(request):
    permits = Permit.objects.filter.all()
    print(1)
    context = {
        'permits': permits,
    }
    return render(request, 'permit_system_permits.html', context)

def permit_sys_persons(request):
    persons = Person.objects.filter.all()
    print(2)
    context = {
        'persons': persons,
    }
    return render(request, 'permit_system_persons.html', context)
