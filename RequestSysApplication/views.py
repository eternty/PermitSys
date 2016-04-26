import copy

from django.http import HttpResponse
from django.shortcuts import render
from RequestSysApplication.models import Request, Department
from RequestSysApplication.forms import RequestForm, DepartmentForm, DepForm
from RequestSysApplication.prototype import Prototype

# Create your views here.
def index(request):
    return render(request,'index.html')

def request_sys(request):
    #usertype = request.user.usertype.name
    requests = Request.objects.exclude(status ="DON")
    context = {
        'requests': requests,
    }
    return render (request, 'main1.1.html', context)

def permit_sys(request):
    return render(request, 'main2.1.html')

def new_depart(request):
    if request.method == "POST":
        our_form = DepartmentForm(request.POST)

        new_obj = our_form.save(commit=False)
        if our_form.is_valid():
            if new_obj.number == u'ИУ1' or u'ИУ2' or u'ИУ3' or u'ИУ4' or u'ИУ5':

                kafedra = Department.objects.create()
                kafedra.name = u'Кафедра'
                kafedra.number = u'ИУ5'
                kafedra.phone_number = u'+4953453434'
                prototype = Prototype()                                 #PROTOTYPE FOR Kafedra Department
                prototype.register_object('kafedra', kafedra)
                depart_obj = prototype.clone('kafedra', number = new_obj.number,
                                             phone_number = new_obj.phone_number)


            else:
                depart_obj = our_form.save(commit=False)
            depart_obj.save()
            context = {
                'depart_obj': depart_obj,
                'form': our_form
            }
            return render(request, 'main1.2.html')
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
        our_request = Request.objects.get(id=pk)

        our_form = RequestForm(request.POST)
        if our_form.is_valid():
            our_request.firstname = our_form.cleaned_data['firstname']
            our_request.lastname = our_form.cleaned_data['lastname']
            our_request.patronymic = our_form.cleaned_data['patronymic']
            our_request.department = our_form.cleaned_data['department']
            our_request.position = our_form.cleaned_data['position']
            our_request.end_date = our_form.cleaned_data['end_date']
            our_request.passport_number = our_form.cleaned_data['passport_number']
            our_request.passport_serial = our_form.cleaned_data['passport_serial']
            our_request.phone_number = our_form.cleaned_data['phone_number']
            our_request.status = our_form.cleaned_data['status']
            our_request.save()
            request_form = RequestForm(instance=our_request)
            context = {
                'reqobject': our_request,
                'form': request_form
            }
        else:
            return HttpResponse("Error!")
    else:
        reqobject = Request.objects.get(id=pk)
        our_form = RequestForm(instance=reqobject)
        context={
            'reqobject': reqobject,
            'form': our_form
        }
    return render(request, 'request.html', context)

def creation(request, form):
    if request.method == "POST":
        our_form = RequestForm(request.POST)
        if our_form.is_valid():
            our_request = our_form.save(commit=False)
            our_request.save()
        else:
            return HttpResponse("Error!")

    return our_request

def new_request(request):
    if request.method == "POST":
        our_form = RequestForm(request.POST)
        if our_form.is_valid():

            our_request = our_form.save(commit=False)
            our_request.save()


            context = {
                'reqobject': our_request,
                'form': our_form
            }
            return render(request, 'request.html', context )
        else:
            return HttpResponse("Error!")

    else:
        request_form = RequestForm()
        context = {
            'form': request_form

        }
        return render(request, 'new_request.html',context)

def person(request):
    return render(request, 'new_person.html')

def permit_sys_req(request):
    return render(request, 'main2.1.html')

def permit_sys_permits(request):
    return render(request, 'main2.2.html')

def permit_sys_persons(request):
    return render(request, 'main2.3.html')
