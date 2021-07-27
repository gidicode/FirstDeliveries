from users.models import MakeRequest, MakeRequestCash, Shopping, Anonymous, Front_desk, Errand_service
from django.db import models
from django.core.validators import RegexValidator
from datetime import date
from django.utils import timezone

phone_regex = RegexValidator(regex=r'^\+?1?\d{9,12}$')

#all the type of delivery vechiles we have
class Fleets(models.Model):
    OPTIONS1 = [
                ("Bike", "Bike"),
                ( "Tricycle", "Tricycle"),
    ]

    fleet_plate_number = models.CharField(max_length=100, null=True)
    Tracker_id = models.CharField(max_length=100, null=True)
    Tracker_phone_num = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100, choices=OPTIONS1, null=True)
    vechile_name = models.CharField(max_length=100, null=True)    
    date_created = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self):
        return f"{self.fleet_plate_number}, {self.category}, {self.vechile_name}"

#driver full details
class RidersProfile(models.Model):
    attached_bike = models.OneToOneField(Fleets, on_delete=models.SET_NULL,  null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=17, null=True)
    Address = models.CharField(max_length = 100, null=True)
    verified_gurantor = models.BooleanField(default=False) 
    gurantor_name = models.CharField(max_length=100, null=True)
    gurantor_address = models.CharField(max_length=100, null=True)
    Riders_profile = models.CharField(max_length=100, null=True)
    busy = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.first_name}, {self.attached_bike}"
    
#updating a particular  delivery/attaching items to deliver for driver
class RidersDeliveries(models.Model):
    OPTIONS1 = [
                ("Pending", "Pending"),
                ("Delivered", "Delivered"),
                ( "Transfered", "Transfered"),
                ( "Canceled", "Canceled"),
    ]

    rider = models.ForeignKey(RidersProfile, null=True, on_delete =models.SET_NULL)
    veichle_used = models.ForeignKey(Fleets, null=True, on_delete =models.SET_NULL)
    cash_request = models.ForeignKey(MakeRequestCash, null=True, on_delete =models.SET_NULL, blank=True)
    e_payment_request = models.ForeignKey(MakeRequest, on_delete=models.SET_NULL,  null=True, blank=True)
    shopping = models.ForeignKey(Shopping, on_delete=models.SET_NULL,  null=True, blank=True)
    anonymous = models.ForeignKey(Anonymous, on_delete = models.SET_NULL, null=True, blank=True)
    errand = models.ForeignKey(Errand_service, on_delete = models.SET_NULL, null=True, blank=True)
    front_desk = models.ForeignKey(Front_desk, on_delete = models.SET_NULL, null=True, blank=True)
    staus = models.CharField(max_length=100, choices=OPTIONS1, default="Pending", null=True)
    dispute=models.CharField(max_length=100, blank=True)
    date_created = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self):
        return f"{self.rider}, {self.staus}, {self.e_payment_request}"

    class Meta:
        ordering = ('-date_created',)
