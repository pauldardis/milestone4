from django.db import models

# Create your models here.
class Product(models.Model):
    catagory = models.CharField(max_length=254, default='')
    subcatagory = models.CharField(max_length=254, default='')
    name = models.CharField(max_length=254, default='')
    description = models.TextField(default='')
    brief_description = models.TextField(null = True, blank=True)
    full_description = models.TextField(null = True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images',null = True, blank=True)
    image1 = models.ImageField(upload_to='images',null = True, blank=True)
    image2 = models.ImageField(upload_to='images',null = True, blank=True)
    image3 = models.ImageField(upload_to='images',null = True, blank=True)
    image4 = models.ImageField(upload_to='images',null = True, blank=True)

    def __str__(self):
        return self.name