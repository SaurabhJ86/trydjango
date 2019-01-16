from django.db import models
from django.urls import reverse

# Create your models here.


class Book(models.Model):
	title = models.CharField(max_length=120)
	author = models.CharField(max_length=120)
	pages = models.IntegerField()
	cost = models.DecimalField(decimal_places=2,max_digits=5)
	ratings = models.IntegerField()
	summary = models.TextField()
	active = models.BooleanField(default=True)


	def __str__(self):
		return self.title


	def get_absolute_url(self):
		return reverse('books:Book-Detail',kwargs={"id":self.id})

