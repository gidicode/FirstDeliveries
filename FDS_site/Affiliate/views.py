from decimal import Context
from django.contrib.auth.models import User
from .models import *
from .forms import *
from users.models import Customer
from Management.models import Management_Notification
from django.shortcuts import redirect, render
from django.contrib import messages
from hashids import Hashids
from django.conf import settings

from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from users.decorators import *
from django.utils import timezone
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from django.views.decorators.http import require_http_methods    


def Affiliate_joinPage(request, user):    
    return render(request, "Affiliate/JoinAffiliate.html")

def Creating_referal_code(request, user):
    Marketer = Customer.objects.get(user = request.user)
    Referal_id = request.user.username
    try:
        Affiliate_Group.objects.create(
            Marketer = Marketer,
            Referal_ID = Referal_id
        )    
    except IntegrityError as e:
        e = f"'{Referal_id}' is already registered"
        return render(request, "Affiliate/AlreadyExist.html", {"message": e})
    return redirect('welcome_page', request.user.id)

def Welcome_page(request, user):
    affiliate_id  = Affiliate_Group.objects.get(Marketer = user)
    get_the_code = affiliate_id.Referal_ID
    return render(request, "Affiliate/Welcome_Page.html", {'Referal_id':get_the_code})

def Marketer_Dashboard(request, user):

    marketer = Affiliate_Group.objects.get(Marketer = user)
    all_customer_referral = Referrals.objects.filter(marketer = marketer)
    count_total_referals = all_customer_referral.count()
    all_time_earnings = marketer.Amount_Credited
    wallet_balance = marketer.Wallet_Balance
    payout_history = marketer.request_payout_set.filter(Payment_status = 'Pending').count()

    context = {
        'wallet_balance':wallet_balance,
        'all_time_earnings':all_time_earnings,
        'all_customer_referral':all_customer_referral,
        'count_total_referals':count_total_referals,
        'payout_history':payout_history,
    }
    return render(request, 'Affiliate/Marketer_Dashboard.html', context)

def Add_bank_account(request, user):    
    Makerter = Affiliate_Group.objects.get(Marketer = user)
    all_account = Makerter.bank_account_details_set.all()   
    print(all_account) 
    if request.method == 'POST':
        bank_form = Add_account(request.POST)
        if bank_form.is_valid():
            instance = bank_form.save(commit=False)
            instance.marketer = Makerter
            instance.save()
            return redirect('add-bank', user = user)
    else:
        bank_form = Add_account()

    context = {
        'all_account':all_account,
        'bank_form':bank_form,
    }
    return render(request, 'Affiliate/Add_bank.html', context)

@require_http_methods(['DELETE'])
def Delete_account(request, pk):
    Bank_Account_Details.objects.filter(id =pk).delete()
    return redirect('add-bank', user = request.user.pk)


def Request_Payout_form(request, user):
    Marketer = Affiliate_Group.objects.get(Marketer = user)
    wallet_balance = Marketer.Wallet_Balance
    
    if request.method == "POST":
        request_form = Request_Funds(user=request.user, data=request.POST)
        if request_form.is_valid():
            instance = request_form.save(commit=False)            
            instance.marketer = Marketer
            instance.save()       

            #Withdrawing the money
            Marketer.Wallet_Balance -= instance.Debit_amount
            Marketer.save()
            wallet_balance = Marketer.Wallet_Balance
            messages.success(request, f"""
                                Request Successful, Amount debited is {instance.Debit_amount}/n 
                                Wallet Balance is {wallet_balance}
                            """)

            return redirect('affiliate_dashboard', user = user)
    else:
        request_form = Request_Funds(user=request.user)
    context = {
        'request_form':request_form,
        'Marketer':Marketer,
    }
    return render(request, 'Affiliate/Request_payout.html', context)

def Payout_History_list(request, user):
    Marketer = Affiliate_Group.objects.get(Marketer = user)
    all_payout = Marketer.request_payout_set.all()
    return render(request, 'Affiliate/Payout_history.html', {'all_payout':all_payout},)

def Payout_History_Details(request, pk):
    payout_details = Request_Payout.objects.filter(id= pk)
    return render(request, 'Affiliate/Payout_history_details.html', {'payout_details':payout_details})

def Balance_status(request, user):
    marketer = Affiliate_Group.objects.get(Marketer = user )
    return render(request, 'Affiliate/Balance_status.html', {'Balance':marketer})

def Delivery_Details(request, pk):
    delivery_details = Referrals.objects.filter(id = pk)
    return render(request, 'Affiliate/DeliveryDetails.html', {'delivery_details':delivery_details})


#CheckingUser
