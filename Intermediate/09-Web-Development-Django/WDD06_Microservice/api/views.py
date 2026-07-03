from django.shortcuts import render
from .models import Producto
from .serializers import ProductoSerializer
from rest_framework import viewsets

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer