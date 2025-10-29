# Avoid importing submodules at package import time to prevent ImportError when Django loads settings.
try:
	# Attempt to expose convenience names if submodules are available.
	from . import config
	from .role import Role
	from .permission import Permission
	from .user_profile import UserProfile
	from .role_permission import RolePermission
except (ImportError, ModuleNotFoundError):
	pass