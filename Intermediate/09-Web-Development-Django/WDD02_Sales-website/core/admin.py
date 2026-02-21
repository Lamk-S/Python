from django.contrib import admin
from .models import Customer, Category, Product, Order, OrderDetails, Perfil, Supplier

admin.site.register([Customer, Category, Product, Order, OrderDetails, Perfil, Supplier])