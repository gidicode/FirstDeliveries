from django import forms
from django.forms import fields
from .models import  *


class fleetForm(forms.ModelForm):
    class Meta:
        model = Fleets
        fields = "__all__"

class ridersProfileForm(forms.ModelForm):
    class Meta:
        model = RidersProfile
        fields = "__all__"

from django.core.exceptions import ValidationError


def chk_cash(value):
    if RidersDeliveries.objects.filter(cash_request = value).exists():
        raise ValidationError((f'{value} already exist.'), params= {'value':value})

def chk_ePayment(value):
    if RidersDeliveries.objects.filter(e_payment_request = value).exists():
        raise ValidationError((f'{value} already exist.'), params= {'value':value})

def chk_shopping(value):
    if RidersDeliveries.objects.filter(shopping = value).exists():
        raise ValidationError((f'{value} already exist.'), params= {'value':value})

def chk_anonymous(value):
    if RidersDeliveries.objects.filter(anonymous = value).exists():
        raise ValidationError((f'{value} already exist.'), params= {'value':value})

class ridersdeliveryForm(forms.ModelForm):
    cash_request = forms.ModelChoiceField( queryset=MakeRequestCash.objects.all(), validators= [chk_cash], required=False )
    e_payment_request = forms.ModelChoiceField(queryset = MakeRequest.objects.all(), validators= [chk_ePayment], required=False )
    shopping = forms.ModelChoiceField( queryset=Shopping.objects.all(), validators= [chk_shopping],  required=False)
    anonymous = forms.ModelChoiceField( queryset=Anonymous.objects.all(), validators= [chk_anonymous],  required=False )

    class Meta:
        model = RidersDeliveries
        fields = "__all__"

class updateRidersDelivery(forms.ModelForm):
    class Meta:
        model = RidersDeliveries
        fields = ['staus', 'dispute']
