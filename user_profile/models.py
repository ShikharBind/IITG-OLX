from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from django.core import validators
from django.urls import reverse
from posts_app.models import Product

# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='detail')

    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True,null=True)
    program = models.CharField(max_length=10)
    department = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)#, validators=[validators.DecimalValidator(10, 0)])
    wishlist_products = models.ManyToManyField(Product,blank=True,null=True)

    def __str__(self):
        full_name = self.user.first_name + ' ' + self.user.last_name
        return full_name

    def get_absolute_url(self):
        return reverse("user_profile:user_data",kwargs={'pk':self.pk})

    def add_to_wishlist(self,product):
        if product:
            self.wishlist_products.add(product)
        return

    def remove_from_wishlist(self,product):
        if product:
            self.wishlist_products.remove(product)
        return

    @property
    def profile_pic_url(self):
        if self.profile_pic and hasattr(self.profile_pic, 'url'):
            return self.profile_pic.url
        else:
            return '/static/images/Logo_imageOnly.jpeg'
