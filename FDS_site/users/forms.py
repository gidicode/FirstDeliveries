from re import template
from django import forms
from django.contrib.auth import models
from django.forms import ModelForm, Textarea, fields, widgets
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import  Anonymous, Customer, Errand_service, MakeRequest, MakeRequestCash, Shopping, Front_desk
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError



def chk_email(value):
    if User.objects.filter(email = value).exists():
        raise ValidationError((f'{value} already exist.'), params= {'value':value})

def chk_number(value):
    if Customer.objects.filter(phone_number = value).exists():
        raise ValidationError((f'{value} already exist.'), params= {'value':value})


class UserRegisterForm(UserCreationForm):
    locations = [
        ('--', '--'),
        ('Calabar', 'Calabar'),
        ('Port Harcourt', 'Port Harcourt')
    ]

    first_name = forms.CharField(label='', max_length=15, widget= forms.TextInput
                           (attrs={'placeholder':'First Name'}), required=True)
    last_name = forms.CharField(label='', max_length= 15, widget= forms.TextInput
                           (attrs={'placeholder':'Last Name'}), required=True)
    email = forms.EmailField(label='', max_length=30, validators= [chk_email], widget= forms.EmailInput
                           (attrs={'placeholder':'Email'}),)
    phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$', label='', required=True,                   
                    validators= [chk_number], widget= forms.TextInput(attrs={'placeholder':'070xxxxxxx'}))
    Alt_phone_num = forms.RegexField(regex=r'^\+?1?\d{9,15}$', label='', required = False,
                    validators= [chk_number], widget= forms.TextInput
                           (attrs={'placeholder':'2nd Phone Number'}))
    username = forms.CharField(label="", max_length=10, required=True, widget= forms.TextInput
                           (attrs={'placeholder':'Username'}) )
    TermsAgreement = forms.BooleanField(label='Terms & Agreement', required = True)    
    Location = forms.ChoiceField(label="Location", choices=locations, widget=forms.Select)
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder':'Create Password'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput (attrs={'placeholder':'Confirm Password'}))
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email',  'phone_number', 'Alt_phone_num', 'Location','password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username')

class UserUpdateForm(forms.ModelForm):    
    locations = [        
        ('Calabar', 'Calabar'),
        ('Port Harcourt', 'Port Harcourt')
    ]
    Location = forms.ChoiceField(label="Location", choices=locations, widget=forms.Select)
    class Meta:
        model = Customer
        fields = ['email', 'Alt_phone_num', 'Location']


class UpdateLocation(forms.ModelForm):
    locations = [        
        ('Calabar', 'Calabar'),
        ('Port Harcourt', 'Port Harcourt')
    ]
    Location = forms.ChoiceField(label="Location", choices=locations, widget=forms.Select)
    class Meta:
        model = Customer
        fields = ['Location']

#Profile Update Form
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model =Customer
        fields = ['image']


