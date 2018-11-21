from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.urls import reverse


############## AIR ##############

class FlightLeg(models.Model):
    #air_option = models.ForeignKey(AirOption, on_delete=models.CASCADE)
    airline = models.CharField(max_length=255)
    flight_num = models.PositiveIntegerField()
    depart_from = models.CharField(max_length=255)
    depart_air_code = models.CharField(max_length=3)
    depart_date_time = models.DateTimeField(default=timezone.now)
    arrive_into = models.CharField(max_length=255)
    arrive_air_code = models.CharField(max_length=3) 
    arrive_date_time = models.DateTimeField(default=timezone.now)

    
class AirOption(models.Model):
    #group_air = models.ForeignKey(GroupAir, on_delete=models.CASCADE)
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
    flight_legs = models.ManyToManyField(FlightLeg)
                

class GroupAir(models.Model):
    group_air_name = models.CharField(max_length=255)
    air_budget = models.DecimalField(max_digits=10, decimal_places=2)
    air_option = models.ManyToManyField(AirOption)
    
    def __str__(self):
        return self.group_air_name
        
        

############## HOTEL ##############

class HotelOption(models.Model):
    #group_hotel = models.ForeignKey(GroupHotel, on_delete=models.CASCADE)
    hotel_name = models.CharField(max_length=255)
    room_type = models.CharField(max_length=255)
    check_in = models.DateTimeField(default=timezone.now)
    check_out = models.DateTimeField(default=timezone.now)
    number_of_nights = models.PositiveIntegerField()
    number_of_rooms = models.PositiveIntegerField() # per day
    hotel_rate = models.DecimalField(max_digits=10, decimal_places=2) # per room
    hotel_fees = models.DecimalField(max_digits=10, decimal_places=2) # total fees
    hotel_taxes = models.DecimalField(max_digits=4, decimal_places=2) # % percentage
    
    def __str__(self):
        return self.hotel_name 
        

class GroupHotel(models.Model):
    group_hotel_name = models.CharField(max_length=255)
    hotel_budget = models.DecimalField(max_digits=10, decimal_places=2)
    hotel_options = models.ManyToManyField(HotelOption)

    def __str__(self):
        return self.group_hotel_name   
        
    
############## GROUND TRANSFER ##############

class GroundOption(models.Model):
    #group_transfer = models.ForeignKey(GroupTransfer, on_delete=models.CASCADE)
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
    
    
    def __str__(self):
        return self.vendor_name 


class GroupTransfer(models.Model):
    group_transfer_name = models.CharField(max_length=255)
    ground_budget = models.DecimalField(max_digits=10, decimal_places=2)
    ground_options = models.ManyToManyField(GroundOption)

    def __str__(self):
        return self.group_transfer_name




############## Estimate ##############

class Estimate(models.Model):
    
    PAYMENT_STATUS_CHOICES = (
        ('P', 'Pending'),
        ('R', 'Received'),
        ('C', 'Cancelled'),
    )
    
    #CITY_STATE_JSON = simplejson.dumps({name:value})[1:-1] #remove '{' and '}'
    
    id_num = models.AutoField(primary_key=True)
    account_num = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    details = models.TextField()
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)
    number_of_people = models.PositiveIntegerField()
    agent = models.ForeignKey(get_user_model(),
    on_delete=models.CASCADE,
    )
    
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICES)
    destination = models.CharField(max_length=255)
    
    #############################
    ###  Estimate ManytoMany  ###
    #############################
    group_air = models.ManyToManyField(GroupAir)
    group_hotel = models.ManyToManyField(GroupHotel)
    group_transfer = models.ManyToManyField(GroupTransfer)
    
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('estimate_detail', args=[str(self.id)])
        
        