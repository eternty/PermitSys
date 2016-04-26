from django.http import HttpResponse
from django.shortcuts import render
from RequestSysApplication.models import Request
from RequestSysApplication.forms import RequestForm

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

def depart(request):
    return render(request, 'main1.2.html')

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

def new_request(request):
    if request.method == "POST":
        our_form = RequestForm(request.POST)
        if our_form.is_valid():

            our_request = our_form.save(commit=False)
            our_request.save()

            pk = our_request.id
            return render(request, 'request.html', pk )
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
