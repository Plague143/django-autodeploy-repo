from django.contrib import admin
from django.urls import path
from django.http import JsonResponse

def health_check(request):
    return JsonResponse({'status': 'ok', 'service': 'django-app'})

def home(request):
    return JsonResponse({'message': 'Welcome to Django API', 'version': '1.0.0'})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', health_check, name='health'),
    path('', home, name='home'),
]
