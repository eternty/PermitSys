import json

from RequestSysApplication.models import MyRequest
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("/")
            else:
                return HttpResponse("Disabled account!")
        else:
            return render(request, 'signin_page.html')

    else:
        return render(request, 'signin_page.html')

def logout_view(request):
    logout(request)
    return render(request,'logout.html')

@login_required(login_url='/signin')
def index(request):
    usertype = request.user.usertype.name
    if request.user.usertype.name == u'Оператор заявок':
        active_requests = MyRequest.objects.exclude(status__name = u'Завершена')

        context = {
            'requests': requests,
        }
        return render(request, 'engineer.html', context)

    elif request.user.usertype.name == u'Диспетчер':

        active_requestss = Request.objects.exclude(status__name = u'Завершена')
        requests = Request.objects.filter(status__name = u'Зарегистрирована')
        requests.order_by('-createtime','reqtype')
        myrequests = active_requestss.filter(engineer = request.user)
        context = {
            'requests': requests,
            'myrequests': myrequests,
            'usertype': usertype
        }
        return render(request, 'disp.html', context)

    elif request.user.usertype.name == u'Клиент':

        requests = Request.objects.filter(company=request.user.company)
        myrequests = Request.objects.filter(creator=request.user)
        context = {
            'requests': requests,
            'myrequests': myrequests,
            'usertype': usertype
        }
        return render(request, 'client.html', context)
    else:
        requests = Request.objects.exclude(status__name = u'Завершена')
        newrequests = Request.objects.filter(status__name = u'Зарегистрирована')
        context = {
            'requests': requests,
            'newrequests': newrequests,
            'usertype': usertype
        }
        return render(request, 'manager.html', context)
