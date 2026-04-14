from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('home')),

    # Allauth centraliza todo (Login, Social, MFA)
    path('accounts/', include('allauth.urls')),
    
    # Vistas personalizadas de la app accounts
    path('accounts/', include('accounts.urls')),

    # Auth clásico
    path('accounts/', include('django.contrib.auth.urls')),
]