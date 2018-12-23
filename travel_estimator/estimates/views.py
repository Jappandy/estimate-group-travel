from django.contrib.messages.views import SuccessMessageMixin 
from django.contrib import messages
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse, FileResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.views.generic.edit import UpdateView
from django.views.generic import DetailView, ListView, CreateView, TemplateView, View
from django.views.generic.base import TemplateResponseMixin
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from estimates.models import(AirHotelTransferEstimate, Estimate, GroupAir, AirOption,
    FlightLeg, GroupHotel, HotelOption, GroupTransfer, GroundOption,)
from estimates.forms import(AirHotelTransferEstimateForm, EstimateForm, AirOptionForm, 
    GroupAirForm, FlightLegForm, GroupHotelForm, HotelOptionForm, GroupTransferForm, GroundOptionForm)
from reportlab.pdfgen import canvas
from estimates.utils import render_to_html_pdf
from estimates.pdfs import render_to_pdf
from django.utils import timezone
import json
import requests


##################################################################
### PDF -- WORKING
##################################################################

class PDFResponseMixin(TemplateResponseMixin):
    """
        http://www.example.com?[pdf_querydict_key]=[pdf_querydict_value]

    Example with values::
        http://www.example.com?format=pdf
    """
    
    pdf_querydict_key = 'format'
    pdf_querydict_value = 'pdf'

    def is_pdf(self):
        value = self.request.GET.get(self.pdf_querydict_key, '')
        return value.lower() == self.pdf_querydict_value.lower()

    def get_pdf_response(self, context, **response_kwargs):
        return render_to_pdf(self.get_object())

    def render_to_response(self, context, **response_kwargs):
        if self.is_pdf():
            from django.conf import settings
            context['STATIC_ROOT'] = settings.STATIC_ROOT
            return self.get_pdf_response(context, **response_kwargs)
            
        #context[self.pdf_url_varname] = self.get_pdf_url()
        return super(PDFResponseMixin, self).render_to_response(
            context, **response_kwargs)

