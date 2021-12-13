from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.contrib.postgres.fields import CICharField
from django.db import models
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    username_validator = ASCIIUsernameValidator()

    username = CICharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    email = models.EmailField(_('email address'), unique=True)

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        db_table = 'user'
