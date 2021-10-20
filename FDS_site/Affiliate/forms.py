from django.forms.widgets import Select
from django.http import request
from .models import Bank_Account_Details, Request_Payout, Affiliate_Group
from django import forms
from users.models import Customer
from django.forms import Textarea, fields, models
from django.core.exceptions import ValidationError
from django.views import View       

class Add_account(forms.ModelForm):        
    class Meta:
        model = Bank_Account_Details
        fields = ['Account_Number', 'Account_Name', 'Bank_Name']


class Checks(View):     
    def get_from_kwargs(self):
        kwargs = super(Checks, self).get_from_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class Request_Funds(forms.ModelForm):              
    def __init__(self, user, *args, **kwargs):    
        self.user = user                        
        super(Request_Funds, self).__init__(*args, **kwargs)          

    class Meta:
        model = Request_Payout
        fields = ['Debit_amount', 'Select_bank']
    
    def clean_Debit_amount(self):                      
        content = self.cleaned_data["Debit_amount"]   
        customer = Customer.objects.get(user = self.user)           
        Marketer = Affiliate_Group.objects.get(Marketer= customer)

        wallet_balance = Marketer.Wallet_Balance        

        if content < 1000 and wallet_balance > 1000:                
                raise ValidationError((f'"{content}" amount entered is below withdrawal limit, enter an amount starting from N1000'), params= {'content':content})
        elif content < 1000 and wallet_balance < 1000:
                raise ValidationError((f'You have a low wallet balance. N{wallet_balance}'), params= {'wallet_balance':wallet_balance})

        if content > wallet_balance:
            raise ValidationError((f'Insufficient Funds, Max amount you can request for with drawal is {wallet_balance}'),  params= {'wallet_balance':wallet_balance})       
        return content  


class Update_cash_out(forms.ModelForm): 
    Debit_amount = forms.CharField(widget=forms.TextInput(attrs={"readonly": "readonly"}))   
    class Meta:
        model = Request_Payout
        fields = ['Debit_amount','Payment_status', 'Amount_credited', 'Account_credited_to']  
              
    def clean(self):        
        cleaned_data = super().clean()            
        Debit_amount = int(cleaned_data.get('Debit_amount'))          
        Amount_credited = cleaned_data.get('Amount_credited')           
        print(Amount_credited)  

        if Amount_credited > Debit_amount:
            raise ValidationError((f'"{Amount_credited}" amount entered is aboved the requested amount "{Debit_amount}"'), params= {'Debit_amount':Debit_amount, 'Amount_credited':Amount_credited})
        elif Amount_credited < Debit_amount:
            raise ValidationError((f'"{Amount_credited}" amount entered is below the requested amount "{Debit_amount}"'), params= {'Debit_amount':Debit_amount, 'Amount_credited':Amount_credited})

        return cleaned_data
    