class OrderForm(forms.ModelForm): 
    OPTIONS2 = [
            ( "Van", "Van"),
            ("Bike", "Bike"),
            ( "Tricycle", "Tricycle (Keke)"),
    ]
    LOADING_CHOICE = [
            ("loading", "Loading"),
            ( "off Loading", "Off Loading"),
    ]

    Choice_for_TP = forms.ChoiceField(label="Choice for Transportation", choices=OPTIONS2, widget=forms.RadioSelect)
    reciever_phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$', label='Reciever Number',
                    min_length=11, widget= forms.TextInput)
    reciever_name2 = forms.CharField(label='', max_length=50, required=False, widget= forms.TextInput
                           (attrs={'placeholder':'Reciever Name (2)'}))
    reciever_name3 = forms.CharField(label='', max_length=50, required=False, widget= forms.TextInput
                           (attrs={'placeholder':'Reciever Name (3)'}))
    reciever_name4 = forms.CharField(label='', max_length=50, required=False, widget= forms.TextInput
                           (attrs={'placeholder':'Reciever Name (4)'}))
    reciever_name5 = forms.CharField(label='', max_length=15, required=False, widget= forms.TextInput
                           (attrs={'placeholder':'Reciever Name (5)'}))
    Address_of_reciever2 = forms.CharField(label='', max_length=15, required=False, widget= forms.TextInput
                           (attrs={'placeholder':'Address of reciever (2)'}))
    Address_of_reciever3 = forms.CharField(label='', max_length=50, required=False, widget= forms.TextInput
                           (attrs={'placeholder':'Address of reciever (3)'}))
    Address_of_reciever4 = forms.CharField(label='', max_length=50, required=False, widget= forms.TextInput
                           (attrs={'placeholder':'Addressof reciever (4)'}))
    Address_of_reciever5 = forms.CharField(label='', max_length=50, required=False, widget= forms.TextInput
                           (attrs={'placeholder':'Address of reciever (5)'}))                                                      
    Package_description2 = forms.CharField(label='', max_length=50, required=False, widget= forms.TextInput
                           (attrs={'placeholder':'Package description (2)'}))
    Package_description3 = forms.CharField(label='', max_length=50, required=False, widget= forms.TextInput
                        (attrs={'placeholder':'Package description (3)'}))   
    Package_description4 = forms.CharField(label='', max_length=50, required=False, widget= forms.TextInput
                        (attrs={'placeholder':'Package description (4)'}))   
    Package_description5 = forms.CharField(label='', max_length=15, required=False, widget= forms.TextInput
                        (attrs={'placeholder':'Packagen description (5)'}))    

    reciever_phone_number2 = forms.RegexField(regex=r'^\+?1?\d{9,15}$', required = False,
                    min_length=11, widget= forms.TextInput(attrs={'placeholder':'070xxxxxxxx'}))                                                
    reciever_phone_number2 = forms.RegexField(regex=r'^\+?1?\d{9,15}$', label='', required = False,
                    min_length=11, widget= forms.TextInput(attrs={'placeholder':'Reciever Phone Number'}))
    reciever_phone_number3 = forms.RegexField(regex=r'^\+?1?\d{9,15}$', label='', required = False,
                    min_length=11, widget= forms.TextInput(attrs={'placeholder':'Reciever Phone Number'}))
    reciever_phone_number4 = forms.RegexField(regex=r'^\+?1?\d{9,15}$', label='', required = False,
                    min_length=11,  widget= forms.TextInput(attrs={'placeholder':'Reciever Phone Number'}))
    reciever_phone_number5 = forms.RegexField(regex=r'^\+?1?\d{9,15}$', label='', required = False,
                    min_length=11, widget= forms.TextInput(attrs={'placeholder':'Reciever Phone Number'}))
    Loading_choice = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices = LOADING_CHOICE)
    class Meta:
        model = MakeRequest
        fields = '__all__'
        exclude = ['customer', 'date_created', 'status', 'Amount_paid', 'charge_id', 'paid', 'order_id', 'assigned', 'type', 'Amount_Payable']

class adminform(forms.ModelForm): 
    class Meta:
        model = MakeRequest
        fields = ['status', 'paid', 'confirmed', 'Amount_paid', ]

class adminformCash(forms.ModelForm): 
    class Meta:
        model = MakeRequestCash
        fields = ['status', 'Amount_Paid', 'confirmed',]

class adminformShopping(forms.ModelForm): 
    class Meta:
        model = Shopping
        fields = ['amount_paid', 'status', 'Charge', 'Item_Cost', 'Total', 'Amount_Refunded', 'confirmed']

class AdminAnonForm(forms.ModelForm):    
    class Meta:
        model = Anonymous
        fields = ['status', 'confirmed', 'Amount_Paid', 'receiver_name', 'receiver_address', 'receiver_contact' ]

