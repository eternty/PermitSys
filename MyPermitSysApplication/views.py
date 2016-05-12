import copy

from MyPermitSysApplication.ServiceLayer import PermitSystemServiceLayer
from MyPermitSysApplication.classes import   PersonGateway
#from MyPermitSysApplication.forms import PersonForm
from MyPermitSysApplication.forms import PersonForm
from MyPermitSysApplication.models import Permit, Person
from django.http import HttpResponse
from django.shortcuts import render
from RequestSysApplication.models import MyRequest, Department, Position


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
    print(0)
    context = PermitSystemServiceLayer.parse(choice, pk)
    if context['answer'] == u'show':
        return render(request, 'request_for_permit.html', context)
    else:
        return render(request, 'permit.html', context)



def person(request,pk):

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
                'form': form
            }
            return render(request, 'position.html', context)

        else:
            return HttpResponse("Error!")
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
            #'name': position.name,
            #'info': position.info,
            'form': form,
            'id': pk
            }
        return render(request, 'position.html', context)

def permit_sys_req(request):

    requests = MyRequest.objects.filter(status = 'APR')
    context={
        'requests':requests,
    }

    return render(request, 'permit_system_requests.html', context)


def permit_sys_permits(request):
    permits = Permit.objects.all()
    context = {
        'permits': permits,
    }
    return render(request, 'permit_system_permits.html', context)

def permit_sys_persons(request):
    persons = Person.objects.all()
    context = {
        'persons': persons,
    }
    return render(request, 'permit_system_persons.html', context)
