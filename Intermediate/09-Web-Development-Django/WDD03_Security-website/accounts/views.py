from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages

# Vista para registrar un nuevo usuario
def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() # Guarda el nuevo usuario en la base de datos
            username = form.cleaned_data.get('username')
            messages.success(request, f"Usuario dado de alta {username}")
            return redirect('login') # Redirige a la página de login tras el registro
    else:
        form = UserRegisterForm()
    
    return render(request, 'accounts/register.html', {'form':form})