class AdminErrandForm(forms.ModelForm):    
    class Meta:
        model = Errand_service
        fields = ['status', 'confirmed', 'Amount_Paid', 'profit' ]

class AdminFrontForm(forms.ModelForm):    
    class Meta:
        model = Front_desk
        fields = ['status', 'confirmed', 'Amount_Paid', 'profit' ]

class Request_Cash(forms.ModelForm):
    OPTIONS2 = [
            ( "Van", "Van"),
            ("Bike", "Bike"),
            ( "Tricycle", "Tricycle (Keke)"),
    ]
    LOADING_CHOICE = [
            ("loading", "Loading"),
            ( "off Loading", "Off Loading"),
    ]

    Choice_for_TP = forms.ChoiceField(label="Choice for Transportation", choices=OPTIONS2, widget=forms.RadioSelect)
    reciever_phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$', required=False, label='Reciever Number',
                    min_length=11, widget= forms.TextInput)
    reciever_name2 = forms.CharField(label='', max_length=50, required=False, widget= forms.TextInput
                           (attrs={'placeholder':'Reciever Name (2)'}))
    reciever_name3 = forms.CharField(label='', max_length=50, required=False, widget= forms.TextInput
                           (attrs={'placeholder':'Reciever Name (3)'}))
    reciever_name4 = forms.CharField(label='', max_length=50, required=False, widget= forms.TextInput
                           (attrs={'placeholder':'Reciever Name (4)'}))
    reciever_name5 = forms.CharField(label='', max_length=15, required=False, widget= forms.TextInput
                           (attrs={'placeholder':'Reciever Name (5)'}))
    Address_of_reciever3 = forms.CharField(label='', max_length=50, required=False, widget= forms.TextInput
                           (attrs={'placeholder':'Address of reciever (3)'}))
    Address_of_reciever3 = forms.CharField(label='', max_length=50, required=False, widget= forms.TextInput
                           (attrs={'placeholder':'Address of reciever (3)'}))
    Address_of_reciever4 = forms.CharField(label='', max_length=50, required=False, widget= forms.TextInput
                           (attrs={'placeholder':'Addressof reciever (4)'}))
    Address_of_reciever5 = forms.CharField(label='', max_length=50, required=False, widget= forms.TextInput
                           (attrs={'placeholder':'Address of reciever (5)'}))                                                      
    Package_description2 = forms.CharField(label='', max_length=50, required=False, widget= forms.TextInput
                        (attrs={'placeholder':'Package description (2)'}))   
    Package_description3 = forms.CharField(label='', max_length=50, required=False, widget= forms.TextInput
                        (attrs={'placeholder':'Package description (3)'}))   
    Package_description4 = forms.CharField(label='', max_length=50, required=False, widget= forms.TextInput
                        (attrs={'placeholder':'Package description (4)'}))   
    Package_description5 = forms.CharField(label='', max_length=15, required=False, widget= forms.TextInput
                        (attrs={'placeholder':'Packagen description (5)'}))    

    reciever_phone_number2 = forms.RegexField(regex=r'^\+?1?\d{9,15}$', label='', required = False,
                    min_length=11, widget= forms.TextInput(attrs={'placeholder':'Reciever Phone Number (2)'}))
    reciever_phone_number3 = forms.RegexField(regex=r'^\+?1?\d{9,15}$', label='', required = False,
                    min_length=11, widget= forms.TextInput(attrs={'placeholder':'Reciever Phone Number(3)'}))
    reciever_phone_number4 = forms.RegexField(regex=r'^\+?1?\d{9,15}$', label='', required = False,
                    min_length=11,  widget= forms.TextInput(attrs={'placeholder':'Reciever Phone Number(4)'}))
    reciever_phone_number5 = forms.RegexField(regex=r'^\+?1?\d{9,15}$', label='', required = False,
                    min_length=11, widget= forms.TextInput(attrs={'placeholder':'Reciever Phone Number(5)'}))
    Loading_choice = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices = LOADING_CHOICE)
    class Meta:
        model = MakeRequestCash
        fields = '__all__'
        exclude = ['type', 'Amount_Paid', 'customer', 'date_created', 'status', 'paid',  'order_id', 'assigned', 'Amount_Payable' ]


