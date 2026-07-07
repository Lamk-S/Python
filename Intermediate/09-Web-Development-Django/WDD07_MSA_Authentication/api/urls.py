from django.urls import path
from .views import (
    HelloView,
    ProductoListCreateView,
    ProductoDetailView,
    RegisterView
)

urlpatterns = [
    path("hello/", HelloView.as_view(), name="hello"),
    path("register/", RegisterView.as_view(), name="register"),
    path("productos/", ProductoListCreateView.as_view(), name="productos"),
    path("producto/<int:pk>/", ProductoDetailView.as_view(), name="producto"),
]