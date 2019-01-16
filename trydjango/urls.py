"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import include,path

from pages.views import home_view,about_view
from profiles.views import UserToggleView
# from cart.views import cart_home
urlpatterns = [
	path('', home_view,name='home'),
	path('about/',about_view,name='about'),
    path('admin/', admin.site.urls),
	path('blog/',include('Blog.urls')),
    path('book/',include('book.urls')),
	path('books/',include('books.urls')),
    path('cart/',include('cart.urls')),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('profile-follow/',UserToggleView.as_view(),name='follow'),
    # The below is for illustration purpse while using the attribute "template_name"
    # path('logout/',LogoutView.as_view(template_name='logged_out2.html'),name='logout'),    
    path('product/',include('products.urls')),
    path('profile/',include('profiles.urls')),
    path('service/',include('service.urls')),
]