class Shopping_Form(forms.ModelForm):
    class Meta:
        model = Shopping
        fields =['List_Items', 'Place_of_purchase', 'Note', 'Address','payment_channel', 'Amount',]    
        widgets = {
            'List_Items':Textarea(attrs={'cols': 20, 'row':10})            
            }

class AnonForm(forms.ModelForm):
    OPTIONS2 = [
            ( "Van", "Van"),
            ("Bike", "Bike"),
            ( "Tricycle", "Tricycle (Keke)"),            
    ]
    locations = [
        ('--', '--'),
        ('Calabar', 'Calabar'),
        ('Port Harcourt', 'Port Harcourt')
    ]
    Package_description = forms.CharField(label='', max_length=100, widget= forms.TextInput
                           (attrs={'placeholder':'Package Description'}))
    Your_phone_number = forms.CharField(label='', max_length=100, widget= forms.TextInput
                           (attrs={'placeholder':'Your Phone Number'}))
    Your_location = forms.CharField(label='', max_length=100, widget= forms.TextInput
                           (attrs={'placeholder':'Your Location'}))                            
    Choice_for_TP = forms.ChoiceField(label="Choice for Transportation", choices=OPTIONS2, widget=forms.RadioSelect, help_text="RANGE: Bike(N500), Tricycle(N1000), Van(negotiable) ")
    Location = forms.ChoiceField(label="Location", choices=locations, widget=forms.Select)
    class Meta:
        model = Anonymous 
        fields = [ 'Package_description', 'Your_phone_number', 'Your_location', 'Location', 'Choice_for_TP',]
#
#
#Errand Service forms.

class Fuel_errand(forms.ModelForm):
    class Meta:
        model = Errand_service
        fields = ['fuel_per_amount', 'payment_channel', 'your_location']

class Gas_errand(forms.ModelForm):

    class Meta:
        model = Errand_service
        fields = ['Gas_Quantity', 'payment_channel', 'your_location']



def chk_drug(value):
    illegal_drugs = [
                    'Codeine', 'codeine', 'CODEINE', 'Codine', 
                    'codine', 'Codin', 'codin', 'Rohypnol', 'rohypnol', 
                    'refnol', 'Rohynol', 'rohynol', 'GHB', 'ghb', 'Ghb', 
                    'Ketamine', 'ketamine', 'methamphetamine', ' heroin', 'diazepam', 
                    'cough syrup', 'tramadol', 'Tramadol', 'TRAMADOL', 'MDMA', 
                    'ectasy', 'Ectasy' 'Lysergic acid diethylamide'
                    'LSD', 'Valium', 'morphine', 'Fentanyl', 'Ritalin', 
                    'ritalin', 'RITALIN', 'Oxymorphon', 'oxymorphon', 'Adderal'
                    ]
    if value in illegal_drugs:
        raise ValidationError((f'{value} falls under the drug abuse category and we cant purchase it.'), params= {'value':value})

class Drugs_errand(forms.ModelForm):
    Drug_name = forms.CharField(widget=forms.Textarea(attrs={'placeholder':"Enter list of specified drugs", 'row':3}), validators= [chk_drug],  )
    class Meta:

        model = Errand_service
        fields = ['Drug_store', 'Drug_store_location', 'Drug_name', 'medical_prescription', 'Enter_amount', 'payment_channel', 'your_location']

class Bread_errand(forms.ModelForm):
    class Meta:

        model = Errand_service
        fields = ['Bread_brand_name', 'Quantity', 'description', 'Enter_amount', 'payment_channel', 'your_location']

