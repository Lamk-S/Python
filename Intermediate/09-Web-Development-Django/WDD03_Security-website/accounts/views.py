from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user is not None:
                login(request, user)

            messages.success(request, f"Account created successfully for {username}")
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'account/register.html', {'form': form})

@login_required
def home_view(request):
    return render(request, 'account/home.html')