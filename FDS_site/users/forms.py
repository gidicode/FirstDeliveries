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
    first_name = forms.CharField(label='First Name', max_length=15, required=True)
    last_name = forms.CharField(label='Last Name', max_length= 15, help_text='Last name', required=True)
    email = forms.EmailField(max_length=30, validators= [chk_email])
    phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$', 
                    help_text='Enter your phone number in this format 070xxxxxxxx',
                    validators= [chk_number] )
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email',  'phone_number', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name', max_length=15, required=True)
    last_name = forms.CharField(label='Last Name', max_length= 15, required=True)
    email = forms.EmailField(max_length=30)
    phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$', help_text='Enter your phone number in this format 070xxxxxxxx')

    class Meta: #gives us a nested name space for configuration keeping it one place
        model = Customer
        fields = ['email', 'first_name', 'last_name', 'phone_number']

#Profile Update Form
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model =Customer
        fields = ['image']


class OrderForm(forms.ModelForm): 
    class Meta:
        model = MakeRequest
        fields = [
            'reciever_name', 'Address_of_reciever', 
            'Package_description', 'Choice_for_TP', 
            'Your_location', 'reciever_phone_number',]

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
    
    class Meta:
        model = MakeRequestCash
        fields =['reciever_name', 'Address_of_reciever', 
            'Package_description', 'Choice_for_TP', 
            'Your_location', 'reciever_phone_number',]

class Shopping_Form(forms.ModelForm): 
    class Meta:
        model = Shopping
        fields ='__all__'
        exclude = ['customer', 'status', 'charge_id', 'date_created', 'amount_paid', 'Charge', 'Item_Cost', 'Total', 'Amount_Refunded', 'order_id', 'assigned']
        widgets = {
            'List_Items':Textarea(attrs={'cols': 80, 'row':20})
            
            }

class AnonForm(forms.ModelForm):
    class Meta:
        model = Anonymous 
        fields = ['Package_description', 'email', 'Choice_for_TP', 'Your_location', 'Your_phone_number']

class AdminAnonForm(forms.ModelForm):
    class Meta:
        model = Anonymous
        fields = '__all__'
        exclude =['assigned']