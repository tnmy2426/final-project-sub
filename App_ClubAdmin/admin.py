from django.contrib import admin
from .models import User, ClubAdmin
from .forms import CreateNewUser, UserChangeForm
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin 

User = get_user_model()

# Register your models here.


admin.site.site_header = 'Event Management System Administration'
admin.site.index_title = 'SUB Computing Club'
class UserAdmin(BaseUserAdmin):
    add_form = CreateNewUser
    form = UserChangeForm
    list_display = [ 'username', 'full_name', 'is_active', 'is_clubAdmin', 'is_volunteer', 'is_superuser' ]
    list_filter = ('is_active', 'is_superuser', 'is_clubAdmin', 'is_volunteer')

    fieldsets = (
        (None, {'fields': ('username', 'full_name', 'password','is_active','is_clubAdmin','is_volunteer')}),
        ('Permission', {'fields': ('is_superuser', 'is_staff', )})
    )

    add_fieldsets = (
        (None, {'fields': ('username', 'full_name', 'is_active', 'password1', 'password2', 'is_clubAdmin', 'is_volunteer')}),
        ('Permission', {'fields': ('is_superuser', 'is_staff',)})
    )

    ordering = ('username',)

admin.site.register(User, UserAdmin)

# admin.site.register(Group)
# admin.site.register(ClubAdmin)