from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('' , views.employee_list , name = 'employee_list'),
    path('employee/<int:pk>/' , views.employee_detail , name = 'employee_detail'),
    path('employee/new/' , views.employee_new , name = 'employee_new'),
]
