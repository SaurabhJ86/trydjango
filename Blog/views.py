from django.shortcuts import render,get_object_or_404
from django.urls import reverse,reverse_lazy
# Create your views here.
from django.views.generic import (
	CreateView,
	DetailView,
	ListView,
	UpdateView,
	DeleteView,
	)


from .forms import ArticleModelForm
from .models import Article

class ArticleCreateView(CreateView):
	template_name = 'articles/article_create.html'
	form_class = ArticleModelForm

	# If you want to make any changes or run some filters against the data before saving it.
	def form_valid(self,form):
		return super().form_valid(form)

class ArticleDeleteView(DeleteView):
	template_name = 'articles/article_delete.html'

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Article,id=id_)

	def get_success_url(self):
		return reverse("blog:article-list")

class ArticleDetailView(DetailView):
	template_name = 'articles/article_detail.html'

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Article,id=id_)

class ArticleListView(ListView):
	template_name = 'articles/article_list.html'
	queryset = Article.objects.all()


class ArticleUpdateView(UpdateView):
	template_name = 'articles/article_create.html'
	form_class = ArticleModelForm

	def form_valid(self,form):
		return super().form_valid(form)

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Article,id=id_)


