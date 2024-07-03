from django.contrib import admin
from accounts.models import (
    CustomBaseUserManager,
    CustomUser,
    Profile,
)

admin.site.register(CustomUser)
admin.site.register(CustomBaseUserManager)
admin.site.register(Profile)
