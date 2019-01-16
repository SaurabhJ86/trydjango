from django.db import models

# Create your models here.

from products.models import Product
class user_cart(models.Model):

	product = models.ForeignKey(Product,on_delete=models.CASCADE)
	description = models.CharField(max_length=120)
