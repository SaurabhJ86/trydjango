from django.urls import path

from .views import (
	ServiceCreateView,
	ServiceDetailView,
	ServiceListView,
	)

app_name = "service"
urlpatterns = [
	path('',ServiceListView.as_view(),name='service-list'),
	path('create/',ServiceCreateView.as_view(),name='service-create'),
	path('<int:id>/',ServiceDetailView.as_view(),name='service-detail'),
]