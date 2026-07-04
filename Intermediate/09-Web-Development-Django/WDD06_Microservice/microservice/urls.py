from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]

# Rutas para la documentación de la API
urlpatterns += [
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='schema-swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='schema-redoc'),
    path('swagger.json', SpectacularAPIView.as_view(), name='schema'),
]