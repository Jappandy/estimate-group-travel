from django.contrib import admin

from .models import(AirHotelTransferEstimate, Estimate, GroupAir, GroupHotel,
    GroupTransfer, FlightLeg, AirOption, HotelOption, GroundOption)


class EstimateAdmin(admin.ModelAdmin):
    search_fields = ['user__username', 'user__email', 'user__id']
    raw_id_fields = ['user']
    
    class Meta:
        model = Estimate

# class GroupAirAdmin(admin.ModelAdmin):
#     search_fields = ['user__username', 'user__email', 'user__id']
#     raw_id_fields = ['user']
    
#     class Meta:
#         model = GroupAir

admin.site.register(AirHotelTransferEstimate)
admin.site.register(Estimate)
admin.site.register(GroupAir)
admin.site.register(FlightLeg)
admin.site.register(AirOption)
admin.site.register(HotelOption)
admin.site.register(GroupHotel)
admin.site.register(GroupTransfer)
admin.site.register(GroundOption)