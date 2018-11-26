from django import forms

from estimates.models import Estimate, GroupTransfer, GroundOption, GroupHotel, HotelOption, GroupAir, AirOption, FlightLeg


class EstimateForm(forms.ModelForm):
    class Meta:
        model = Estimate
        fields = '__all__' #or []
        # fields = [
        #     'estimate_name',
        #     'estimate_status'
        #     ]
        
        
class GroupTransferForm(forms.ModelForm):
    class Meta:
        model = GroupTransfer
        fields = '__all__'
        

class GroundOptionForm(forms.ModelForm):
    class Meta:
        model = GroundOption
        fields = '__all__'
        

class GroupHotelForm(forms.ModelForm):
    class Meta:
        model = GroupHotel
        fields = '__all__'
        
        
class HotelOptionForm(forms.ModelForm):
    class Meta:
        model = HotelOption
        fields = '__all__'

class AirlOptionForm(forms.ModelForm):
    class Meta:
        model = AirOption
        fields = '__all__'


class GroupAirForm(forms.ModelForm):
    class Meta:
        model = GroupAir
        fields = '__all__'
        

class FlightLegForm(forms.ModelForm):
    class Meta:
        model = FlightLeg
        fields = '__all__'