"""
rewiza_services URL Configuration
"""

from django.contrib import admin
from django.urls import include, path
from dashboard import views as dashboard_views

urlpatterns = [
    path('', include('dashboard.urls', namespace="dashboard")),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', dashboard_views.profile, name="account_profile"),
    path('v2/service/auth/', dashboard_views.service_auth_check)
]
