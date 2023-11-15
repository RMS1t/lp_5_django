from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class SNPValidator(validators.RegexValidator):
    """
     regular expression  for 3 words in field
    """

    regex = r"^[а-яА-Ёё-]+\s{3}$"
    message = _(
        "Enter a valid surname, name and patronymic. This value may contain only letters."
    )