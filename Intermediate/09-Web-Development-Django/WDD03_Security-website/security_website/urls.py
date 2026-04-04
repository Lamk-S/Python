from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')), # Incluir las rutas de la autenticación
    path('', include('django.contrib.auth.urls')), # Incluir las vistas predefinidas de auntenticación de django
]
