from django.urls import path, re_path
from . import views
from django.contrib.auth import login , logout
from django.contrib.auth.views import LoginView
from .views import UserUpdate , Success


urlpatterns = [
    path('', views.index, name='index'),
    path('login_success/', views.login_success, name='login_success'),
    path('test/', views.test, name='test'),
    path('doctor_list/', views.doctor_list, name='doctor_list'),
    path('doctor_home/', views.doctor_home, name='doctor_home'),
    path('receptionist_home/', views.receptionist_home, name='receptionist_home'),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('all_appointments/', views.all_appointments, name='all_appointments'),
    path('register/', views.UserFormView, name='register'),
    path('receptionist_register/', views.ReceptionistFormView, name='receptionist_register'),
    path('doctor_register/', views.DoctorFormView, name='doctor_register'),
    path('login/',views.login.as_view(template_name="home/login.html"),name='login'),
    re_path(r'^appointment/add$', views.AddAppointment, name='addappointment'),
    re_path(r'^appointment/(?P<pk>[0-9]+)/delete/$', views.AppointmentDelete, name='deleteappointment'),
    re_path(r'^appointment/(?P<pk>[0-9]+)/$', views.AppointmentUpdate, name='updateappointment'),
    re_path(r'^profile/edit/$',UserUpdate,name='user-update'),
    re_path(r'^profile/edit/success$', Success, name='success'),
    re_path(r'^logout/$',logout, {'next_page':'/index/login'}, name='logout'),
]
