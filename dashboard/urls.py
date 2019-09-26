"""
rewiza_services dashboard URL Configuration
"""

from django.urls import path

from . import views

app_name = "dashboard"

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.service_list, name='service_list')
]