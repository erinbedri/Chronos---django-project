from django.core.validators import MinLengthValidator
from django.db import models

from chronos.web.validators import file_size


class Profile(models.Model):
    USERNAME_MAX_LEN = 30

    FIRST_NAME_MIN_LEN = 2
    FIRST_NAME_MAX_LEN = 30

    LAST_NAME_MIN_LEN = 2
    LAST_NAME_MAX_LEN = 30

    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        unique=True
    )

    email = models.EmailField(
        blank=True,
        null=True
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        blank=True,
        null=True,
        validators=[
            MinLengthValidator(FIRST_NAME_MIN_LEN),
        ]
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        blank=True,
        null=True,
        validators=[
            MinLengthValidator(LAST_NAME_MIN_LEN),
        ]
    )

    image = models.ImageField(
        upload_to='profile',
        null=True,
        blank=True,
        validators=(
            file_size,
        )
    )
