from PIL import Image
from django.db import models
from django.db.models.base import Model
from users.models import Customer
from django.utils import timezone
from django.core.validators import RegexValidator

phone_regex = RegexValidator(regex=r'^\+?1?\d{9,12}$')
# Create your models here.
class Fleets_PH(models.Model):
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
    attached = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.fleet_plate_number}, {self.category}, {self.vechile_name}"

class RidersProfile_PH(models.Model):
    attached_bike = models.OneToOneField(Fleets_PH, on_delete=models.SET_NULL,  null=True)
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

class MakeRequestCash_PH(models.Model):
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

    LOADING_CHOICE = [
                ("Loading", "Loading"),
                ( "Offloading", "Offloading"),
    ]
    
    customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
    riders = models.ForeignKey(RidersProfile_PH, null=True, on_delete= models.SET_NULL) 
    reciever_name = models.CharField(max_length=20, null=True)
    reciever_name2 = models.CharField(max_length=20, null=True, blank=True, verbose_name="Reciever Name (2)")
    reciever_name3 = models.CharField(max_length=20, null=True, blank=True, verbose_name="Reciever Name (3)")
    reciever_name4 = models.CharField(max_length=20, null=True, blank=True, verbose_name="Reciever Name (4)")
    reciever_name5 = models.CharField(max_length=20, null=True, blank=True, verbose_name="Reciever Name (5)")

    Address_of_reciever = models.CharField( max_length=100, null=True, verbose_name="Reciever Address")
    Address_of_reciever2 = models.CharField( max_length=100, null=True, blank=True, verbose_name="Reciever Address (2)")
    Address_of_reciever3 = models.CharField( max_length=100, null=True, blank=True, verbose_name="Reciever Address (3)")
    Address_of_reciever4 = models.CharField( max_length=100, null=True, blank=True, verbose_name="Reciever Address (4)")
    Address_of_reciever5 = models.CharField( max_length=100, null=True, blank=True, verbose_name="Reciever Address (5)")

    Package_description = models.CharField(max_length=100, null=True)
    Package_description2 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Package Description (2)")
    Package_description3 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Package Description (3)")
    Package_description4 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Package Description (4)")
    Package_description5 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Package Description (5)")

    Choice_for_TP = models.CharField(max_length=100, choices=OPTIONS1, default='Bike', null=True)
    Your_location = models.CharField(max_length=100, null=True, verbose_name="Pickup Location", help_text="The location we would pick the item from")
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    reciever_phone_number = models.CharField(validators=[phone_regex], max_length=17, null=True, verbose_name="Reciever Number",
                            help_text="This Format:070xxxxxxxx")
    reciever_phone_number2 = models.CharField(validators=[phone_regex], max_length=17,  blank=True, verbose_name="Reciever Number(2)") 
    reciever_phone_number3 = models.CharField(validators=[phone_regex], max_length=17, blank=True, verbose_name="Reciever Number(3)")
    reciever_phone_number4 = models.CharField(validators=[phone_regex], max_length=17, blank=True, verbose_name="Reciever Number(4)")
    reciever_phone_number5 = models.CharField(validators=[phone_regex], max_length=17, blank=True, verbose_name="Reciever Number(5)")

    date_created = models.DateTimeField(default=timezone.now, null=True)
    status = models.CharField(max_length=20, choices=STATUS, default='Pending', null=True)
    Loading_choice = models.CharField(max_length=100, null=True)
    paid = models.BooleanField(default=False)
    confirmed = models.BooleanField(default=False)
    Amount_Paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Amount_Payable = models.IntegerField(null= True, )
    order_id= models.CharField(max_length=10, null=True, default=0)
    assigned = models.BooleanField(default=False)
    Cancelation_Reason = models.CharField(max_length= 100, blank=True,  null=True)

    def __str__(self):
        return f'Customer:{self.customer}, Order ID:{self.order_id}'

    class Meta:
        ordering = ('-date_created',)


