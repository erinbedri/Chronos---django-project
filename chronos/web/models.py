from datetime import date

from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import CASCADE

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

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Watch(models.Model):
    BRAND_MAX_LEN = 30

    MODEL_MAX_LEN = 30

    REFERENCE_NUMBER_MAX_LEN = 30

    YEAR_MIN_VALUE = 1800
    YEAR_MAX_VALUE = date.today().year

    WATCH_STYLES_CHOICES = [
        ('Pocket Watch', 'Pocket Watch'),
        ('Railroad Watch', 'Railroad Watch'),
        ('Dress Watch', 'Dress Watch'),
        ('Field Watch', 'Field Watch'),
        ('Aviator Watch', 'Aviator Watch'),
        ('Dive Watch', 'Dive Watch'),
        ('Racing Watch', 'Racing Watch'),
        ('Digital Watch', 'Digital Watch'),
        ('Smart Watch ', 'Smart Watch '),
        ('Fashion Watch', 'Fashion Watch'),
    ]

    STYLE_MAX_LEN = max([len(style[1]) for style in WATCH_STYLES_CHOICES])

    CONDITION_MAX_LEN = 50

    DESCRIPTION_MAX_LEN = 200

    owner = models.ForeignKey(
        Profile,
        on_delete=CASCADE
    )

    brand = models.CharField(
        max_length=BRAND_MAX_LEN,
    )

    model = models.CharField(
        max_length=MODEL_MAX_LEN,
    )

    reference_number = models.CharField(
        max_length=REFERENCE_NUMBER_MAX_LEN,
    )

    year = models.IntegerField(
        blank=True,
        null=True,
        validators=[
            MinValueValidator(YEAR_MIN_VALUE),
            MaxValueValidator(YEAR_MAX_VALUE)],
    )

    style = models.CharField(
        max_length=STYLE_MAX_LEN,
        choices=WATCH_STYLES_CHOICES,
    )

    condition = models.TextField(
        null=True,
        blank=True,
        max_length=CONDITION_MAX_LEN,
    )

    description = models.TextField(
        null=True,
        blank=True,
        max_length=DESCRIPTION_MAX_LEN,
    )

    image = models.ImageField(
        upload_to='watch',
        validators=(
            file_size,
        )
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f'{self.brand} {self.model}'
