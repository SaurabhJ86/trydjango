from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import redirect,render,get_object_or_404,redirect
from django.urls import reverse_lazy,reverse
# Create your views here.
from .models import Book
from .forms import BooksModelForm

from django.views.generic import (
	CreateView,
	DetailView,
	DeleteView,
	ListView,
	UpdateView,
	View,
	)



class BooksCreateView(LoginRequiredMixin,CreateView):

	template_name = 'books/BooksCreateView.html'
	form_class = BooksModelForm

	def form_valid(self,form):
		instance = form.save(commit=False)
		instance.user = self.request.user
		instance.save()
		return super().form_valid(form)

class BooksDeleteView(LoginRequiredMixin,DeleteView):

	template_name = 'books/BooksDeleteView.html'
	success_url = reverse_lazy("book:books-list")

	def get_object(self):
		id_ = self.kwargs.get("id")
		obj = get_object_or_404(Book,id=id_)
		if obj.user.id != self.request.user.id:
			raise Http404("You do not have the permission to delete this page.")
		return obj

class BooksDetailView(LoginRequiredMixin,DetailView):

	template_name = 'books/BooksDetailView.html'

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Book,id=id_)

	"""
	The below method will check whether the logged in user the owner or not, and if owner then an update button
	will be available which will take the owner to update page where he/she can update the details of the book.	
	"""
	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		id_ = self.kwargs.get("id")
		obj = get_object_or_404(Book,id=id_)
		is_owner = False

		if self.request.user.id == obj.user.id:
			context["is_owner"] = True

		return context

class BooksListView(ListView):

	template_name = 'books/BooksListView.html'

	def get_queryset(self,*args,**kwargs):
		filter_by = self.request.GET.get("filter_by")
		books = Book.objects.all()
		if filter_by is not None:
			books = Book.objects.filter(book_type=filter_by.lower())
		return books

	"""
	The below method will allow the redirect to the same page with a QueryString parameter
	which in turn will be used by get_queryset method above.
	"""
	def post(self,request,*args,**kwargs):
		filter_by = request.POST.get("book_type")
		return redirect(f"/book/?filter_by={filter_by}")

	"""
	As of now this method is being used to pass in the Filter values.
	"""
	def get_context_data(self,**kwargs):
		from .models import BOOK_CHOICES
		context = super().get_context_data(**kwargs)
		choices = BOOK_CHOICES

		context["CHOICES"] = choices

		return context

class BooksListViewByUser(ListView):

	template_name = 'books/BooksMyListView.html'

	def get_queryset(self):
		queryset = Book.objects.filter(user=self.request.user)
		return queryset

class BooksUpdateView(LoginRequiredMixin,UpdateView):
	template_name = 'books/BooksCreateView.html'
	form_class = BooksModelForm

	def get_object(self):
		id_ = self.kwargs.get("id")
		obj = get_object_or_404(Book,id=id_)
		# The below will make sure that only the owner can make the changes otherwise an exception would be raised.
		# Using below instead of self.request.user == obj.user, incase the user has same name.
		if self.request.user.id != obj.user.id:
			raise Http404("No permission to update this page.")
			# Need to know why we need to use raise instead of return sometimes.
			# return HttpResponse("You do not have the permission to view this page.")
		return obj

@login_required
def BookCreateFn(request):

	form = BooksModelForm(request.POST or None)
	if form.is_valid():
		if request.user.is_authenticated():
			instance = form.save(commit=False)
			instance.user = request.user
			instance.save()
			form = BooksModelForm()

	template = 'books/BooksCreateView.html'
	context = {
		"form":form,
	}
	return render(request,template,context)