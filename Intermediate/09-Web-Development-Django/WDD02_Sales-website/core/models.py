from django.db import models
from django.urls import reverse

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    state = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('core:home')

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    state = models.BooleanField(default=True)
    categories = models.ManyToManyField(Category, related_name='products')
    
    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    state = models.BooleanField(default=True)
    
    def __str__(self):
        return f'Pedido #{self.id} - Cliente: {self.customer.name}'
    
class OrderDetails(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    state = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.quantity} x {self.product.name}'
    
    def subtotal(self):
        return self.quantity * self.unit_price
    
class Perfil(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    birthdate = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Femenino')])
    preferences = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f'Perfil de {self.customer.name}'
    
class Supplier(models.Model):
    supp_code = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name