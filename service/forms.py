from django import forms

from .models import ServiceModel

class ServiceModelForm(forms.ModelForm):
	class Meta:
		model = ServiceModel
		fields = [
			'name',
			'types',
			'active',
			'content'
		]