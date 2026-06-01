from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('empleados/', include('core.urls')),
    path('', RedirectView.as_view(url='/empleados/', permanent=False)), 
]
