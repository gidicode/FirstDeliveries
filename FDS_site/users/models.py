from django.db import models
import uuid
from django.contrib.auth.models import User
from PIL import Image
from django.core.validators import RegexValidator
from datetime import date
from django.dispatch.dispatcher import receiver
from django.utils import timezone
from django.conf import settings


User = settings.AUTH_USER_MODEL


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=15, null=True)
    last_name = models.CharField(max_length=15, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    phone_number = models.CharField(validators=[phone_regex], max_length=17, null=True)
    Alt_phone_num = models.CharField(validators=[phone_regex], max_length=17, null=True, verbose_name="Phone Number (2nd)")
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
                ( "Van", "Van"),
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
    Amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    charge_id = models.CharField(max_length=100, null=True, validators=[alphanumeric])
    paid = models.BooleanField(default=False)
    order_id= models.CharField(max_length=10, null=True, default=0)
    assigned = models.BooleanField(default=False)
    

    def __str__(self):
        return f'Customer:{self.customer}, Order ID:{self.order_id}'

    class Meta:
        ordering = ('-date_created',)


class MakeRequestCash(models.Model):
    OPTIONS1 = [
                ("Bike", "Bike"),
                ( "Tricycle", "Tricycle (Keke)"),
                ( "Van", "Van"),
    ]

    STATUS = {
        ('Pending', 'Pending'),
        ('Canceled', 'Canceled'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    }
    
    Typeof = {
        ('Single', 'Single'),
        ('Multiple', 'Multiple'),
    }

    type = models.CharField(max_length=50, choices=Typeof, default='Single', null=True)
    customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
    reciever_name = models.CharField(max_length=20, null=True, blank=True)
    reciever_name2 = models.CharField(max_length=20, null=True, blank=True, verbose_name="Reciever Name (2)")
    reciever_name3 = models.CharField(max_length=20, null=True, blank=True, verbose_name="Reciever Name (3)")
    reciever_name4 = models.CharField(max_length=20, null=True, blank=True, verbose_name="Reciever Name (4)")
    reciever_name5 = models.CharField(max_length=20, null=True, blank=True, verbose_name="Reciever Name (5)")

    Address_of_reciever = models.CharField( max_length=100, null=True, blank=True, verbose_name="Reciever Address")
    Address_of_reciever2 = models.CharField( max_length=100, null=True, blank=True, verbose_name="Reciever Address (2)")
    Address_of_reciever3 = models.CharField( max_length=100, null=True, blank=True, verbose_name="Reciever Address (3)")
    Address_of_reciever4 = models.CharField( max_length=100, null=True, blank=True, verbose_name="Reciever Address (4)")
    Address_of_reciever5 = models.CharField( max_length=100, null=True, blank=True, verbose_name="Reciever Address (5)")

    Package_description = models.CharField(max_length=100, blank=True, null=True)
    Package_description2 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Package Description (2)")
    Package_description3 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Package Description (3)")
    Package_description4 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Package Description (4)")
    Package_description5 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Package Description (5)")

    Choice_for_TP = models.CharField(max_length=100, choices=OPTIONS1, default='Bike', null=True)
    Your_location = models.CharField(max_length=100, null=True, verbose_name="Pickup Location", help_text="The location we would pick the item from")
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    reciever_phone_number = models.CharField(validators=[phone_regex], max_length=17, null=True, verbose_name="Reciever Number", blank=True, 
                            help_text="This Format:070xxxxxxxx")
    reciever_phone_number2 = models.CharField(validators=[phone_regex], max_length=17, blank=True, verbose_name="Reciever Number(2)") 
    reciever_phone_number3 = models.CharField(validators=[phone_regex], max_length=17, blank=True, verbose_name="Reciever Number(3)", )
    reciever_phone_number4 = models.CharField(validators=[phone_regex], max_length=17, blank=True, verbose_name="Reciever Number(4)", )
    reciever_phone_number5 = models.CharField(validators=[phone_regex], max_length=17, blank=True, verbose_name="Reciever Number(5)", )

    date_created = models.DateTimeField(default=timezone.now, null=True)
    status = models.CharField(max_length=20, choices=STATUS, default='Pending', null=True)
    paid = models.BooleanField(default=False)
    Amount_Paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    order_id= models.CharField(max_length=10, null=True, default=0)
    assigned = models.BooleanField(default=False)

    def __str__(self):
        return f'Customer:{self.customer}, Order ID:{self.order_id}'

    class Meta:
        ordering = ('-date_created',)

class Anonymous(models.Model):
    OPTIONS2 = [
            ("Bike", "Bike"),
            ( "Tricycle", "Tricycle (Keke)"),
            ( "Van", "Van"),
    ]

    STATUS = {
        ('Pending', 'Pending'),
        ('Canceled', 'Canceled'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    }

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')

    Package_description = models.CharField(max_length=100, null=True, blank=True)
    Choice_for_TP = models.CharField(max_length=20, choices=OPTIONS2, default='Bike', null=True, 
                    help_text=" COST: Bike N500, Tricycle N1000")
    Your_location = models.CharField(max_length=100, null=True, verbose_name="Pickup Location", help_text="The location we would pick your item from")  
    Your_phone_number = models.CharField(validators=[phone_regex], max_length=17, null=True, verbose_name="Your Phone Number")
    date_created = models.DateTimeField(default=timezone.now, null=True)
    status = models.CharField(max_length=20, choices=STATUS, default='Pending', null=True)
    paid = models.BooleanField(default=False)
    email = models.EmailField(max_length=100, null=True)
    Amount_Paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    order_id= models.CharField(max_length=10, null=True, default=0)
    receiver_name = models.CharField(null=True, max_length=100, default = "Not Given" )
    receiver_address = models.CharField(null=True, max_length=100, default = "Not Given")
    receiver_contact = models.CharField(null=True, max_length=100, default = "Not Given")
    assigned = models.BooleanField(default=False)


    def __str__(self):
        return f"""
        Package Description -- {self.Package_description },\n 
        Pickup Location -- {self.Your_location},\n
        Your Contact -- {self.Your_phone_number},\n
        Mode of Transport -- {self.Choice_for_TP},\n
        Delivery Fee -- {self.Amount_Paid}
        """

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
    Amount= models.DecimalField(max_digits=10, decimal_places=2, help_text= 'Enter an estimated amount, our charges Inclusive', default=0)
    Accept_Terms = models.BooleanField(default=False, help_text='Accept our Terms and Condition as regards this method')
    date_created = models.DateTimeField(default=timezone.now, null=True)
    status = models.CharField(max_length=20, choices=STATUS, default='Pending', null=True)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Charge = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Item_Cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Amount_Refunded = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    order_id= models.CharField(max_length=10, null=True, default=0)
    assigned = models.BooleanField(default=False)

    
    def __str__(self):
        return f'Customer:{self.customer}, Order ID:{self.order_id}'

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
    order_id= models.CharField(max_length=10, null=True, default=0)
    Mode_of_Transport = models.CharField(null=True, max_length = 10, default="None")

    def __str__(self):
        return f' Customer:{self.customer}, Order ID:{self.order_id}'

class Delivered(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    Item_delivered = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(default=timezone.now, null=True)
    order_id= models.CharField(max_length=10, null=True, default=0)
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
    order_id= models.CharField(max_length=10, null=True, default=0)
    email = models.EmailField(max_length=100, null=True)

    def __str__(self):
        if self.customer == None:
         return f'Anonymous, {self.viewed, self.item_created}'
        else:
            return f'{self.customer, self.viewed}'