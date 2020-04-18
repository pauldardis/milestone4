from django.db import models

# Create your models here.
class Product(models.Model):
    catagory = models.CharField(max_length=254, default='')
    subcatagory = models.CharField(max_length=254, default='')
    name = models.CharField(max_length=254, default='')
    description = models.TextField(default='')
    brief_description = models.TextField(default='')
    full_description = models.TextField(default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    image1 = models.ImageField(upload_to='images',default='')
    image2 = models.ImageField(upload_to='images',default='')
    image3 = models.ImageField(upload_to='images',default='')
    image4 = models.ImageField(upload_to='images',default='')

    def __str__(self):
        return self.name