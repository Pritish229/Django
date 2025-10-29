from django.contrib import admin
from .models import Role, Permission, UserProfile, RolePermission

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_at', 'updated_at']
    search_fields = ['name', 'description']
    list_filter = ['created_at']

@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_at', 'updated_at']
    search_fields = ['name', 'description']
    list_filter = ['created_at']

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'role', 'contact_no', 'gender', 'created_at', 'updated_at']
    list_filter = ['role', 'gender', 'created_at']
    search_fields = ['user__username', 'user__email', 'contact_no']

@admin.register(RolePermission)
class RolePermissionAdmin(admin.ModelAdmin):
    list_display = ['role', 'permission', 'created_at', 'updated_at']
    list_filter = ['role', 'created_at']