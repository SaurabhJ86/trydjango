from django.conf.urls import url
from .views import (
		BookListAPIView,
	)

urlpatterns = [
	url(r'^$',BookListAPIView.as_view()),
]