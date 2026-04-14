from django.urls import path
from allauth.account.views import SignupView
from .views import home_view

urlpatterns = [
    path('register/', SignupView.as_view(), name='register'),
    path('', home_view, name='home')
]