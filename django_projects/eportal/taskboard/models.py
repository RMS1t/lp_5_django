from django.db import models
from django.contrib.auth.models import AbstractUser


class AdvUser(AbstractUser):
    pd_agree = models.BooleanField(blank=False, db_index=True,
                                       verbose_name='Согласен на обработку данных?')
    SNP=

    class Meta(AbstractUser.Meta):
        pass
