from django.shortcuts import render
from .models import Producto
from .serializers import ProductoSerializer
from rest_framework import viewsets

class ProductoViewSet(viewsets.ModelViewSet):
    """
    retrive: Devuelve un producto específico.
    list: Devuelve todos los productos.
    create: Crea un nuevo producto.
    delete: Elimina un producto existente.
    partial_update: Actualiza parcialmente un producto existente.
    update: Actualiza un producto existente completamente.
    """
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer