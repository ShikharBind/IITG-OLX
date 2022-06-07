from django.db import models
from django.utils import timezone
# from django.ur

# Create your models here.

class Product(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    product_title = models.CharField(max_length=200)
    product_details = models.TextField()
    image = models.ImageField()
    current_age = models.IntegerField()
    price = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.product_title