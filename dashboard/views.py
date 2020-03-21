from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core import management
from django.conf import settings
import requests
from .models import Service
from .utils import trigger_gitlab_job


def home(request):
    return render(request, 'dashboard/home.html')

@login_required
def profile(request):
    return render(request, 'dashboard/profile.html')

def service_auth_check(request):
    if request.user.is_authenticated:
        return HttpResponse(status=200)
    else:
        return HttpResponseForbidden()

def service_list(request):
    context = {}
    context['services'] = Service.objects.all()
    return render(request, 'dashboard/service/service_list.html', context)

def idp_redirect(request, value):
    """Redirects to any path

    :param value: Path to redirect to
    :type value: string (required)

    :return: Http response redirect
    :rtype: Http response
    """
    path = request.path.replace("/idp/redirect/", "https://")
    return HttpResponseRedirect(path)

def db_backup(request):
    trigger_gitlab_job('echo')
    return HttpResponseRedirect(reverse_lazy('account_profile'))

def db_restore(request):
    trigger_gitlab_job('echo')
    return HttpResponseRedirect(reverse_lazy('account_profile'))

def media_backup(request):
    management.call_command('mediabackup', '--noinput', verbosity=0)
    return HttpResponseRedirect(reverse_lazy('account_profile'))

def media_restore(request):
    management.call_command('mediarestore', '--noinput', verbosity=0)
    return HttpResponseRedirect(reverse_lazy('account_profile'))
