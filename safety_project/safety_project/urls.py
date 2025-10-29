from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import dashboard, login_view

urlpatterns = [
    # 🏠 Root = Dashboard (requires login)
    path('', dashboard, name='dashboard'),

    # 🔐 Login page
    path('login/', login_view, name='login'),

    # ⚙️ Django Admin
    path('admin/', admin.site.urls),
]

# 🖼️ Static + Media in dev mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)