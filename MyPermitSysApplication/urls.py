from django.conf.urls import url
from MyPermitSysApplication import views



urlpatterns = [
    url(r'permit_sys_control/(?P<pk>[0-9]+)/(?P<choice>[a-z]+)/?$', views.permit_console, name="requests_control"),
    url(r'permit_sys_permits/?$', views.permit_sys_permits, name="permits"),
    url(r'permit_sys_persons/?$', views.permit_sys_persons, name="persons"),
    url(r'$', views.permit_sys_req, name="permit_sys_req"),
    url(r'new_permit?$', views.permit, name = "new_permit"),
    #url(r'new_person?$', views.person, name="new_person"),


    #url(r'^issue_subsystem?$', views.issue_subsystem)

]