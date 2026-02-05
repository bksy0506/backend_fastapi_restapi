from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("emp/",views.EmployeeListCreateAPIView.as_view() ),
    path("emp/<int:id>/",views.EmployeeUpdateDeleteAPIView.as_view() ),
]
