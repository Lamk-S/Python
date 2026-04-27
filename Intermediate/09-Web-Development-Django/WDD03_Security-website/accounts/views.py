from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import LoginHistory

@login_required
def home_view(request):
    return render(request, 'account/home.html')

@login_required
def activity_view(request):
    # Obtenemos los últimos 15 inicios de sesión del usuario actual
    logins = LoginHistory.objects.filter(user=request.user)[:15]
    return render(request, 'account/activity.html', {'logins': logins})