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
    is_sold = models.BooleanField(default=False)
    selling_date = models.DateTimeField(blank=True, null=True)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchases', blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def sell(self,buyrequest):
        self.is_sold = True
        self.selling_date = timezone.now()
        self.buyer = buyrequest.buyer
        self.save()

    def __str__(self):
        return self.product_title

    def get_absolute_url(self):
        return reverse("posts_app:product_detail",kwargs={'pk':self.pk})

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return '/static/images/Logo_imageOnly.jpeg'





class BuyRequest(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='buy_requests')
    price_negotiating = models.IntegerField(blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='requests')


    def __str__(self):
        return self.product.product_title

    def get_absolute_url(self):
        return reverse("posts_app:product_detail",kwargs={'pk':self.product.pk})