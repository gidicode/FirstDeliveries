from django import forms
from django.forms import ModelForm, Textarea
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import  Customer, MakeRequest, MakeRequestCash, ForPayments, Shopping
from django.core.validators import RegexValidator

class UserRegisterForm(UserCreationForm):
    OPTIONS = [
                ("Port Harcourt", "Port Harcourt"),
                ( "Cross Calabar", "Cross River"),
    ]
            
    first_name = forms.CharField(label='First Name', max_length=15, required=True)
    last_name = forms.CharField(label='Last Name', max_length= 15, help_text='Last name', required=True)
    state = forms.MultipleChoiceField(widget=forms.SelectMultiple, choices=OPTIONS)
    email = forms.EmailField(max_length=30)
    phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$', help_text='Enter your phone number in this format 070xxxxxxxx')

    
    class Meta: #gives us a nested name space for configuration keeping it one place
        model = User
        fields = ['first_name', 'last_name', 'username', 'email',  'state', 'phone_number', 'password1', 'password2']


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
        exclude = ['customer', 'status', 'charge_id', 'date_created', 'amount_paid', 'Charge', 'Item_Cost', 'Total', 'Amount_Refunded']
        widgets = {
            'List_Items':Textarea(attrs={'cols': 80, 'row':20})
            }
    