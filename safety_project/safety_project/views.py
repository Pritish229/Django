from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Try importing your Role and UserProfile models
try:
    from .role import Role
    from .user_profile import UserProfile
except (ImportError, ModuleNotFoundError):
    Role = None
    UserProfile = None


# 🧠 Dashboard - login required
@login_required(login_url='/login/')
def dashboard(request):
    roles = Role.objects.all()[:5] if Role is not None else []
    users = UserProfile.objects.select_related('role', 'user').all()[:10] if UserProfile is not None else []

    context = {
        'roles': roles,
        'users': users,
        'title': 'Safety App RBAC Dashboard',
    }
    return render(request, 'adminlte/dashboard.html', context)


# 🔐 Login page
def login_view(request):
    # If already logged in, redirect to dashboard
    if request.user.is_authenticated:
        return redirect('dashboard')

    return render(request, 'adminlte/login.html', {'title': 'Login'})
