from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime

# Health check view
@csrf_exempt
def health_check(request):
    return JsonResponse({
        'status': 'healthy',
        'service': 'auth-service',
        'timestamp': datetime.now().isoformat()
    }, status=200)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('users.urls')),
    path('health/', health_check, name='health'),  # ← AJOUTEZ CETTE LIGNE
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)