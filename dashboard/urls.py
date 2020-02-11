"""
rewiza_services dashboard URL Configuration
"""

from django.urls import path

from . import views

app_name = "dashboard"

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.service_list, name='service_list'),
    path('conf/db/backup', views.db_backup, name='db_backup'),
    path('conf/db/restore', views.db_restore, name='db_restore'),
    path('conf/media/backup', views.media_backup, name='media_backup'),
    path('conf/media/restore', views.media_restore, name='media_restore'),
]