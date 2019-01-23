from django.conf import settings
from django.contrib.auth import get_user_model,login,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render,redirect

# Create your views here.
from profiles.models import Profile
from .forms import SignUpForm

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

"""
The below view would be responsible for showing logged in user details as well as some links to books referenced by the current user.
"""
@login_required
def my_account(request):

	context = {}

	return render(request,"accounts.html",context)


def register(request):
	print("something")
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get("username")
			password = form.cleaned_data.get("password1")
			user = authenticate(username=username,password=password)
			login(request,user)
			return redirect('/')
	else:
		if request.user.is_authenticated:
			return redirect('/')
		form = SignUpForm()
	context = {
		"form":form,
	}

	template_name = "Register.html"

	return render(request,template_name,context)

