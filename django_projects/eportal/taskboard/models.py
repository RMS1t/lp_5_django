from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from taskboard.validators import LoginValidator, SNPValidator


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
        unique=True,
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

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.login

    class Meta(AbstractUser.Meta):
        pass


class OrderPetition(models.Model):
    """Model representing a Order."""

    class OrderStatus(models.TextChoices):
        NEW = "N", _("Новая заявка")
        PROCESSING = "W", _("Принято на обработку")
        FINISHED = "E", _("Выполнена")

    title = models.CharField(max_length=200)
    content = models.TextField(
        max_length=1000, help_text="Enter a  description of the yours order")
    # ManyToManyField used because a genre can contain many books and a Book can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    category = models.ForeignKey(
        'Category', on_delete=models.SET_NULL, null=False)
    user_id = models.ForeignKey(
        'AdvUser', on_delete=models.SET_NULL, null=False)
    order_time = models.DateTimeField()
    status = models.CharField(max_length=2, choises=OrderStatus.choices, default=OrderStatus.NEW)

    class Meta:
        ordering = ['title', 'status']

    def get_absolute_url(self):
        """Returns the url to access a particular book record."""
        return reverse('order-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.title


class Category(models.Model):
    """Model representing a Category (e.g. 3d, 2d, Picture, etc.)"""
    name = models.CharField(max_length=200,
                            unique=True,
                            help_text="Enter the Category")

    def get_absolute_url(self):
        """Returns the url to access a particular language instance."""
        return reverse('category-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name
