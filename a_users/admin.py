from django.contrib import admin

from a_users.models import *


admin.site.register(
    [
        Profile,
    ]
)
