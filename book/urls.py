from django.urls import path

from .views import (
	BooksCreateView,
	BookCreateFn,
	BooksDeleteView,
	BooksDetailView,
	BooksListView,
	BooksListViewByUser,
	BooksUpdateView
	)

app_name='book'
urlpatterns = [
	path('',BooksListView.as_view(),name='books-list'),
	path('mylist/',BooksListViewByUser.as_view(),name='books-my-list'),
	path('create/',BooksCreateView.as_view(),name='books-create'),
	path('<int:id>/delete/',BooksDeleteView.as_view(),name='books-delete'),
	path('<int:id>/update/',BooksUpdateView.as_view(),name='books-update'),
	path('<int:id>/',BooksDetailView.as_view(),name='books-details'),
	# path('create/',BookCreateFn,name='books-create'),
]