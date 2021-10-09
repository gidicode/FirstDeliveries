from django.contrib.messages.api import error
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.fields import DateTimeField
from django.utils.regex_helper import Choice
from users.models import Customer
from django.utils import timezone
# Create your models here.


class Affiliate_Group(models.Model):
    Marketer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    Referal_ID = models.CharField(unique=True, null=True, max_length=5, editable=False)
    Date_Joined = models.DateTimeField(default=timezone.now, editable=False, null = True, blank=True)
    Total_Referal = models.IntegerField(default=0, editable=False, null=True)
    Amount_Genreated = models.DecimalField(max_digits=6, editable=False, null = True, decimal_places=2)
    Amount_Credited = models.DecimalField(max_digits=6, editable=False, null = True, decimal_places=2)
    Wallet_Balance = models.DecimalField(max_digits=6, editable=False, null = True, decimal_places=2)
    Profit_Generated = models.DecimalField(max_digits=6, editable=False, null = True, decimal_places=2)

    def __str__(self):
        return f"{self.Marketer}, {self.Referal_ID}"

class Referrals(models.Model):
    Vehicle = [
                ("Bike", "Bike"),
                ( "Tricycle", "Tricycle (Keke)"),                
    ]

    STATUS = {
        ('Pending', 'Pending'),
        ('Canceled', 'Canceled'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    }

    Date_Time = models.DateTimeField(default=timezone.now, null=True)
    marketer = models.ForeignKey(Affiliate_Group, on_delete=models.CASCADE, null=True)
    Referal_ID = models.CharField(max_length=5, null=True, editable=False)
    Rider = models.ForeignKey('BikeControl.RidersProfile', null=True, on_delete= models.SET_NULL)        
    Choice_for_TP = models.CharField(max_length=10, choices = Vehicle, null=True)
    Delivery_status = models.CharField(max_length=20, editable=False, choices=STATUS, null=True)
    Trips_count = models.IntegerField(null= True, default=0,)
    Delivery_Fee = models.DecimalField(max_digits=6, decimal_places=2)
    Customer_percentage_profit = models.DecimalField(max_digits=6, decimal_places=2)
    FLLS_perentage_profit = models.DecimalField(max_digits=6, decimal_places=2)
    Order_ID = models.CharField(max_length=8, null=True)

    def __str__(self):
        return f"{self.marketer}, {self.Referal_ID}"

class Bank_Account_Details(models.Model):
    def Check_Len(value):
        if len(value) < 10:
            raise ValidationError(
                ('%(value) is less than 10 numbers, Please check and correct.'), params={'value':value},
            )   
        elif len(value) > 10:
            raise ValidationError(
                ('%(value) is more than 10 numbers, Please check and correct.'), params={'value':value},
            )
             
    marketer = models.ForeignKey(Affiliate_Group, on_delete=models.CASCADE, null=True)
    Account_Number = models.IntegerField(validators=[Check_Len], unique=True, editable=False)
    Account_Name = models.CharField(max_length = 100, null=True, unique=True, editable=False)
    Bank_Name = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return f"{self.Bank_Name}, {self.Account_Number}"

class Request_Payout(models.Model):
    STATUS = {
        ('Paid', 'Paid'),
        ('Canceled', 'Canceled'),
        ('Pending', 'Pending'),        
    }

    marketer = models.ForeignKey(Affiliate_Group, on_delete=models.CASCADE, null=True)
    Debit_amount = models.IntegerField(default=0, null=True)
    Select_bank = models.ForeignKey(Bank_Account_Details, on_delete=models.CASCADE, null=True, related_name="banks")
    Date_Requested = models.DateTimeField(default=timezone.now, null=True)
    Payment_status = models.CharField(choices=STATUS, default="Pending", max_length = 10, null=True)
    Transaction_ID = models.CharField(max_length=10, null=True, editable=False)
    Amount_credited = models.IntegerField(null=True)
    Account_credited_to = models.ForeignKey(Bank_Account_Details, on_delete=models.CASCADE, null=True)
    Payment_date = models.DateField(default=None, null=True)

    def __str__(self):
        return f"{self.marketer}, {self.Debit_amount}"