from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.urls import reverse


##################################################################
### AIR MODELS 
##################################################################

class FlightLeg(models.Model):
    air_leg_name = models.CharField(max_length=255)
    airline = models.CharField(max_length=255)
    flight_num = models.PositiveIntegerField()
    depart_from = models.CharField(max_length=255)
    depart_air_code = models.CharField(max_length=3)
    depart_date_time = models.DateTimeField(default=timezone.now)
    arrive_into = models.CharField(max_length=255)
    arrive_air_code = models.CharField(max_length=3) 
    arrive_date_time = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.air_leg_name
    
    # def save(self, *args, **kwargs):
    #     return super(FlightLeg, self).save(*args, **kwargs)
    
    
    
class AirOption(models.Model):
    air_option_name = models.CharField(max_length=255)
    passenger_count = models.PositiveIntegerField()
    air_rate = models.DecimalField(max_digits=10, decimal_places=2) # per person
    air_fees = models.DecimalField(max_digits=10, decimal_places=2) # total fees
    air_taxes = models.DecimalField(max_digits=4, decimal_places=2) # % percentage
    air_discount = models.DecimalField(max_digits=10, decimal_places=2) # total discounts
    commit_deadline = models.DateTimeField(default=timezone.now)
    payment_deadline = models.DateTimeField(default=timezone.now)
    ticket_deadline = models.DateTimeField(default=timezone.now)
    utilize_deadline = models.DateTimeField(default=timezone.now)
    departure_date = models.DateTimeField(default=timezone.now)
    return_date = models.DateTimeField(default=timezone.now)
    flight_legs = models.ManyToManyField(FlightLeg, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.air_option_name
        
    # def save(self, *args, **kwargs):
    #     return super(AirOption, self).save(*args, **kwargs)
    
    

class GroupAir(models.Model):
    group_air_name = models.CharField(max_length=255)
    air_budget = models.DecimalField(max_digits=10, decimal_places=2)
    air_options = models.ManyToManyField(AirOption,  blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
  
  
    def __str__(self):
        return self.group_air_name
        
    # def save(self, *args, **kwargs):
    #     ''' On save, update timestamps '''
    #     return super(GroupAir, self).save(*args, **kwargs)       


##################################################################
### HOTEL MODELS 
##################################################################

class HotelOption(models.Model):
    hotel_option_name = models.CharField(max_length=255)
    hotel_name = models.CharField(max_length=255)
    room_type = models.CharField(max_length=255)
    check_in = models.DateTimeField(default=timezone.now)
    check_out = models.DateTimeField(default=timezone.now)
    number_of_nights = models.PositiveIntegerField()
    number_of_rooms = models.PositiveIntegerField() # per day
    hotel_rate = models.DecimalField(max_digits=10, decimal_places=2) # per room
    hotel_fees = models.DecimalField(max_digits=10, decimal_places=2) # total fees
    hotel_taxes = models.DecimalField(max_digits=4, decimal_places=2) # % percentage
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.hotel_option_name
        
    # def save(self, *args, **kwargs):
    #     return super(HotelOption, self).save(*args, **kwargs)
    
    
    
class GroupHotel(models.Model):
    group_hotel_name = models.CharField(max_length=255)
    hotel_budget = models.DecimalField(max_digits=10, decimal_places=2)
    hotel_options = models.ManyToManyField(HotelOption, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
  
    
    def __str__(self):
        return self.group_hotel_name   
        
    # def save(self, *args, **kwargs):
    #     return super(GroupHotel, self).save(*args, **kwargs)


##################################################################
### GROUND TRANSFER MODELS  
##################################################################

class GroundOption(models.Model):
    transfer_option_name = models.CharField(max_length=255)
    vendor_name = models.CharField(max_length=255)
    number_of_shuttles = models.PositiveIntegerField()
    transfer_rate = models.DecimalField(max_digits=10, decimal_places=2) # one way
    transfer_fees = models.DecimalField(max_digits=10, decimal_places=2) # total 
    transfer_taxes = models.DecimalField(max_digits=4, decimal_places=2) # % percentage
    pickup_date = models.DateTimeField(default=timezone.now)
    pickup_location = models.CharField(max_length=255)
    dropoff_date = models.DateTimeField(default=timezone.now)
    dropoff_location = models.CharField(max_length=255)
    service_details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.transfer_option_name

    # def save(self, *args, **kwargs):
    #     return super(GroundOption, self).save(*args, **kwargs)


class GroupTransfer(models.Model):
    group_transfer_name = models.CharField(max_length=255)
    ground_budget = models.DecimalField(max_digits=10, decimal_places=2)
    ground_options = models.ManyToManyField(GroundOption, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.group_transfer_name

    # def save(self, *args, **kwargs):
    #     return super(GroupTransfer, self).save(*args, **kwargs)

        
##################################################################
### ESTIMATE MODELS 
##################################################################

class Estimate(models.Model):
    
    PAYMENT_STATUS_CHOICES = (
        ('P', 'Pending'),
        ('R', 'Received'),
        ('C', 'Cancelled'),
    )
    
    ESTIMATE_STATUS_CHOICES = (
        ('P', 'Pending'),
        ('S', 'Submitted'),
        ('C', 'Cancelled'),
        ('R', 'Received'),
    )
    
    #CITY_STATE_JSON = simplejson.dumps({name:value})[1:-1] #remove '{' and '}'
    estimate_id = models.AutoField(primary_key=True)
    estimate_name = models.CharField(max_length=255)
    estimate_status = models.CharField(max_length=10, choices=ESTIMATE_STATUS_CHOICES)
    details = models.TextField()
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)
    number_of_people = models.PositiveIntegerField()
    agent = models.ForeignKey(get_user_model(),
    on_delete=models.CASCADE,
    )
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES)
    destination = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    #############################
    ###  Estimate ManytoMany  ###
    #############################
    group_air = models.ManyToManyField(GroupAir, blank = True)
    group_hotel = models.ManyToManyField(GroupHotel, blank = True)
    group_transfer = models.ManyToManyField(GroupTransfer, blank = True)
    
    
    def __str__(self):
        return self.estimate_name
    
    def get_absolute_url(self):
        return reverse('details_estimate', args=[str(self.id)])
    
    # def save(self, *args, **kwargs):
    #     new_obj = self.save(commit=False)
    #     new_obj.save()
        
    #     group_air = self.group_air
    #     group_air.save_m2m()
        
    #     group_hotel = self.group_hotel
    #     group_hotel.save_m2m()
        
    #     group_transfer = self.group_transfer
    #     group_transfer.save_m2m()
    #     return super(Estimate, self).save(*args, **kwargs)   
    


##################################################################
### THROUGH MODELS 
##################################################################

class AirHotelTransferEstimate(models.Model):
    account_id = models.AutoField(primary_key=True)
    account_name =  models.CharField(max_length=255)
    estimate = models.ForeignKey(Estimate, on_delete=models.CASCADE, blank=True, null=True)
    group_air = models.ManyToManyField(GroupAir, blank=True,)
    group_hotel = models.ManyToManyField(GroupHotel, blank=True,)
    group_transfer = models.ManyToManyField(GroupTransfer, blank=True,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

        
    
    def __str__(self):
        return self.account_name
        
    def get_absolute_url(self):
        return reverse('details_full_estimate', args=[str(self.id)])
    
        
    # def save(self, *args, **kwargs):
    #     return super(AirHotelTransferEstimate, self).save(*args, **kwargs)   