class Errand_service_PH(models.Model):
    STATUS = {
        ('Pending', 'Pending'),
        ('Purchase in Process', 'Purchase in Process'), 
        ('On Route for Delivery', 'On route for Delivery'),
        ('Delivered', 'Delivered')
    }

    category_choice = {
        ('Fuel', 'Fuel'),
        ('Bread', 'Bread'),
        ('Drugs', 'Drugs'),
        ('Gas', 'Gas'),
        ('Shawarma', 'Shawarma'),
        ('Pizza', 'Pizza'),
        ('Ice Cream', 'Ice Cream'),
        ('Fruits', 'Fruits'),
        ('Food', 'Food'),
        ('Others', 'Others'),
    }
    payment_choice = {        
        ('Card/Transfer', 'Card/Transfer')
    }
    Shawarma_type={
        ('Chicken', 'Chicken'),
        ('Beef', 'Beef'), 
        ('Special', 'Special'),
    }

    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    riders = models.ForeignKey(RidersProfile_PH, null=True, on_delete= models.SET_NULL)        
    category = models.CharField(max_length = 100, null=True, choices=category_choice)
    fuel_per_amount = models.IntegerField(null=True, verbose_name='Petrol Amount', help_text='Enter amount for fuel needed (Not litres)')
    payment_channel = models.CharField(max_length=100, choices=payment_choice, null=True, verbose_name='Payment Choice')
    Bread_brand_name = models.CharField(max_length=100,  null=True, verbose_name='Bread Name')
    Quantity = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, null=True, blank=True, help_text="Further description")
    Enter_amount = models.IntegerField(null=True, verbose_name='Amount', help_text='Cost to purchase items')
    Drug_store = models.CharField(max_length = 100, null= True,  verbose_name="Pharmacy Name", help_text="Write 'None' if None")
    Drug_store_location = models.CharField(max_length = 100, null= True, blank=True, verbose_name="Pharmacy Location")
    Drug_name = models.CharField(max_length = 200, null=True, help_text='Must be an over the counter drug')
    Gas_Quantity = models.IntegerField(null=True, help_text='Enter the quantity of gas you want refilled (1-12kg)')
    Shawarma_store = models.CharField(max_length=100, null=True, help_text="write None if None")
    Shawarma_desc = models.CharField(max_length=100, null=True, choices=Shawarma_type, verbose_name='Preference')
    pizza_store = models.CharField(max_length=100, null=True, verbose_name='Place of Purchase')
    Pizza_desc = models.CharField(max_length=100, null=True, verbose_name='Type of Pizza')
    ice_Cream_desc = models.CharField(max_length=100, null=True, verbose_name='Ice Cream Description')
    ice_Cream_store = models.CharField(max_length=100, null=True)
    fruits_description = models.CharField(max_length=100, null=True)
    fruits_purchase_store = models.CharField(max_length=100, null=True, blank=True, verbose_name='Purchase Location')
    medical_prescription = models.FileField(upload_to='medical_presciption', default= "default.jpg", null=True, blank=True, help_text='Alternatively upload precription')
    Food_Vendor = models.CharField(max_length=100, null=True)
    Food_description = models.CharField(max_length=200, null=True)
    your_location = models.CharField(max_length=100, null=True)
    order_id = models.CharField(max_length=7, null=True)
    Ps_reference = models.CharField(max_length=10, null=True)
    date_created = models.DateTimeField(default=timezone.now, null=True)
    assigned = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)
    confirmed = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
    profit = models.IntegerField(null= True, default=0)
    Amount_Paid = models.DecimalField(max_digits=10, null=True, decimal_places=2)
    Amount_Payable = models.IntegerField(null= True )
    status = models.CharField(max_length=100, choices=STATUS, default='Pending', null=True)

    def __str__(self):
        return f'{self.customer}, {self.order_id}, {self.category}'

    class Meta:
        ordering = ('-date_created',)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) 

        img = Image.open(self.medical_prescription.path)

        if img.height > 500 or img.width > 500:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.medical_prescription.path)

