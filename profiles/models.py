from django.db import models

# Create your models here.
from django.conf import settings
from django.db.models.signals import post_save

from django.urls import reverse

from book.models import Genre
User = settings.AUTH_USER_MODEL


class ProfileManager(models.Manager):
	def toggle_user(self,request_user,user_to_toggle):
		profile = Profile.objects.get(user__username__iexact=user_to_toggle)
		user = request_user
		is_following = False
		if user in profile.followers.all():
			profile.followers.remove(user)
		else:
			profile.followers.add(user)
			is_following = True
		return profile,is_following

class Profile(models.Model):
	user 		= models.OneToOneField(User,on_delete=models.CASCADE)
	followers 	= models.ManyToManyField(User,related_name='is_following',blank=True)
	activated 	= models.BooleanField(default=False)
	timestamp 	= models.DateTimeField(auto_now_add=True)
	updated 	= models.DateTimeField(auto_now=True)
	genre 		= models.ManyToManyField(Genre,related_name='follows_genre',blank=True)


	objects = ProfileManager()

	def __str__(self):
		return self.user.username

	def get_absolute_url(self):
		return reverse("profiles:profile-detail",kwargs={"username":self.user.username})



def post_save_user_receiver(sender,instance,created,*args,**kwargs):
	if created:
		profile,is_created = Profile.objects.get_or_create(user=instance)
		default_user_profile = Profile.objects.get(id=2)

		default_user_profile.followers.add(instance)



post_save.connect(post_save_user_receiver,sender=User)