# admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser

class CustomUserAdmin(UserAdmin):
#    list_display = (
#         'username', 'email', 'first_name', 'last_name','role'
#         )
    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2')
        }),
        ('Additional info', {
            'fields': ('role',)
        })
    )
 
admin.site.register(CustomUser, CustomUserAdmin)