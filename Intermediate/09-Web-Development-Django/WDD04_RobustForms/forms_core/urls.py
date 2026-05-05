from django.urls import path
from . import views


urlpatterns = [
    path('', views.procesar_pago_view, name='procesar_pago'),
]