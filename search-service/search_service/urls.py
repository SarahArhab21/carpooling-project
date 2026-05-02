"""
URL configuration for search_service project.
"""
from django.contrib import admin
from django.urls import include, path
from django.http import JsonResponse
from datetime import datetime

# Health check
def health_check(request):
    return JsonResponse({
        'status': 'healthy',
        'service': 'search-service',
        'timestamp': datetime.now().isoformat()
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('search.urls')),
    path('health/', health_check, name='health'),  # ← AJOUTER CETTE LIGNE
]