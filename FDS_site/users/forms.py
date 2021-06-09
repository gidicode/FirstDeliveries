from django import forms
from django.forms import ModelForm, Textarea, fields
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import  Anonymous, Customer, MakeRequest, MakeRequestCash, ForPayments, Shopping
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

    class Meta: #gives us a nested name space for configuration keeping it one place
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
    Choice_for_TP = forms.ChoiceField(label="Choice for Transportation", choices=OPTIONS2, widget=forms.RadioSelect, help_text="RANGE: Bike(N500 - N1500), Tricycle(N1000 - N2500), Van(negotiable) ")
    reciever_name = forms.CharField
    class Meta:
        model = MakeRequest
        fields = ['reciever_phone_number', 'Address_of_reciever',
                'reciever_name', 'Package_description', 'Your_location',
                'Choice_for_TP', 
                 ]

class adminform(forms.ModelForm): 
    class Meta:
        model = MakeRequest
        fields = '__all__'
        exclude = ['assigned']

class adminformCash(forms.ModelForm): 
    class Meta:
        model = MakeRequestCash
        fields = '__all__'
        exclude = ['assigned']

class adminformShopping(forms.ModelForm): 
    class Meta:
        model = Shopping
        fields = '__all__'
        exclude = ['assigned']
        
class Request_Cash(forms.ModelForm):
    OPTIONS2 = [
            ( "Van", "Van"),
            ("Bike", "Bike"),
            ( "Tricycle", "Tricycle (Keke)"),
            
    ]

    Choice_for_TP = forms.ChoiceField(label="Choice for Transportation", choices=OPTIONS2, widget=forms.RadioSelect, help_text="RANGE: Bike(N500 - N1500), Tricycle(N1000 - N2500), Van(negotiable) ")
    
    class Meta:
        model = MakeRequestCash
        fields = '__all__'
        exclude = ['type', 'Amount_Paid', 'customer', 'date_created', 'status', 'paid',  'order_id', 'assigned', ]

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

    Choice_for_TP = forms.ChoiceField(label="Choice for Transportation", choices=OPTIONS2, widget=forms.RadioSelect, help_text="RANGE: Bike(N500 - N1500), Tricycle(N1000 - N2500), Van(negotiable) ")
    class Meta:
        model = Anonymous 
        fields = [ 'Package_description', 'Your_phone_number', 'Your_location', 'email', 'Choice_for_TP',  ]

class AdminAnonForm(forms.ModelForm):
    
    class Meta:
        model = Anonymous
        fields = '__all__'
        exclude =['assigned']