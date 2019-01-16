from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect

# Create your views here.
from .forms import ProductCreate,ProductCreateForm
from .models import Product


# def product_create_view(request):
# 	form = ProductCreateForm()
# 	if request.method == "POST":
# 		form = ProductCreateForm(request.POST)
# 		if form.is_valid():
# 			# print(form.cleaned_data)
# 			Product.objects.create(**form.cleaned_data)


# 	context = {
# 		"form":form,
# 	}

# 	return render(request,'products/product_create_view_form.html',context)
# This is to handle dynamic url's
def render_data(request,id):

	# obj = Product.objects.get(id=id)
	obj = get_object_or_404(Product,id=id)

	context = {
		"object":obj,
	}

	return render(request,'products/product_detail_view.html',context)

def render_initial_data(request):
	initial = {
		"title":"New IPhone is here"
	}
	obj = Product.objects.get(id=1)
	form = ProductCreate(request.POST or None,instance=obj,initial=initial)
	if form.is_valid():
		form.save()
		form = ProductCreate()


	context = {
		"form":form,
	}

	return render(request,'products/product_create_view.html',context)

def product_delete_view(request,id):
	obj = get_object_or_404(Product,id=id)

	if request.method == "POST":
		obj.delete()
		return redirect("../../")


	context = {
		"object":obj,
	}

	return render(request,'products/product_delete_view.html',context)

def product_create_view(request):
	form = ProductCreate(request.POST or None)

	if form.is_valid():
		form.save()
		form = ProductCreate()

	context = {
		"form":form,
	}

	return render(request,'products/product_create_view.html',context)

def product_list_view(request):

	queryset = Product.objects.all()

	context = {
		"object_list":queryset,

	}

	return render(request,'products/product_list_view.html',context)

def product_detail_view(request,id):
	obj = Product.objects.get(id=id)
	context = {
		'object':obj,
	}

	return render(request,'products/product_detail_view.html',context)


@login_required()
def product_update_view(request,id):

	obj = get_object_or_404(Product,id=id)

	form = ProductCreate(request.POST or None,instance=obj)

	if form.is_valid():
		form.save()

	context = {
		"form":form,
	}

	return render(request,'products/product_update_view.html',context)





