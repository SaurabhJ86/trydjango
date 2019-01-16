from django import forms

from .models import Book
class BooksModelForm(forms.ModelForm):
	class Meta:
		model = Book
		exclude = ['user','is_active']

	# Just a simple Validation Error.
	# def clean_price(self,*args,**kwargs):
	# 	price = self.cleaned_data.get("price")
	# 	if price > 600:
	# 		raise forms.ValidationError("Are you sure this is the correct price to created?")
	# 	return price