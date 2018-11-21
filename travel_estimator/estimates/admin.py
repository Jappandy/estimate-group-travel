from django.contrib import admin

from .models import Estimate, GroupAir, GroupHotel, GroupTransfer, FlightLeg, AirOption, HotelOption, GroundOption 



admin.site.register(Estimate)
admin.site.register(GroupAir)
admin.site.register(FlightLeg)
admin.site.register(AirOption)
admin.site.register(HotelOption)
admin.site.register(GroupHotel)
admin.site.register(GroupTransfer)
admin.site.register(GroundOption)