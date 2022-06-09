from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from django.core import validators
from django.urls import reverse

# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='detail')

    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True,null=True)
    program = models.CharField(max_length=10)
    department = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)#, validators=[validators.DecimalValidator(10, 0)])

    def __str__(self):
        return self.user.first_name

    def get_absolute_url(self):
        return reverse("user_profile:user_data",kwargs={'pk':self.pk})
