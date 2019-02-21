from rest_framework import generics

from book.models import Book
from .serializers import BookSerializers


class BookListAPIView(generics.ListAPIView):
	permission_classes 				= []
	authentication_classes 			= []
	serializer_class 				= BookSerializers
	queryset 						= Book.objects.all()