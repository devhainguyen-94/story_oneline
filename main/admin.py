# admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Category
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name','role',
        )
    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2')
        }),
        ('Additional info', {
            'fields': ('role',)
        })
    )

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_by', 'created_at']  # Các trường bạn muốn hiển thị trong danh sách
    search_fields = ['name']  # Cho phép tìm kiếm theo tên
    list_filter = ['created_at']  # Bộ lọc dựa trên thời gian tạo

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Category, CategoryAdmin)