from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.contrib.auth.models import User

class MySocialAccountAdapter(DefaultSocialAccountAdapter):

    def pre_social_login(self, request, sociallogin):
        """
        Se ejecuta antes de crear un usuario social.
        Aquí unificamos por email.
        """
        email = sociallogin.account.extra_data.get('email')

        if not email:
            return

        try:
            user = User.objects.get(email=email)
            # Vincula cuenta Google con usuario existente
            sociallogin.connect(request, user)
        except User.DoesNotExist:
            pass