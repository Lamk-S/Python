from django.urls import path
from .views import HomeView, CustomerCreateView, CustomerDetailView

app_name = "core"

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('customer/create', CustomerCreateView.as_view(), name='customer_create'),
    path('customer/<int:pk>', CustomerDetailView.as_view(), name='customer_detail')
]