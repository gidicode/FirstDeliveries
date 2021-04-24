from django.db import models
import uuid
from django.contrib.auth.models import User
from PIL import Image
from django.core.validators import RegexValidator
from datetime import date
from django.utils import timezone
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=15, null=True)
    last_name = models.CharField(max_length=15, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    phone_number = models.CharField(validators=[phone_regex], max_length=17, null=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', null=True)
    email = models.EmailField(max_length=100, null=True)
    signup_confirmation = models.BooleanField(default=False)
    

    def __str__(self):
        return f'{self.user.username}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) 

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    

class MakeRequest(models.Model):
    OPTIONS1 = [
                ("Bike", "Bike"),
                ( "Tricycle", "Tricycle (Keke)"),
    ]

    STATUS = {
        ('Pending', 'Pending'),
        ('Canceled', 'Canceled'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    }

    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

    customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
    reciever_name = models.CharField(max_length=20, null=True)
    Address_of_reciever = models.CharField( max_length=50, null=True)
    Package_description = models.CharField(max_length=25, blank=True)
    Choice_for_TP = models.CharField(max_length=20, choices=OPTIONS1, default='Bike', null=True)
    Your_location = models.CharField(max_length=30, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    reciever_phone_number = models.CharField(validators=[phone_regex], max_length=17, null=True)
    date_created = models.DateTimeField(default=timezone.now, null=True)
    status = models.CharField(max_length=20, choices=STATUS, default='Pending', null=True)
    Amount = models.CharField(null=True, max_length=20, default=0)
    charge_id = models.CharField(max_length=100, null=True, validators=[alphanumeric])
    paid = models.BooleanField(default=False)
    order_id=models.CharField(null=True, max_length=20, default=0)
    

    def __str__(self):
        return f'{self.reciever_name, self.charge_id, self.paid, self.order_id, self.Choice_for_TP }'

    class Meta:
        ordering = ('-date_created',)


class MakeRequestCash(models.Model):
    OPTIONS1 = [
                ("Bike", "Bike"),
                ( "Tricycle", "Tricycle (Keke)"),
    ]

    STATUS = {
        ('Pending', 'Pending'),
        ('Canceled', 'Canceled'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    }

    customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
    reciever_name = models.CharField(max_length=20, null=True)
    Address_of_reciever = models.CharField( max_length=50, null=True)
    Package_description = models.CharField(max_length=100, null=True, blank=True)
    Choice_for_TP = models.CharField(max_length=20, choices=OPTIONS1, default='Bike', null=True)
    Your_location = models.CharField(max_length=30, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    reciever_phone_number = models.CharField(validators=[phone_regex], max_length=17, null=True)
    date_created = models.DateTimeField(default=timezone.now, null=True)
    status = models.CharField(max_length=20, choices=STATUS, default='Pending', null=True)
    paid = models.BooleanField(default=False)
    Amount_Paid = models.CharField(null=True, max_length=20, default=0)
    order_id =models.CharField(null=True, max_length=20, default=0)

    def __str__(self):
        return f'{self.reciever_name, self.reciever_phone_number, self.order_id}'

    class Meta:
        ordering = ('-date_created',)

        
class Shopping(models.Model):
    STATUS = {
        ('Pending', 'Pending'),
        ('Canceled', 'Canceled'),
        ('At the Mall', 'At the Mall'),
        ('Delivered', 'Delivered'),
    }

    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    List_Items= models.TextField(max_length=500, null=True, help_text='Fill in your list of items you want us to purchase and pick for you')
    Place_of_purchase = models.CharField(max_length=100, null=True, help_text='Specify a place of for purchase if any.')
    Note = models.CharField(max_length=200, null=True, help_text='Any further description')
    Address = models.CharField(max_length=200, null=True, help_text='Specify the address we would deliver Your items to')
    Amount=models.CharField(max_length=7, null=True, help_text= 'Enter an estimated amount, our charges Inclusive')
    Accept_Terms = models.BooleanField(default=False, help_text='Accept our Terms and Condition as regards this method')
    date_created = models.DateTimeField(default=timezone.now, null=True)
    status = models.CharField(max_length=20, choices=STATUS, default='Pending', null=True)
    amount_paid = models.CharField(max_length=100, null=True)
    Charge = models.CharField(max_length=100, null=True)
    Item_Cost = models.CharField(max_length=100, null=True)
    Total = models.CharField(max_length=100, null=True)
    Amount_Refunded = models.CharField(max_length=100, null=True)
    order_id=models.CharField(null=True, max_length=20, default=0)

    
    def __str__(self):
        return f'{self.customer, self.List_Items, self.Amount, self.order_id}'

    class Meta:
        ordering = ('-date_created',)


class ForPayments(models.Model):
    OPTION2 = {
        ('paid','paid'),
        ("declined","declined"),
    }

    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    For_online_payment = models.ForeignKey(MakeRequest, on_delete=models.SET_NULL, blank=True, null=True)
    For_shopping_payment = models.ForeignKey(Shopping, on_delete=models.SET_NULL, blank=True, null=True)
    For_cash_payment = models.ForeignKey(MakeRequestCash, on_delete=models.SET_NULL, blank=True, null=True)
    paystack_access_code = models.CharField(max_length=100, blank=True, null=True)
    paid = models.BooleanField(default=False)
    charge_id = models.CharField(max_length=100, null=True, validators=[alphanumeric])
    date_created = models.DateTimeField(default=timezone.now, null=True)
    money_paid = models.CharField(null=True, max_length = 10, default="None")
    order_id=models.CharField(null=True, max_length=20, default=0)
    Mode_of_Transport = models.CharField(null=True, max_length = 10, default="None")

    def __str__(self):
        return f'{self.customer, self.date_created, self.order_id, self.paid, self.Mode_of_Transport}'

class Delivered(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    Item_delivered = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(default=timezone.now, null=True)
    order_id=models.CharField(null=True, max_length=20, default=0)
    viewed = models.BooleanField(default=False)
    title = models.CharField(max_length=100, null=True)
    Message = models.TextField(max_length=500, null=True)

    def __str__(self):
        return f'{self.customer, self.date_created}'

class adminNotification(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    viewed = models.BooleanField(default=False)
    item_created = models.CharField(max_length = 200, null=True)
    date_created = models.DateTimeField(default=timezone.now, null=True)
    order_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'{self.customer, self.viewed}'

    

