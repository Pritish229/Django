from django.db import models
from .role import Role
from .permission import Permission

class RolePermission(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.role.name} - {self.permission.name}"

    class Meta:
        verbose_name = "Role Permission"
        verbose_name_plural = "Role Permissions"
        unique_together = ['role', 'permission']