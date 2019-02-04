from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.
User = settings.AUTH_USER_MODEL

BOOK_CHOICES = [
	('history','HISTORY'),
	('drama','DRAMA'),
	('horror','HORROR'),
	('thriller','THIRLLER'),
	('spy','SPY'),
	('comic','COMIC'),
	('science','SCIENCE'),
]
class Genre(models.Model):
	genre 		= models.CharField(max_length=50)
	timestamp 	= models.DateTimeField(auto_now_add=True)
	updated 	= models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.genre

class Author(models.Model):
	author 		= models.CharField(max_length=120)
	timestamp 	= models.DateTimeField(auto_now_add=True)
	updated 	= models.DateTimeField(auto_now=True)
	about 		= models.TextField()
	genre 		= models.ManyToManyField(Genre,related_name='author_genre',blank=True)

	def __str__(self):
		return self.author

	def get_absolute_url(self,**kwargs):
		return reverse("author_details",kwargs={"id":self.id})

class Book(models.Model):
	user 		= models.ForeignKey(User,on_delete=models.CASCADE)
	title 		= models.CharField(max_length=120)
	author 		= models.CharField(max_length=120)
	author_new 	= models.ForeignKey(Author,on_delete=models.CASCADE,null=True,blank=True)
	pages 		= models.IntegerField(default=200)
	price 		= models.DecimalField(max_digits=5,decimal_places=2)
	ratings 	= models.DecimalField(max_digits=5,decimal_places=2)
	fictional 	= models.BooleanField(default=False)
	book_type 	= models.CharField(max_length=100,choices=BOOK_CHOICES,default='history')
	genre 		= models.ManyToManyField(Genre,related_name='under_genre',blank=True)
	summary 	= models.TextField()
	is_active 	= models.BooleanField(default=False)
	timestamp 	= models.DateTimeField(auto_now_add=True)
	updated 	= models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.title


	def get_absolute_url(self):
		return reverse("book:books-details",kwargs={"id":self.id})