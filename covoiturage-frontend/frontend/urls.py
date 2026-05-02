from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.views import health_check  # ← AJOUTER CETTE IMPORT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('health/', health_check, name='health'),  # ← AJOUTER CETTE LIGNE
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)