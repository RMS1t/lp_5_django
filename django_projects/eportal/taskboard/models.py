from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from eportal.taskboard.validators import SNPValidator, LoginValidator


class AdvUser(AbstractUser):
    pd_agree = models.BooleanField(blank=False, db_index=True,
                                   verbose_name='Consent to data processing')
    login = models.CharField(
        verbose_name='Login',
        max_length=255,
        help_text=_(
            "Required field. Enter Latin Login"
        ),
        validators=[LoginValidator],
        unique=False,
    )
    username = models.CharField(
        verbose_name='SNP(Surname Name Patronymic)',
        max_length=255,
        help_text=_(
            "Required field. Enter Cyrillic Surname First Name Patronymic"
        ),
        validators=[SNPValidator],
        unique=False,
    )
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.login

    class Meta(AbstractUser.Meta):
        pass


class OrderPetition(models.Model):
    pass


class Category(models.Model):
    pass