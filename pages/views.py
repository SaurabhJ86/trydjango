from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from profiles.models import Profile

User = settings.AUTH_USER_MODEL
# Need to work on this.
@login_required
def home_view(request):

	is_following = get_user_model().objects.get(username=request.user).is_following.all()

	context = {
		"is_following":is_following
	}

	return render(request,"home.html",context)


def about_view(request):
	context = {
	"my_name":"saurabh",
	"my_number":8600652281,
	"my_list":[86,00,65,22,"again"]

	}

	return render(request,"about.html",context)