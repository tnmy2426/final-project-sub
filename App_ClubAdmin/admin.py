from django.contrib import admin
from .models import User, ClubAdmin
from django.contrib.auth.models import Group

# Register your models here.
admin.site.register(User)
# admin.site.register(Group)


# admin.site.register(ClubAdmin)