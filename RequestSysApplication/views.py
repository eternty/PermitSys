from django.shortcuts import render
from RequestSysApplication.models import Request

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

def request(request):
    return render(request, 'new_request.html')

def person(request):
    return render(request, 'new_person.html')

def permit_sys_req(request):
    return render(request, 'main2.1.html')

def permit_sys_permits(request):
    return render(request, 'main2.2.html')

def permit_sys_persons(request):
    return render(request, 'main2.3.html')
