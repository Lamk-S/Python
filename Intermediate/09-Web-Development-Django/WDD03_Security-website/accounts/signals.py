from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in

from allauth.socialaccount.signals import social_account_added, social_account_updated

from .models import Profile, LoginHistory # Importamos LoginHistory

from .models import Profile

# Crear Perfil automáticamente
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# Guardar datos de Google
@receiver(social_account_added)
@receiver(social_account_updated)
def populate_user_profile(request, sociallogin, **kwargs):
    user = sociallogin.user
    data = sociallogin.account.extra_data

    profile, _ = Profile.objects.get_or_create(user=user)

    # Nombre
    user.first_name = data.get('given_name', '')
    user.last_name = data.get('family_name', '')

    # Avatar
    profile.avatar = data.get('picture')

    user.save()
    profile.save()
    
# Historial de login
@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    if request:
        # Extraer la IP real del usuario
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        
        # Extraer el User-Agent (Navegador y Sistema Operativo)
        user_agent = request.META.get('HTTP_USER_AGENT', '')[:255]

        # Guardar en la base de datos
        LoginHistory.objects.create(
            user=user,
            ip_address=ip,
            user_agent=user_agent
        )