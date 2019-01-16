from django.shortcuts import render

# Create your views here.


def cart_home(request):

	context = {}

	return render(request,"cart_home.html",context)