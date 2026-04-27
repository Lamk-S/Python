from django.urls import path
from allauth.account.views import SignupView
from .views import home_view, activity_view

urlpatterns = [
    path('register/', SignupView.as_view(), name='register'),
    path('activity/', activity_view, name='activity'),
    path('', home_view, name='home')
]