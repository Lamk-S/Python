from django.urls import path
from .views import HomeView, CustomerCreateView, CustomerDetailView, CustomerDeleteView, CustomerUpdateView

app_name = "core"

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('customer/create', CustomerCreateView.as_view(), name='customer_create'),
    path('customer/detail/<int:pk>', CustomerDetailView.as_view(), name='customer_detail'),
    path('customer/delete/<int:pk>', CustomerDeleteView.as_view(), name='customer_delete'),
    path('customer/edit/<int:pk>', CustomerUpdateView.as_view(), name='customer_update')
]