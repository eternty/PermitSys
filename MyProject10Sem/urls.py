"""MyProject10Sem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,patterns, include
from django.contrib import admin

from RequestSysApplication import views
#from MyPermitSysApplication import views


urlpatterns = [
    #url(r'^signin/?$', views.signin),
    url(r'^$', views.index),
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^request_sys?$', views.request_sys),
    #url(r'^request/(?P<pk>[0-9]+)/request_sys?$', views.request_sys),
    url(r'^permit_sys?$', views.permit_sys),

    url(r'^depart?$', views.depart),
    url(r'^new_depart?$', views.new_depart),
    url(r'^new_request?$', views.new_request),
    url(r'^new_permit?$', views.permit),
    url(r'^new_person?$', views.person),
    url(r'^request/(?P<pk>[0-9]+)/?$', views.request),

    url(r'^permit_sys_req?$', views.permit_sys_req),
    url(r'^permit_sys_permits?$', views.permit_sys_permits),
    url(r'^permit_sys_persons?$', views.permit_sys_persons),
    #url(r'^issue_subsystem?$', views.issue_subsystem)

]
