from atexit import register
from django.contrib import admin
from posts_app import models

# Register your models here.
admin.site.register(models.Product)