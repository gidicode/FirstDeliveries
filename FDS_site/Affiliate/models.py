from datetime import time
from django.core.exceptions import ValidationError
from django.db import models
from users.models import Customer
from django.utils import timezone
from decimal import Decimal


# Create your models here.
class Affiliate_Group(models.Model):
    Marketer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    Referal_ID = models.CharField(unique=True, null=True, max_length=5, editable=False)
    Date_Joined = models.DateTimeField(default=timezone.now, editable=False, null = True, blank=True)
    Total_Referal = models.IntegerField(default=0, editable=False, null=True)
    Amount_Genreated = models.DecimalField(max_digits=20, default=Decimal('0.00'), editable=True, null = True, decimal_places=2)
    Amount_Credited = models.DecimalField(max_digits=20, default=Decimal('0.00'), editable=True, null = True, decimal_places=2)
    cashed_out = models.DecimalField(max_digits=20, default=Decimal('0.00'), editable=True, null = True, decimal_places=2)
    Wallet_Balance = models.DecimalField(max_digits=20, default=Decimal('0.00'), editable=True, null = True, decimal_places=2)
    Tempoary_wallet_balance = models.DecimalField(max_digits=20, default=Decimal('0.00'), editable=True, null = True, decimal_places=2)
    Profit_Generated = models.DecimalField(max_digits=20, default=Decimal('0.00'), editable=True, null = True, decimal_places=2)

    def __str__(self):
        return f"{self.Referal_ID}"     
      
            
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
    Delivery_Fee = models.DecimalField(max_digits=6, null=True, decimal_places=2)
    Customer_percentage_profit = models.DecimalField(max_digits=6, null=True, decimal_places=2)
    FLLS_perentage_profit = models.DecimalField(max_digits=6, null=True, decimal_places=2)
    Order_ID = models.CharField(max_length=8, null=True)
    Completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.marketer}, {self.Referal_ID}"
    
    class Meta:
        ordering = ('-Date_Time',)

class Bank_Account_Details(models.Model):
    def Check_Len(value):
        if len(str(value)) < 10:
            raise ValidationError(
                ('%(value)  is less than 10 numbers, Please check and correct.'), params={'value':value},
            )   
        elif len(str(value)) > 10:
            raise ValidationError(
                ('%(value)  is more than 10 numbers, Please check and correct.'), params={'value':value},
            )              
    marketer = models.ForeignKey(Affiliate_Group, on_delete=models.CASCADE, null=True)
    Account_Number = models.IntegerField(validators=[Check_Len], unique=True)
    Account_Name = models.CharField(max_length = 100, null=True, unique=False)
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
    Amount_credited = models.IntegerField(null=True, verbose_name="Amount to pay", help_text="Dont input an amount more or less than the debit amount")
    Account_credited_to = models.ForeignKey(Bank_Account_Details, on_delete=models.CASCADE, null=True)
    Payment_date = models.DateField(default=None, null=True)

    def __str__(self):
        return f"{self.marketer}, {self.Debit_amount}"

    class Meta:
        ordering = ('-Date_Requested',)

class Notification(models.Model):
    marketer = models.ForeignKey(Affiliate_Group, on_delete=models.CASCADE, null=True)
    message = models.CharField(max_length=200, null=True)
    viewed = models.BooleanField(default = False)
    date = models.DateTimeField(default=timezone.now, null=True)

class Notification_admin(models.Model):
    marketer = models.ForeignKey(Affiliate_Group, on_delete=models.CASCADE, null=True)
    message = models.CharField(max_length=200, null=True)
    viewed = models.BooleanField(default = False)
    date = models.DateTimeField(default=timezone.now, null=True)