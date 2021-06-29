from re import template
from django import forms
from django.contrib.auth import models
from django.forms import ModelForm, Textarea, fields, widgets
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
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
    first_name = forms.CharField(label='', max_length=15, widget= forms.TextInput
                           (attrs={'placeholder':'First Name'}), required=True)
    last_name = forms.CharField(label='', max_length= 15, widget= forms.TextInput
                           (attrs={'placeholder':'Last Name'}), required=True)
    email = forms.EmailField(label='', max_length=30, validators= [chk_email], widget= forms.EmailInput
                           (attrs={'placeholder':'Email'}),)
    phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$', label='', required=True,
                    help_text='In this format 070xxxxxxxx',
                    validators= [chk_number], widget= forms.TextInput
                           (attrs={'placeholder':'070xxxxxxx'}))
    Alt_phone_num = forms.RegexField(regex=r'^\+?1?\d{9,15}$', label='', required = False,
                    validators= [chk_number], widget= forms.TextInput
                           (attrs={'placeholder':'Alternative Phone Number'}))
    username = forms.CharField(label="", max_length=10, required=True, widget= forms.TextInput
                           (attrs={'placeholder':'Username'}) )

    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email',  'phone_number', 'Alt_phone_num', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):    

    class Meta:
        model = Customer
        fields = ['email', 'Alt_phone_num']

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
    Choice_for_TP = forms.ChoiceField(label="Choice for Transportation", choices=OPTIONS2, widget=forms.RadioSelect, help_text="RANGE: Bike(N500), Tricycle(N1000), Van(negotiable) ")
    reciever_phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$', label='Reciever Number', required = False,
                    min_length=11, widget= forms.TextInput)
    reciever_phone_number2 = forms.RegexField(regex=r'^\+?1?\d{9,15}$', required = False,
                    min_length=11, widget= forms.TextInput)
    reciever_phone_number3 = forms.RegexField(regex=r'^\+?1?\d{9,15}$', required = False,
                    min_length=11, widget= forms.TextInput)
    reciever_phone_number4 = forms.RegexField(regex=r'^\+?1?\d{9,15}$', required = False,
                    min_length=11, widget= forms.TextInput)
    reciever_phone_number4 = forms.RegexField(regex=r'^\+?1?\d{9,15}$', required = False,
                    min_length=11, widget= forms.TextInput)
    Loading_choice = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices = LOADING_CHOICE)
    class Meta:
        model = MakeRequest
        fields = '__all__'
        exclude = ['customer', 'date_created', 'status', 'Amount', 'charge_id', 'paid', 'order_id', 'assigned', 'type', 'Amount_Payable']

class adminform(forms.ModelForm): 
    class Meta:
        model = MakeRequest
        fields = ['status']

class adminformCash(forms.ModelForm): 
    class Meta:
        model = MakeRequestCash
        fields = ['status', 'Amount_Paid', 'paid']

class adminformShopping(forms.ModelForm): 
    class Meta:
        model = Shopping
        fields = ['amount_paid', 'status', 'Charge', 'Item_Cost', 'Total', 'Amount_Refunded']
        
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

    Choice_for_TP = forms.ChoiceField(label="Choice for Transportation", choices=OPTIONS2, widget=forms.RadioSelect, help_text="PRICE RANGE: Bike(N500), Tricycle(N1000), Van(negotiable) ")
    reciever_phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$', label='Reciever Number', required = False,
                    min_length=11, widget= forms.TextInput)
    reciever_phone_number2 = forms.RegexField(regex=r'^\+?1?\d{9,15}$', required = False,
                    min_length=11, widget= forms.TextInput)
    reciever_phone_number3 = forms.RegexField(regex=r'^\+?1?\d{9,15}$', required = False,
                    min_length=11, widget= forms.TextInput)
    reciever_phone_number4 = forms.RegexField(regex=r'^\+?1?\d{9,15}$', required = False,
                    min_length=11, widget= forms.TextInput)
    reciever_phone_number4 = forms.RegexField(regex=r'^\+?1?\d{9,15}$', required = False,
                    min_length=11, widget= forms.TextInput)
    Loading_choice = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices = LOADING_CHOICE)
    class Meta:
        model = MakeRequestCash
        fields = '__all__'
        exclude = ['type', 'Amount_Paid', 'customer', 'date_created', 'status', 'paid',  'order_id', 'assigned', 'Amount_Payable' ]


class Shopping_Form(forms.ModelForm):
    OPTIONS2 = [
            ( "Van", "Van"),
            ("Bike", "Bike"),
            ( "Tricycle", "Tricycle (Keke)"),
            
    ]

    Choice_for_TP = forms.ChoiceField(label="Choice for Transportation", choices=OPTIONS2, widget=forms.RadioSelect, help_text="RANGE: Bike(N500 - N1500), Tricycle(N1000 - N2500), Van(negotiable) ") 
    class Meta:
        model = Shopping
        fields ='__all__'
        exclude = ['customer', 'status', 'charge_id', 'date_created', 'amount_paid', 'Charge', 'Item_Cost', 'Total', 'Amount_Refunded', 'order_id', 'assigned']
        widgets = {
            'List_Items':Textarea(attrs={'cols': 80, 'row':20})
            
            }

class AnonForm(forms.ModelForm):
    OPTIONS2 = [
            ( "Van", "Van"),
            ("Bike", "Bike"),
            ( "Tricycle", "Tricycle (Keke)"),
            
    ]

    Choice_for_TP = forms.ChoiceField(label="Choice for Transportation", choices=OPTIONS2, widget=forms.RadioSelect, help_text="RANGE: Bike(N500), Tricycle(N1000), Van(negotiable) ")
    class Meta:
        model = Anonymous 
        fields = [ 'Package_description', 'Your_phone_number', 'Your_location', 'email', 'Choice_for_TP',  ]

class AdminAnonForm(forms.ModelForm):
    
    class Meta:
        model = Anonymous
        fields = '__all__'
        exclude =['assigned']

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
                    'Codeine', 'Rohypnol', 'GHB', 
                    'ghb', 'Ghb', 'Ketamine', 'ketamine', 
                    'methamphetamine', ' heroin', 'diazepam', 
                    'cough syrup', 'tramadol', 'MDMA', 
                    'ectasy', 'Ectasy' 'Lysergic acid diethylamide'
                    'LSD', 'Valium', 'morphine', 'Fentanyl', 'Ritalin',
                    'Oxymorphon', 'oxymorphon', 'Adderal'
                    ]
    if value in illegal_drugs:
        raise ValidationError((f'{value} falls under the drug abuse category and we cant purchase it.'), params= {'value':value})

class Drugs_errand(forms.ModelForm):
    Drug_name = forms.CharField(widget=forms.Textarea(attrs={'placeholder':"Enter list of specified drugs", 'row':3}), validators= [chk_drug],  )
    class Meta:

        model = Errand_service
        fields = ['Drug_store', 'Drug_name', 'medical_prescription', 'Enter_amount', 'payment_channel', 'your_location']

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