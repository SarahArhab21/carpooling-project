from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from datetime import datetime

# Health check
def health_check(request):
    return JsonResponse({
        'status': 'healthy',
        'service': 'booking-service',
        'timestamp': datetime.now().isoformat()
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('booking.urls')),
    path('health/', health_check, name='health'),  # ← AJOUTER CETTE LIGNE
]