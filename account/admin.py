from django.contrib import admin
from django.contrib.auth import get_user_model
from .forms import UserAdminChangeForm, UserAdminCreationForm

from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

User = get_user_model()


class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ['email', 'admin']
    list_filter = ['admin', 'staff', 'is_active']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Full Name', {'fields': ('full_name',)}),
        ('Permissions', {'fields': ('admin', 'staff', 'is_active',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2',)}
        ),
    )
    search_fields = ['email', 'fullname']
    ordering = ['email']
    filter_horizontal = ()

admin.site.register(User, UserAdmin)

admin.site.unregister(Group)