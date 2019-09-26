from django.shortcuts import render
from django.http import HttpResponseForbidden, HttpResponse
from django.contrib.auth.decorators import login_required

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
    return render(request, 'dashboard/service/service_list.html')