from django.conf import settings
from django.contrib.auth import get_user_model,login,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Count
from django.http import HttpResponse,Http404
from django.views.generic import (
		UpdateView,
		ListView,
	)
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse

# Create your views here.
from book.models import Book,Genre
from profiles.models import Profile

from .forms import SignUpForm

# Need to work on this.
@login_required
def home_view(request):
	is_following = get_user_model().objects.get(username=request.user).is_following.all()

	followed_books = []
	genre_books = []

	if is_following:
		for user in is_following:
			for book in user.user.book_set.all():
				followed_books.append(book)

	get_genre = Profile.objects.get(user=request.user).genre.all()
	if get_genre:
		genre_books = Book.objects.filter(genre__in=get_genre)
	books = list(set(followed_books + list(genre_books)))

	# books = Book.objects.filter(genre__in=get_genre)
	# new_books = list(books)
	# final_list = list(set(followed_books + new_books))
	context = {
		"is_following":is_following,
		"books":books,
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

"""
There are couple of things which I need to mention here. First of all, instead of using the form UserCreationForm,
I am using the model "User" and its fields which in turn will work instead of the form_class,

In the method get_success_url, I am using the self.get_object() method to pass in the id as the kwargs
to the url "update_details."
"""
class update_details(LoginRequiredMixin,UpdateView):
	# form_class = UserCreationForm
	model = User
	fields = ['first_name','last_name','email']
	template_name = 'update_details.html'

	def get_object(self):
		id_ = self.kwargs.get("id")
		obj = get_object_or_404(User,id=id_)
		if self.request.user.id != obj.id:
			raise Http404("No permission to update details page.")
		return obj

	def get_success_url(self):
		return reverse('update_details',kwargs={"id":self.get_object().id})


def register(request):
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


class listGenre(LoginRequiredMixin,ListView):
	template_name = "listGenre.html"
	queryset = Genre.objects.annotate(num_book=Count("under_genre")).filter(num_book__gt=0)

	def get_context_data(self,**kwargs):
		context 			= super().get_context_data(**kwargs)
		get_user_genres 	= Profile.objects.get(user=self.request.user).genre.all()
		unselected_genres 	= [g for g in Genre.objects.all() if g not in get_user_genres]

		context["Unselected_Genre"] = unselected_genres
		context["Selected_Genre"] 	= get_user_genres

		return context




