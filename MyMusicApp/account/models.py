from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from MyMusicApp.account.validators import validate_username


# Create your models here.
class Account(models.Model):
    username = models.CharField(max_length=15, validators=[MinLengthValidator(2), validate_username])
    email_address = models.EmailField()
    age = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0)])
