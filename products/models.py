from django.db import models
from .choices import PRODUCT_CATAGORY, PRODUCT_SUBCATAGORY

# Create your models here.
class Product(models.Model):
    catagory = models.CharField(max_length=254, choices=PRODUCT_CATAGORY)
    subcatagory = models.CharField(max_length=254, choices=PRODUCT_SUBCATAGORY)
    name = models.CharField(max_length=254, default='')
    product_summary = models.TextField(default='')
    product_description = models.TextField(null = True, blank=True)
    product_features = models.TextField(null = True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image1 = models.ImageField(upload_to='images',null = True, blank=True)
    image2 = models.ImageField(upload_to='images',null = True, blank=True)
    image3 = models.ImageField(upload_to='images',null = True, blank=True)
   

    def __str__(self):
        return self.name