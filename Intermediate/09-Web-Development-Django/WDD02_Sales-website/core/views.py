from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Customer

class HomeView(ListView):
    model = Customer
    template_name = "index.html"
    
class CustomerCreateView(CreateView):
    model = Customer
    template_name = 'customer_create.html'
    fields = ['name', 'email', 'phone', 'address', 'state']
    
class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customer_detail.html'