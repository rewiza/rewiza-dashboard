from django import template
from django.contrib.auth.hashers import check_password
from django.conf import settings


register = template.Library()

@register.filter
def uses_default_password(user):
    currentpassword = user.password
    matchcheck = check_password(settings.DEFAULT_ADMIN_PASSWORD, currentpassword)
    if matchcheck:
        return True
    return False
