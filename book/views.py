from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse,Http404
from django.shortcuts import redirect,render,get_object_or_404
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

class BooksListView(ListView):

	template_name = 'books/BooksListView.html'
	queryset = Book.objects.all()

class BooksListViewByUser(ListView):

	template_name = 'books/BooksListView.html'

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