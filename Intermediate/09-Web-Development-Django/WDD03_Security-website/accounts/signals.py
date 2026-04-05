from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from allauth.socialaccount.signals import social_account_added, social_account_updated

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