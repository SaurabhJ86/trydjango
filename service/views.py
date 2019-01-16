from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import login_required
from django.shortcuts import render,get_object_or_404
from django.views.generic import (
	CreateView,
	DetailView,
	ListView,
	)
# Create your views here.
from .forms import ServiceModelForm
from .models import ServiceModel



class ServiceCreateView(LoginRequiredMixin,CreateView):
	template_name = 'services/service_create.html'
	form_class = ServiceModelForm


	def form_valid(self,form):
		return super().form_valid(form)

class ServiceDetailView(DetailView):
	template_name = 'services/service_detail.html'

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(ServiceModel,id=id_)


class ServiceListView(ListView):
	template_name = 'services/service_list.html'
	queryset = ServiceModel.objects.all()