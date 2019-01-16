from django.urls import path

from .views import (
	product_detail_view,
	product_create_view,
	product_delete_view,
	product_list_view,
	product_update_view,
	)

app_name='products'
urlpatterns = [
	path('',product_list_view,name="product_list"),
	path('create/',product_create_view,name='product_create'),
    path('<int:id>/',product_detail_view,name="product_detail"),
    path('<int:id>/delete/',product_delete_view,name="product_delete"),
    path('<int:id>/update/',product_update_view,name="product_update"),  
]