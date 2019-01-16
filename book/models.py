from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.
User = settings.AUTH_USER_MODEL


class Book(models.Model):
	user 		= models.ForeignKey(User,on_delete=models.CASCADE)
	title 		= models.CharField(max_length=120)
	author 		= models.CharField(max_length=120)
	pages 		= models.IntegerField(default=200)
	price 		= models.DecimalField(max_digits=5,decimal_places=2)
	ratings 	= models.DecimalField(max_digits=5,decimal_places=2)
	summary 	= models.TextField()
	is_active 	= models.BooleanField(default=False)
	timestamp 	= models.DateTimeField(auto_now_add=True)
	updated 	= models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.title


	def get_absolute_url(self):
		return reverse("book:books-details",kwargs={"id":self.id})