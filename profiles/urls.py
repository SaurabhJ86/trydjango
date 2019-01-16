from django.urls import path


from .views import (
	UserBooksDetailView,
	UserProfilesListView,
	UserToggleView,
	)

app_name = 'profiles'
urlpatterns = [
	path('',UserProfilesListView.as_view(),name='profile-list'),
	path('<str:username>/',UserBooksDetailView.as_view(),name='profile-detail'),
	# path('profile-follow/',UserToggleView.as_view(),name='follow-profile'),
]