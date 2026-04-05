from django.urls import path
from .views import register_view, home_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('', home_view, name='home')
]