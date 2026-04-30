from django.urls import path
from allauth.account.views import SignupView
from .views import home_view, activity_view, profile_view

urlpatterns = [
    path('register/', SignupView.as_view(), name='register'),
    path('activity/', activity_view, name='activity'),
    path('profile/', profile_view, name='profile'),
    path('', home_view, name='home')
]