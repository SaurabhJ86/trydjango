from django.urls import path

from .views import (
	BookCreateView,
	BookDeleteView,
	BookDetailView,
	BookListView,
	BookUpdateView,
	)

app_name = 'books'
urlpatterns = [
	path('',BookListView.as_view(),name='Book-List'),
	path('<int:id>/',BookDetailView.as_view(),name='Book-Detail'),
	path('<int:id>/update/',BookUpdateView.as_view(),name='Book-Update'),
	path('<int:id>/delete/',BookDeleteView.as_view(),name='Book-Delete'),	
	path('create/',BookCreateView.as_view(),name='Book-Create'),
]