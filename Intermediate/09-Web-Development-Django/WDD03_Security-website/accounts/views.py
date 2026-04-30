from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import LoginHistory
from .forms import UserUpdateForm, ProfileUpdateForm

@login_required
def home_view(request):
    return render(request, 'account/home.html')

@login_required
def activity_view(request):
    # Obtenemos los últimos 15 inicios de sesión del usuario actual
    logins = LoginHistory.objects.filter(user=request.user)[:15]
    return render(request, 'account/activity.html', {'logins': logins})

@login_required
def profile_view(request):
    if request.method == 'POST':
        # Instanciamos ambos formularios con los datos del POST y las instancias actuales
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, '¡Tu perfil ha sido actualizado exitosamente!')
            return redirect('profile')
            
    else:
        # Si es un GET, llenamos los formularios con los datos actuales del usuario
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'account/profile.html', context)