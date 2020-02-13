#!/bin/bash

script="
from django.contrib.auth import get_user_model

User = get_user_model()
superusers = User.objects.filter(is_superuser=True)

username = 'admin';
email = 'admin@rewiza.cz';
password = os.environ.get('ADMIN_PASSWORD')

if superusers.count() == 0:
    User.objects.create_superuser(username, email, password)
    print('Default superuser created.')
else:
    print('Superuser creation skipped.')
"
printf "$script" | python manage.py shell
