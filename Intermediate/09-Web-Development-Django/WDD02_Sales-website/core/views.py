from django.views.generic.list import ListView
from .models import Customer

class HomeView(ListView):
    model = Customer
    template_name = "index.html"