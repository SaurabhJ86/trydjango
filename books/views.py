from django.urls import reverse,reverse_lazy
from django.shortcuts import render,get_object_or_404

# Create your views here.
from .forms import BookForm
from .models import Book
from django.views.generic import (
	CreateView,
	DetailView,
	DeleteView,
	ListView,
	UpdateView,
	)



class BookCreateView(CreateView):
	template_name = 'books/BookCreateView.html'
	form_class = BookForm

	def form_valid(self,form):
		# The below shows you the data that has been passed.
		# print(form.cleaned_data)
		return super().form_valid(form)

class BookDeleteView(DeleteView):
	template_name = 'books/BookDeleteView.html'
	model = BookForm
	success_url = reverse_lazy('books:Book-List')
	# The below will throw an error
	# success_url = reverse('home')

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Book,id=id_)



class BookDetailView(DetailView):
	template_name = 'books/BookDetailView.html'

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Book,id=id_)

class BookListView(ListView):
	template_name = 'books/BookListView.html'
	queryset = Book.objects.all()


class BookUpdateView(UpdateView):
	template_name = 'books/BookCreateView.html'
	form_class = BookForm

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Book,id=id_)