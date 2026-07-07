from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import filters
from .models import Producto
from .serializers import ProductoSerializer, UserRegisterSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

class HelloView(APIView):

    def get(self, request):
        return Response({
            "message": f"Bienvenido {request.user.username}"
        })
    
class ProductoListCreateView(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["nombre"]
    ordering_fields = ["precio", "stock", "fecha_creacion"]
    ordering = ["nombre"]
    filterset_fields = ["stock"]

class ProductoDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer