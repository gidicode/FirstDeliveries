from django.http import request
from .models import Affiliate_Group
from django.core.exceptions import ValidationError

def Check_balance(value):
    Marketer = Affiliate_Group.objects.get(Marketer= request.user)
    wallet_balance = Marketer.Wallet_Balance
    if value < 1000:                
            raise ValidationError((f'Your are not eligble to request for funds.'), params= {'value':value})
    elif value > wallet_balance:
        raise ValidationError((f'{value} Insufficient Funds.'), params= {'value':value})                