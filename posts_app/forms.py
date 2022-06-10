from dataclasses import fields
from pyexpat import model
from django import forms
from posts_app.models import Product, BuyRequest

class ProductForm(forms.ModelForm):
    class Meta():
        model = Product
        fields = ['product_title','product_details','image','current_age','price']


class BuyRequestForm(forms.ModelForm):
    class Meta():
        model = BuyRequest
        fields = ['price_negotiating']