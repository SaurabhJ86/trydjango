from django.db import models
from django.urls import reverse

# Create your models here.

class ServiceModel(models.Model):
	name = models.CharField(max_length=120)
	types = models.CharField(max_length=120)
	active = models.BooleanField(default=True)
	content = models.TextField()


	def get_absolute_url(self):
		return reverse('service:service-detail',kwargs={'id':self.id})
