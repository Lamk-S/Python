from django.shortcuts import render, get_object_or_404
from .models import Product

def index(request):
    products = Product.objects.all()        
    return render(request, "index.html", {'products':products})

def details(request, pk):
    product = get_object_or_404(Product, pk = pk)
    return render(request, "details.html", {'products':product})