from django.contrib import admin
from django.urls import path, include
from main.views import  get_category, get_service

app_name = 'main'

urlpatterns = [
    # path('validation/',validator,name = 'validator'),
    # path('service/<int:id>/',get_service,name = 'get_service'),
    path('category/<slug:slug>/',get_service,name = 'get_service'),
    path('category/',get_category,name = 'get_category'),

]