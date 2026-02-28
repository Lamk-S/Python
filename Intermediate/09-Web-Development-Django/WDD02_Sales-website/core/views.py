from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Customer
from django.urls import reverse_lazy

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
    
class CustomerDeleteView(DeleteView):
    model = Customer
    success_url = reverse_lazy('core:home')
    template_name='confirm_customer_delete.html'
    
class CustomerUpdateView(UpdateView):
    model = Customer
    template_name = 'customer_create.html'
    fields = ['name', 'email', 'phone', 'address', 'state']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['edit'] = True
        return context