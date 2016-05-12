from django.conf.urls import url,patterns, include
from django.contrib import admin
from RequestSysApplication import views

urlpatterns = [

    url(r'^$', views.request_sys, name = "request_sys"),
    url(r'^request_sys$', views.request_sys, name="request_sys"),
    url(r'^depart?$', views.depart , name= "depart"),
    url(r'^new_depart?$', views.new_depart, name ="new_depart"),
    url(r'^new_request?$', views.new_request, name = "new_request"),
    url(r'^new_position?$', views.new_position, name = "new_position"),
    url(r'^request/(?P<pk>[0-9]+)/?$', views.request, name = "request"),
    url(r'^request_proceed/(?P<pk>[0-9]+)/(?P<choice>[a-z]+)?$', views.request_proceed, name = "request_proceed"),
    url(r'position_delete/(?P<pk>[0-9]+)?$', views.position_delete, name="position_delete"),
    url(r'^position/(?P<pk>[0-9]+)/?$', views.position, name = "position"),
    url(r'request_proceed/(?P<pk>[0-9]+)/(?P<choice>[a-z]+)/request_sys?$', views.request_sys, name="request_sys"),
]