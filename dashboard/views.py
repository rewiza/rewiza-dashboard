from django.shortcuts import render
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Service

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
