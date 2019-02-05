from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect

# Create your views here.
from django.views.generic import (
	View,
	DetailView,
	ListView,
	)

User = settings.AUTH_USER_MODEL

from .models import Profile
class UserBooksDetailView(DetailView):

	template_name = 'profiles/ProfileDetailView.html'


	def get_object(self):
		user = self.kwargs.get("username")
		obj = get_object_or_404(get_user_model(),username=user)
		return obj
		# queryset = Profile.objects.get()

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		is_following = False
		is_owner = False
		user = self.request.user
		# Need to explain the below step for future.
		get_owner = Profile.objects.get(user=self.get_object())
		get_owner_followers = get_owner.followers.all()
		get_user_is_following = user.is_following.all()

		# This part is required so that we can show the Followed_By part in the profile page.
		common_users = []
		for user in get_owner_followers:
			if Profile.objects.get(user=user) in get_user_is_following:
				common_users.append(user)


		if self.request.user.id == get_owner.user.id:
			is_owner = True

		if user.is_authenticated:
			if user in get_owner.followers.all():
				is_following = True
		context["is_following"] = is_following
		context["is_owner"] = is_owner
		context["common_users"] = common_users

		return context


class UserProfilesListView(ListView):

	template_name = 'profiles/ProfileListView.html'

	def get_queryset(self):
		"""
			The below will make sure that for authenticated user i.e. not Anonymous different data comes and for
			Anonymous all the users are shown.
		"""
		if self.request.user:
			queryset = Profile.objects.all().exclude(user__username = self.request.user)
		else:
			queryset = Profile.objects.all()
		return queryset

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		"""
			This will make sure that only authenticated user can see the content. 
			For Anonymous user he/she will see data from queryset(above) only
		"""
		if self.request.user.is_authenticated:
			followers = Profile.objects.get(user__username=self.request.user).followers.all()
			is_following = get_user_model().objects.get(username=self.request.user).is_following.all()
			context["followers"] = followers
			context["is_following"] = is_following
		return context

"""
The below class would be responsible for the follow button at the ProfileDetailView.html file.
The post method will handle the url "follow" at the urls.py file at trydjango path which in turn is being used by the form "follow_form"
"""
class UserToggleView(View):
	def post(self,request,*args,**kwargs):
		owner = request.POST.get("username").strip()
		profile,is_following = Profile.objects.toggle_user(self.request.user,owner)
		return redirect(f"/profile/{owner}/")








