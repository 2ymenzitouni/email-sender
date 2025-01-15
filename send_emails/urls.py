from django.contrib import admin
from django.urls import path ,include
from . import views
urlpatterns = [
    path('' , views.home , name = 'home'),
    path('send_emails/' , views.send_emails , name= 'send_emails'),
    path('contact_us/' , views.contact_us , name= 'contact_us'),
]
