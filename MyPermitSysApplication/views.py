from MyPermitSysApplication.ServiceLayer import PermitSystemServiceLayer, PermitSystemServiceLayerPerson, \
    PermitSystemSLRequests, PermitSystemSLPermits, PermitSystemSLPersons
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render



"""def permit_sys(request):
    return render(request, 'permit_system_requests.html')"""

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

    context = PermitSystemServiceLayer.show_createcont(choice, pk)
    if context['answer'] == 1:
        return render(request, 'request_for_permit.html', context)
    else:
        return render(request, 'print_permit.html', context)

def request_for_permit(request, pk):

    context = PermitSystemSLRequests.request_for_permit(pk)
    return render(request, 'request_for_permit.html', context)

def person(request,pk):
    context = PermitSystemServiceLayerPerson.person(request, pk)
    if context['error'] == 1:
        return HttpResponse("Error!")
    else:
        return render(request, 'person.html', context)

def temp_permit(request,pk):
    context = PermitSystemServiceLayer.temp_permit(request, pk)

    return render(request, 'print_permit.html', context)

def permit_sys_req(request):
    context = PermitSystemSLRequests.requests(request)
    return render(request, 'permit_system_requests.html', context)


def permit_sys_permits(request):
    context = PermitSystemSLPermits.permits(request)
    return render(request, 'permit_system_permits.html', context)


def permit_sys_persons(request):
    context = PermitSystemSLPersons.persons(request)
    return render(request, 'permit_system_persons.html', context)

def permits_of_person(request,pk):
    context = PermitSystemServiceLayerPerson.permits_of_person(pk)
    return render(request, 'permits_of_person.html', context)

def person_delete(request,pk):
    PermitSystemSLPersons.person_delete(pk)
    return HttpResponseRedirect('/permitsystem/permit_sys_persons')

def show_permit(request, pk):
    context = PermitSystemSLPermits.show_permit(request,pk)
    if context['error'] == 1:
        return HttpResponse("Error!")
    else:
        return render(request, 'permit.html', context)

def print_permit(request,pk):
    context = PermitSystemSLPermits.print_permit(pk)
    return render(request, 'print_permit.html',context)

def print(request,pk):
    context = PermitSystemSLPermits.print(request,pk)
    return HttpResponseRedirect('/permitsystem/permit_sys_permits')