class Front_desk_PH(models.Model): 
    OPTIONS2 = [
        ("Bike", "Bike"),
        ( "Tricycle", "Tricycle (Keke)"),
        ( "Van", "Van"),
    ]
    
    delivery_type = [
        ('Pick & Drop', 'Pick & Drop'),
        ('Errand', 'Errand')
    ]

    STATUS = {
        ('Pending', 'Pending'),
        ('Canceled', 'Canceled'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    }

    cus_payment_method = {
        ('Card', 'Card'),
        ('Cash', 'Cash'),
        ('Transfer', 'Transfer'),
        ('Transfer & Cash', 'Transfer & Cash'),
        
    }

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)        
    riders = models.ForeignKey(RidersProfile_PH, null=True, blank=True, on_delete= models.SET_NULL)        
    customer_name = models.CharField( max_length=100, null=True, blank=True)
    item_description = models.CharField(max_length=200, null=True, blank=True)
    customer_location = models.CharField(max_length=100, null=True, verbose_name='Delivery Address'  , blank=True)
    delivery_destination = models.CharField(max_length=200, null=True, verbose_name='Receiver Location', blank=True)
    Reciever_phone_number = models.CharField(validators=[phone_regex], max_length=17, null=True, blank=True, verbose_name="Reciever Number")
    Receiver_name = models.CharField(max_length=100,blank=True, null=True)
    Customer_phone_number = models.CharField(validators=[phone_regex], max_length=17, null=True, blank=True, verbose_name="Customer Phone Number")
    Choice_for_TP = models.CharField(max_length=100, choices=OPTIONS2, null=True)
    Delivery_type = models.CharField(max_length=100, choices=delivery_type, null=True)
    Purchase_location = models.CharField(max_length=100,blank=True, null=True)
    Cancelation_Reason = models.CharField(max_length= 100,blank=True,  null=True)
    Quantity = models.CharField(max_length= 100,blank=True,  null=True)
    Enter_amount = models.IntegerField(null=True, verbose_name='Item Amount', blank=True, help_text='Cost to purchase items')
    Note = models.CharField(max_length=100, null=True, blank="True")
    date_created = models.DateTimeField(default=timezone.now, null=True)
    order_id = models.CharField(max_length=7, null=True)
    assigned = models.BooleanField(default=False)
    status = models.CharField(max_length=100, choices=STATUS, default="Pending", null=True)
    customer_payment_method = models.CharField(max_length=100, choices=cus_payment_method, null=True)
    payments_confirmed = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)
    confirmed = models.BooleanField(default=False)
    profit = models.IntegerField(null= True, default=0)
    Amount_Paid = models.DecimalField(max_digits=10, null= True, decimal_places=2)
    Amount_Payable = models.IntegerField(null= True, default=500)
    Total = models.IntegerField(null=True)   
    Delivery_Fee = models.IntegerField(null=True)

    def __str__(self):
        return f"  {self.customer}, {self.order_id}"
    class Meta:
        ordering = ('-date_created',)

class Shopping_PH(models.Model):
    STATUS = {
        ('Pending', 'Pending'),
        ('Canceled', 'Canceled'),
        ('At the Mall', 'At the Mall'),
        ('Delivered', 'Delivered'),
    }

    PAYMENT_CHOICE = {
        ('Card/Transfer', 'Card/Transfer')
    }

    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    riders = models.ForeignKey(RidersProfile_PH, null=True, on_delete= models.SET_NULL)        
    List_Items= models.TextField(max_length=500, null=True)
    Place_of_purchase = models.CharField(max_length=100, null=True, help_text='Specify a place for purchase if any.')
    Note = models.CharField(max_length=200, null=True, blank=True, help_text='Any further description')
    Address = models.CharField(max_length=200, null=True, verbose_name='Delivery Address')
    Amount = models.IntegerField(null= True, help_text= 'Enter an estimated amount, our charges Inclusive.' )
    Accept_Terms = models.BooleanField(default=False, help_text='Accept our Terms and Condition as regards this method')
    date_created = models.DateTimeField(default=timezone.now, null=True)
    status = models.CharField(max_length=20, choices=STATUS, default='Pending', null=True)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    Charge = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    Item_Cost = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    Total = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    Amount_Refunded = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    order_id= models.CharField(max_length=10, null=True)
    assigned = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)
    confirmed = models.BooleanField(default=False)
    payment_channel = models.CharField(max_length=100, choices= PAYMENT_CHOICE, null=True, verbose_name='Payment Choice')
    Cancelation_Reason = models.CharField(max_length= 100,blank=True,  null=True)
    Ps_reference = models.CharField(max_length=10, null=True)

    def __str__(self):
        return f'Customer:{self.customer}, Order ID:{self.order_id}'

    class Meta:
        ordering = ('-date_created',)

class PH_adminNotification(models.Model):
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

class Contact_of_customers(models.Model):
    Customer_name = models.CharField(max_length=200, null=True, blank=True)
    Customer_address = models.CharField(max_length=100, null=True, blank=True)
    Customer_contact = models.CharField(max_length=11, null=True, unique=True)
    Used_service_count = models.IntegerField(null=True)
    date_created = models.DateTimeField(default=timezone.now, null=True)
    