from django.db import models
from django.contrib.auth.models import User
from django.core import validators

# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_pic = models.ImageField()
    program = models.CharField(max_length=10)
    department = models.CharField(max_length=50)
    contact = models.CharField(max_length=10, validators=[validators.DecimalValidator(10, 0)])
