from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class UserAdminConfig (UserAdmin):
    search_fields= ('email', 'first_name', 'last_name',  'is_staff')
    ordering = ['email']
    list_display = ('email', 'first_name', 'last_name',  'is_owner')

    fieldsets = (( None, { 'fields': ('email', 'first_name', 'last_name', 'is_owner')}),
                    ('Permissions', {'fields' : ('is_staff', 'is_active','is_superuser')}))
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )

admin.site.register(CustomUser, UserAdminConfig)