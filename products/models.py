from django.db import models
from django.urls import reverse
# Create your models here.

class Product(models.Model):
	title 		= models.CharField(max_length=120)
	description = models.TextField()
	price 		= models.DecimalField(decimal_places=2,max_digits=999)
	summary 	= models.TextField()
	featured 	= models.BooleanField()


	def get_absolute_url(self):
		return reverse("products:product_detail",kwargs={"id":self.id})

