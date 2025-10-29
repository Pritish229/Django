from django.shortcuts import render
# Import models from their actual modules; guard to avoid import-time crashes.
try:
	from .role import Role
	from .user_profile import UserProfile
except (ImportError, ModuleNotFoundError):
	Role = None
	UserProfile = None

def dashboard(request):
	roles = Role.objects.all()[:5] if Role is not None else []  # Example: Top 5 roles
	users = UserProfile.objects.select_related('role', 'user').all()[:10] if UserProfile is not None else []  # Example: Recent users
	context = {
		'roles': roles,
		'users': users,
		'title': 'Safety App RBAC Dashboard',
	}
	return render(request, 'adminlte/dashboard.html', context)