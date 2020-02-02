"""
rewiza_services URL Configuration
"""

from django.contrib import admin
from django.urls import include, path, re_path
from dashboard import views as dashboard_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', include('dashboard.urls', namespace="dashboard")),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', dashboard_views.profile, name="account_profile"),
    path('v2/service/auth/', dashboard_views.service_auth_check),
    re_path(r'^idp/redirect/(?P<value>\w+)', dashboard_views.idp_redirect, name='idp_redirect'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
