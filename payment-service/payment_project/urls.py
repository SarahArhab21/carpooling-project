from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse, JsonResponse
from datetime import datetime

def home(request):
    return HttpResponse("""...""")  # Votre HTML ici

# Health check
def health_check(request):
    return JsonResponse({
        'status': 'healthy',
        'service': 'payment-service',
        'timestamp': datetime.now().isoformat()
    })

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/payments/', include('payments.urls')),
    path('health/', health_check, name='health'),  # ← AJOUTER CETTE LIGNE
]