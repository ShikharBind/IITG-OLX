from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core import validators
from django.urls import reverse
# from django.ur

# Create your models here.

class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    product_title = models.CharField(max_length=200)
    product_details = models.TextField(blank=True)
    image = models.ImageField(upload_to='product_pics/', blank=True,null=True)
    current_age = models.IntegerField()
    price = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)
    selling_date = models.DateTimeField(blank=True, null=True)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchases', blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.product_title

    def get_absolute_url(self):
        return reverse("posts_app:product_detail",kwargs={'pk':self.pk})