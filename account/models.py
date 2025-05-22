from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from rest_framework.authtoken.models import Token

class User(AbstractUser):
    class UserRole(models.TextChoices):
        SIMPLE_USER = "simple_user", _("Simple User")
        ATTORNEY = "attorney", _("Attorney")
        OTHER = "other", _("Other")

    role = models.CharField(_('role'), max_length=125, choices=UserRole.choices, default=UserRole.SIMPLE_USER)

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.get_full_name()

    def get_token(self):
        token, created = Token.objects.get_or_create(user=self)
        return {
            "token": token.key,
            "user_id": self.pk,
            "role": self.role
        }