from django import forms

from .models import Product

class ProductCreate(forms.ModelForm):
	title 		= forms.CharField(label='Product Title',
			widget=forms.TextInput(attrs={"placeholder":"Product Title"}))
	
	description = forms.CharField(required=False,
			widget=forms.Textarea(attrs={
				"placeholder":"Product Description",
				"rows":20,
				"cols":40,
				}))
	
	price 		= forms.DecimalField(initial=350)

	email 		= forms.EmailField(required=False)
	class Meta:
		model = Product
		fields = [
			'title','description','price','featured'
		]

	# def clean_email(self,*args,**kwargs):
	# 	email = self.cleaned_data.get("email")
	# 	if not email.endswith("edu"):
	# 		raise forms.ValidationError("Not a valid Email Address")
	# 	return email


class ProductCreateForm(forms.Form):

	title 		= forms.CharField()
	description = forms.CharField()
	price 		= forms.DecimalField()
	featured 	= forms.BooleanField()