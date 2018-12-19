from django import forms
from django.contrib.auth import get_user_model
# from django.utils.text import slugify

from estimates.models import (AirHotelTransferEstimate, Estimate, GroupTransfer,
    GroundOption, GroupHotel, HotelOption, GroupAir, AirOption, FlightLeg)

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset

# from django.forms.models import inlineformset_factory
# from django.forms.models import BaseInlineFormSet


##################################################################
### MODELS FORMS
##################################################################

class AirHotelTransferEstimateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Fieldset("", 'account_name','estimate','group_air','group_hotel',
            'group_transfer'),
        )
        
        super(AirHotelTransferEstimateForm,self).__init__(*args, **kwargs)
        
    class Meta:
        model = AirHotelTransferEstimate
        fields = '__all__' #or []
        


class EstimateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Fieldset("", 'estimate_name','estimate_status','details',
            'start_date','end_date','number_of_people', 'agent', 'payment_status',
            'destination','group_air','group_hotel', 'group_transfer'),
        )
    
        super(EstimateForm,self).__init__(*args, **kwargs)
        
    class Meta:
        model = Estimate
        fields = '__all__' 
        
    


            
### GROUND           
class GroupTransferForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Fieldset("", 'group_transfer_name', 'ground_budget', 'ground_options'),
        )
        
        super(GroupTransferForm,self).__init__(*args, **kwargs)
        
    class Meta:
        model = GroupTransfer
        fields = '__all__'



class GroundOptionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Fieldset("", 'transfer_option_name', 'vendor_name',
            'number_of_shuttles', 'transfer_rate', 'transfer_fees', 
            'transfer_taxes', 'pickup_date','pickup_location',
            'dropoff_date','dropoff_location','service_details'),
        )
        
        super(GroundOptionForm,self).__init__(*args, **kwargs)
     
    class Meta:
        model = GroundOption
        fields = '__all__'


### HOTEL  
class GroupHotelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Fieldset("",'group_hotel_name', 'hotel_budget', 'hotel_options'),
        )
        
        super(GroupHotelForm,self).__init__(*args, **kwargs)
     
    class Meta:
        model = GroupHotel
        fields = '__all__'



class HotelOptionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Fieldset("", 'hotel_option_name', 'hotel_name', 'room_type', 
            'check_in', 'check_out', 'number_of_nights', 'number_of_rooms', 
            'hotel_rate', 'hotel_fees', 'hotel_taxes'),
        )
        
        super(HotelOptionForm,self).__init__(*args, **kwargs)
     
    class Meta:
        model = HotelOption
        fields = '__all__'


### AIR 
class FlightLegForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Fieldset("", 'air_leg_name', 'airline', 'flight_num', 'depart_from',
            'depart_air_code', 'depart_date_time', 'arrive_into', 
            'arrive_air_code', 'arrive_date_time'),
        )
        
        super(FlightLegForm,self).__init__(*args, **kwargs)
     
    class Meta:
        model = FlightLeg
        fields = '__all__'



class AirOptionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Fieldset("", 'air_option_name', 'passenger_count', 'air_rate', 
            'air_fees','air_taxes', 'air_discount', 'commit_deadline', 
            'payment_deadline', 'ticket_deadline', 'utilize_deadline', 
            'departure_date', 'return_date','flight_legs'),
        )
        
        super(AirOptionForm,self).__init__(*args, **kwargs)
     
    class Meta:
        model = AirOption
        fields = '__all__'

       
        
class GroupAirForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Fieldset("", 'group_air_name', 'air_budget', 'air_options'),
        )
        
        super(GroupAirForm,self).__init__(*args, **kwargs)
     
    class Meta:
        model = GroupAir
        fields = '__all__'

# Inline forms
# EstimateGroupAirInlineFormSet = inlineformset_factory(GroupAir, Estimate, form=EstimateForm, extra=1, can_delete=False)
# EstimateGroupHotelInlinFormSet = inlineformset_factory(GroupHotel, Estimate, form=EstimateForm, extra=1, can_delete=False)
# EstimateGroupTransferInlineFormSet = inlineformset_factory(GroupTransfer, Estimate, form=EstimateForm, extra=1, can_delete=False)
