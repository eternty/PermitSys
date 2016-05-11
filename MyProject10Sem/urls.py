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

from MyProject10Sem import views
from RequestSysApplication import views

urlpatterns = [
    #url(r'^signin/?$', views.signin),
    url(r'^$', views.index),
    url(r'^admin/', admin.site.urls),
    url(r'^requestsystem/', include('RequestSysApplication.urls')),
    url(r'^permitsystem/', include('MyPermitSysApplication.urls')),
   # url(r'^signin/?$', views.signin),
    #url(r'^logout/?$', views.logout_view),

]

