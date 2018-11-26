from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from estimates.models import Estimate
from estimates.forms import EstimateForm


class EstimateListView(LoginRequiredMixin, ListView):
    model = Estimate
    template_name = 'estimate-list.html'  # Specify your own template name/location
	
    #template_name = 'list.html'
	#queryset = Estimate.objects.all()
	#context_object_name = 'objects'
	#paginate_by = 10
	
	#context_object_name = 'estimate_list'   # your own name for the list as a template variable
    #estimates = Estimate.objects.all()


class CreateEstimateView(LoginRequiredMixin, CreateView):
    form_class = EstimateForm
    #success_url = reverse_lazy('login')
    template_name = 'add-estimate-form.html'

class UpdateEstimateView(LoginRequiredMixin, UpdateView):
    model = Estimate
    fields = '__all__'
    template_name_suffix = '_update_form'
    