##################################################################
### PDF OPTION 2  - WORKING 
##################################################################

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        data = {
            'today': 'today', 
            'amount': 39.99,
            'customer_name': 'Cooper Mann',
            'order_id': 1233434,
        }
        pdf = render_to_html_pdf('pdf/estimate-invoice.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


##################################################################
### TAKES USER TO SKYSCANNER'S WHITELABEL 
##################################################################
class SearchFlightsTemplateView(LoginRequiredMixin, TemplateView):
    
    template_name = 'search-flights.html'
   

################################################################## 
class FullEstimateListView(LoginRequiredMixin, ListView):
    
    model = AirHotelTransferEstimate
    template_name = 'full-estimate-list.html'
    queryset = AirHotelTransferEstimate.objects.all()
    context_object_name = 'full_estimate_list'



class CreateAirHotelTransferEstimateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = AirHotelTransferEstimateForm
    template_name = 'add-full-estimate-form.html'
    model = AirHotelTransferEstimate
    success_url = '/full-estimate-list/'
    success_message = "Your information was created successfully"



class UpdateAirHotelTransferEstimateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = AirHotelTransferEstimate
    fields = '__all__'
    template_name = 'update-full-estimate-form.html'
    success_url = '/full-estimate-list/'
    success_message = "Your information was updated successfully"


    

class FullEstimateDetailView(LoginRequiredMixin, DetailView):
    
    model = AirHotelTransferEstimate
    template_name = 'details-full-estimate.html'
    # queryset = .objects.all() #AirHotelTransferEstimate.objects.filter(id_gt=1)

    
    def get_object(self):
        obj = super(FullEstimateDetailView, self).get_object()
        # Record the last accessed date
        obj.save()
        return obj


### ESTIMATE
class EstimateListView(LoginRequiredMixin, ListView):
    
    model = Estimate
    template_name = 'estimate-list.html'
    queryset = Estimate.objects.all()
    context_object_name = 'estimate_list'
    


### ESTIMATE CREATE
class CreateEstimateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = EstimateForm
    template_name = 'add-estimate-form.html'
    model = Estimate
    success_url = '/add-full-estimate-form/'
    success_message = "Your information was created successfully"
    # queryset = Estimate.objects.all()

    
    
    
### ESTIMATE UPDATE    
class UpdateEstimateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Estimate
    fields = '__all__'
    template_name = 'update-estimate-form.html'
    success_url = '/'
    success_message = "Your information was updated successfully"
    
    
### PDF    
class EstimatePDFDetailView(LoginRequiredMixin, PDFResponseMixin, DetailView):
    model = Estimate
    slug_field = 'slug'


### ESTIMATE DETAIL
class EstimateDetailView(LoginRequiredMixin, DetailView):
    
    model = Estimate
    template_name = 'details-estimate.html'
    # queryset = Estimate.objects.all() #Estimate.objects.filter(id_gt=1)

    
    def get_object(self):
        obj = super(EstimateDetailView, self).get_object()
        obj.save()
        return obj


### GROUP AIR CREATE
class CreateGroupAirView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = GroupAirForm
    template_name = 'add-group-air-form.html'
    model = GroupAir
    success_url = '/add-hotel-option-form/'
    success_message = "Your information was created successfully"


### GROUP AIR UPDATE
class UpdateGroupAirView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = GroupAir
    fields = '__all__'
    # exclude = ('group_air', 'group_hotel', 'group_transfer')
    template_name = 'update-group-air-form.html'
    success_url = '/'
    success_message = "Your information was updated successfully"


### GROUP AIR DETAIL
class GroupAirDetailView(LoginRequiredMixin, DetailView):
    model = GroupAir
    template_name = 'details-group-air.html'
    # queryset = .objects.all() #GroupAir.objects.filter(id_gt=1)

    
    def get_object(self):
        obj = super(GroupAirDetailView, self).get_object()
        obj.save()
        return obj


### AIR OPTION CREATE
class CreateAirOptionView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = AirOptionForm
    template_name = 'add-air-option-form.html'
    model = AirOption
    success_url = '/add-group-air-form/'
    success_message = "Your information was created successfully"


### AIR OPTION UPDATE
class UpdateAirOptionView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = AirOption
    fields = '__all__'
    # exclude = ('group_air', 'group_hotel', 'group_transfer')
    template_name = 'update-air-option-form.html'
    success_url = '/'
    success_message = "Your information was updated successfully"


### AIR OPTION DETAIL
class AirOptionDetailView(LoginRequiredMixin, DetailView):
    model = AirOption
    template_name = 'details-air-option.html'
    # queryset = .objects.all() #GroupAir.objects.filter(id_gt=1)

    def get_object(self):
        obj = super(AirOptionDetailView, self).get_object()
        obj.save()
        return obj    


### FLIGHT LEG CREATE 
class CreateFlightLegView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = FlightLegForm
    template_name = 'add-flight-leg-form.html'
    model = FlightLeg
    success_url = '/add-air-option-form/'
    success_message = "Your information was created successfully"


### FLIGHT LEG UPDATE
class UpdateFlightLegView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = FlightLeg
    fields = '__all__'
    template_name = 'update-flight-leg-form.html'
    success_url = '/'
    success_message = "Your information was updated successfully"


### FLIGHT LEG DETAIL
class FlightLegDetailView(LoginRequiredMixin, DetailView):
    
    model = FlightLeg
    template_name = 'details-flight-leg.html'
    # queryset = .objects.all() #GroupAir.objects.filter(id_gt=1)

    
    def get_object(self):
        obj = super(FlightLegDetailView, self).get_object()
        obj.save()
        return obj


### GROUP HOTEL CREATE
class CreateGroupHotelView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = GroupHotelForm
    template_name = 'add-group-hotel-form.html'
    model = GroupHotel
    success_url = '/add-ground-option-form/'
    success_message = "Your information was created successfully"


### GROUP HOTEL UPDATE
class UpdateGroupHotelView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = GroupHotel
    fields = '__all__'
    # exclude = ('group_air', 'group_hotel', 'group_transfer')
    template_name = 'update-group-hotel-form.html'
    success_url = '/'
    success_message = "Your information was updated successfully"
  
    
### GROUP HOTEL DETAIL
class GroupHotelDetailView(LoginRequiredMixin, DetailView):
    model = GroupHotel
    template_name = 'details-group-hotel.html'
    # queryset = .objects.all() #GroupAir.objects.filter(id_gt=1)

    
    def get_object(self):
        obj = super(GroupHotelDetailView, self).get_object()
        obj.save()
        return obj


### HOTEL OPTION CREATE
class CreateHotelOptionView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = HotelOptionForm
    template_name = 'add-hotel-option-form.html'
    model = HotelOption
    success_url = '/add-group-hotel-form/'
    success_message = "Your information was created successfully"



### HOTEL OPTION UPDATE
class UpdateHotelOptionView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = HotelOption
    fields = '__all__'
    # exclude = ('group_air', 'group_hotel', 'group_transfer')
    template_name = 'update-hotel-option-form.html'
    success_url = '/'
    success_message = "Your information was updated successfully"
    
    
### HOTEL OPTION DETAIL
class HotelOptionDetailView(LoginRequiredMixin, DetailView):
    model = HotelOption
    template_name = 'details-hotel-option.html'
    # queryset = .objects.all() #GroupAir.objects.filter(id_gt=1)

    
    def get_object(self):
        obj = super(HotelOptionDetailView, self).get_object()
        obj.save()
        return obj


### GROUP TRANSFER CREATE
class CreateGroupTransferView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = GroupTransferForm
    template_name = 'add-group-transfer-form.html'
    model = GroupTransfer
    success_url = '/add-estimate-form/'
    success_message = "Your information was created successfully"


### GROUP TRANSFER UPDATE
class UpdateGroupTransferView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = GroupTransfer
    fields = '__all__'
    # exclude = ('group_air', 'group_hotel', 'group_transfer')
    template_name = 'update-group-transfer-form.html'
    success_url = '/'
    success_message = "Your information was updated successfully"
    

### GROUP TRANSFER DETAIL
class GroupTransferDetailView(LoginRequiredMixin, DetailView):
    model = GroupTransfer
    template_name = 'details-group-transfer.html'
    # queryset = .objects.all() #GroupAir.objects.filter(id_gt=1)

    
    def get_object(self):
        obj = super(GroupTransferDetailView, self).get_object()
        obj.save()
        return obj
  
    
### GROUND OPTION CREATE    
class CreateGroundOptionView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = GroundOptionForm
    template_name = 'add-ground-option-form.html'
    model = GroundOption
    success_url = '/add-group-transfer-form/'
    success_message = "Your information was created successfully"
    

### GROUND OPTION UPDATE
class UpdateGroundOptionView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = GroundOption
    fields = '__all__'
    # exclude = ('group_air', 'group_hotel', 'group_transfer')
    template_name = 'update-ground-option-form.html'
    success_url = '/'
    success_message = "Your information was updated successfully"
    

### GROUND OPTION DETAIL
class GroundOptionDetailView(LoginRequiredMixin, DetailView):
    model = GroundOption
    template_name = 'details-ground-option.html'
    # queryset = .objects.all() #GroundOption.objects.filter(id_gt=1)

    
    def get_object(self):
        obj = super(GroundOptionDetailView, self).get_object()
        obj.save()
        return obj


##################################################################
# def GroupAirCreatePopup(request):
#     form = GroupAirForm(request.POST or None)
#     if form.is_valid():
#         instance = form.save()
#         messages.success(request, 'Successfully Added Group Air')
        
#         return HttpResponse('<script>opener.closePopup(window, "{}", "{}", \
#         "#group_air_id");</script>'.format(instance.pk, instance))
    
#     return render(request, "group-air-form.html", {"form": form})


# def GroupAirEditPopup(request, pk = None):
#     instance = get_object_or_404(GroupAir, pk = pk)
#     form = GroupAirForm(request.POST or None, instance = instance)
#     if form.is_valid():
#         instance = form.save()
#         messages.success(request, 'Successfully Added Group Air')
        
#         return HttpResponse('<script>opener.closePopup(window, "{}",\
#         "{}", "#group_air_id");</script>'.format(instance.pk, instance))
    
#     return render(request, "group-air-form.html", {"form": form})


# @csrf_exempt
# def get_group_air_id(request):
#     if request.is_ajax():
#         group_air_namer = request.GET['group_air_name']
#         group_air_id = GroupAir.objects.get(group_air_name = group_air_namer).id
#         data = {'group_air_id': group_air_id,}
        
#         return HttpResponse(json.dumps(data), content_type='application/json')
#     return HttpResponse("/")
    
    

    
##################################################################

# def manage_estimate(request, group_air_id):
#     """Edit Estimate and its items for a single WHAT???"""
    
#     group_air = get_object_or_404(GroupAir, id=group_air_id)
    
#     if request. method == 'POST':
#         formset = EstimateFormSet(request.POST, instance=group_air)

##################################################################
