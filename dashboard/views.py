from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Service
from django.core import management

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
    path = request.path.replace("/idp/redirect/", "https://")
    return HttpResponseRedirect(path)

def db_backup(request):
    management.call_command('dbbackup', '--noinput', verbosity=0)
    return HttpResponseRedirect(reverse_lazy('account_profile'))

def db_restore(request):
    management.call_command('dbrestore', '--noinput', verbosity=0)
    return HttpResponseRedirect(reverse_lazy('account_profile'))

def media_backup(request):
    management.call_command('mediabackup', '--noinput', verbosity=0)
    return HttpResponseRedirect(reverse_lazy('account_profile'))

def media_restore(request):
    management.call_command('mediarestore', '--noinput', verbosity=0)
    return HttpResponseRedirect(reverse_lazy('account_profile'))
