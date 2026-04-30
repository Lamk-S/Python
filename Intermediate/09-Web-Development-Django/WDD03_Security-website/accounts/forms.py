from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
# Formularios para el perfil
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        # El email lo gestiona Allauth, así que solo dejamos editar nombres
        fields = ['first_name', 'last_name']
        labels = {
            'first_name': 'Nombre(s)',
            'last_name': 'Apellidos'
        }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']
        labels = {
            'avatar': 'URL de tu foto de perfil'
        }
        widgets = {
            'avatar': forms.URLInput(attrs={'placeholder': 'https://ejemplo.com/mifoto.jpg'})
        }