class Shawarma_errand(forms.ModelForm):
    class Meta:

        model = Errand_service
        fields = ['Shawarma_store', 'Shawarma_desc', 'description', 'Quantity',  'Enter_amount', 'payment_channel', 'your_location']

class Pizza_errand(forms.ModelForm):
    class Meta:

        model = Errand_service
        fields = ['pizza_store', 'Pizza_desc', 'description', 'Quantity',  'Enter_amount', 'payment_channel', 'your_location']

class Fruits_errand(forms.ModelForm):
    class Meta:
        fruits_description = forms.CharField(widget=forms.Textarea(attrs={'placeholder':"Name of fruit and the quantity", 'row':2}))
        model = Errand_service
        fields = [ 'fruits_purchase_store', 'fruits_description', 'Enter_amount', 'payment_channel', 'your_location']

class Icecream_errand(forms.ModelForm):
    class Meta:
        model = Errand_service
        fields = [ 'ice_Cream_store', 'ice_Cream_desc', 'Enter_amount', 'payment_channel', 'your_location']

class Food_errand(forms.ModelForm):
    Food_description = forms.CharField(widget=forms.Textarea(attrs={'placeholder':"Food: description; Quantity(plate)", 'row':2}))
    class Meta:
        model = Errand_service
        fields = [ 'Food_Vendor', 'Food_description', 'description', 'Enter_amount', 'payment_channel', 'your_location']

class Other_errand(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder':"Item description and specifications", 'row':2}))
    class Meta:
        model = Errand_service
        fields = [ 'description', 'Quantity', 'Enter_amount', 'payment_channel', 'your_location']

class Front_desk_pick(forms.ModelForm):
    class Meta:
        model = Front_desk
        fields = ['customer_name', 'Customer_phone_number', 'item_description', 'delivery_destination', 'Reciever_phone_number', 'customer_location', 'Amount_Payable', 'Choice_for_TP', 'Note' ]

class Front_desk_errand(forms.ModelForm):
    class Meta:
        model = Front_desk
        fields = ['customer_name', 'Customer_phone_number', 'Quantity', 'delivery_destination', 'item_description', 'Enter_amount', 'Reciever_phone_number', 'Purchase_location', 'customer_location', 'Note' ]

class CashierFormE(forms.ModelForm): 
    class Meta:
        model = MakeRequest
        fields = ['confirmed', 'Amount_paid']

class CashierFormCash(forms.ModelForm): 
    class Meta:
        model = MakeRequestCash
        fields = ['confirmed', 'Amount_Paid',]

class CashierFormShopping(forms.ModelForm): 
    class Meta:
        model = Shopping
        fields = ['confirmed', 'amount_paid', 'Charge', 'Item_Cost', 'Total', 'Amount_Refunded']

class CashierFormAnon(forms.ModelForm): 
    class Meta:
        model = Anonymous
        fields = ['confirmed', 'Amount_Paid']

class CashierFormErrand(forms.ModelForm): 
    class Meta:
        model = Errand_service
        fields = ['confirmed', 'profit', 'Amount_Paid']

class CashierFormFront(forms.ModelForm): 

    class Meta:
        model = Front_desk
        fields = ['confirmed', 'profit', 'Amount_Paid']

class FleetManagerUpdateE(forms.ModelForm):
    class Meta:
        model = MakeRequest
        fields= ['status']

class FleetManagerUpdateC(forms.ModelForm):
    class Meta:
        model = MakeRequestCash
        fields= ['status']

class FleetManagerUpdateS(forms.ModelForm):
    class Meta:
        model = Shopping
        fields= ['status']

class FleetManagerUpdateErr(forms.ModelForm):
    class Meta:
        model = Errand_service
        fields= ['status']

class FleetManagerUpdateA(forms.ModelForm):
    class Meta:
        model = Anonymous
        fields= ['status']

class FleetManagerUpdateF(forms.ModelForm):
    class Meta:
        model = Front_desk
        fields= ['status']