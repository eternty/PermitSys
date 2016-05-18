from django.conf.urls import url
from MyPermitSysApplication import views



urlpatterns = [
    url(r'^permit_sys_control/(?P<pk>[0-9]+)/(?P<choice>[a-z]+)?$', views.permit_console, name="permit_console"),
    url(r'permit_sys_permits/?$', views.permit_sys_permits, name="permits"),
    url(r'permit_sys_persons/?$', views.permit_sys_persons, name="persons"),
    url(r'print/(?P<pk>[0-9]+)/', views.print, name="print"),
    url(r'new_permit?$', views.permit, name = "new_permit"),
    url(r'request_for_permit/(?P<pk>[0-9]+)', views.request_for_permit, name="request_for_permit"),
    url(r'permits_of_person/(?P<pk>[0-9]+)', views.permits_of_person, name="permits_of_person"),
    url(r'print_permit/(?P<pk>[0-9]+)', views.print_permit, name="print_permit"),
    url(r'person/(?P<pk>[0-9]+)', views.person, name="person"),
    url(r'person_delete/(?P<pk>[0-9]+)', views.person_delete, name="person_delete"),
    url(r'temp_permit/(?P<pk>[0-9]+)', views.temp_permit, name="temp_permit"),

    #url(r'new_person?$', views.person, name="new_person"),
    url(r'permit/(?P<pk>[0-9]+)', views.show_permit, name="show_permit"),
    url(r'$', views.permit_sys_req, name="permit_sys_req"),

    #url(r'^issue_subsystem?$', views.issue_subsystem)

]