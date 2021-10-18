from decimal import Context
from django.core import paginator
from .models import *
from .forms import *
from django.db.models import Sum
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
from datetime import datetime
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
    
    paginator = Paginator(all_customer_referral, 5)
    page_number = request.GET.get('page')
    customer_paginated_referrals = paginator.get_page(page_number)    

    context = {
        'wallet_balance':wallet_balance,
        'all_time_earnings':all_time_earnings,
        'all_customer_referral':all_customer_referral,
        'count_total_referals':count_total_referals,
        'customer_paginated_referrals':customer_paginated_referrals,
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

#COMPANY-DASHBOARD

def Dashboard_Affilite(request):    
    return render(request, 'Affiliate/Affiliate_dashboard.html')

def Dashboad_summary(request):
    Affiliate_customers = Affiliate_Group.objects.all()    
    today = datetime.now().date()    
    
    Total_Deliveries = Referrals.objects.filter(Delivery_status = "Delivered").count()
    Pending_Deliveries = Referrals.objects.filter(Delivery_status = 'Pending').count()
    pending_payout = Request_Payout.objects.filter(Payment_status = "Pending").count()
    Total_delivery_fee = Referrals.objects.aggregate(Sum('Delivery_Fee'))
    Credited_to_customers = Referrals.objects.aggregate(Sum('Customer_percentage_profit'))
    Total_cash_out = Request_Payout.objects.aggregate(Sum('Amount_credited'))
    Balance_to_marketers = Affiliate_customers.aggregate(Sum('Wallet_Balance'))
    Total_profit = Affiliate_customers.aggregate(Sum('Profit_Generated'))

    #filtering to amount made today    
    Total_amount_made_today = Referrals.objects.filter(Date_Time__date = today).aggregate(Sum('Delivery_Fee'))    
    Total_deliveries_today = Referrals.objects.filter(Date_Time__date = today).count()

    context = {     
        'Affiliate_customers':Affiliate_customers,
        'Total_Deliveries':Total_Deliveries,
        'Pending_Deliveries':Pending_Deliveries,
        'pending_payout':pending_payout,
        'Total_delivery_fee':Total_delivery_fee,
        'Credited_to_customers':Credited_to_customers,
        'Total_cash_out':Total_cash_out,
        'Balance_to_marketers':Balance_to_marketers,
        'Total_profit':Total_profit,
        'Total_amount_made_today':Total_amount_made_today,
        'Total_deliveries_today':Total_deliveries_today,
    }
    return render(request, 'Affiliate/Dashboard_Summary.html', context)

def Deliveries_list(request):
    all_referrals = Referrals.objects.all()
    context = {
        'all_referrals': all_referrals,
    }
    return render(request, 'Affiliate/Delivery_list.html', context)

def Customer_List(request):
    return render(request, 'Affiliate/Customers_List.html')

def Payout_List(request):
    return render(request, 'Affiliate/Payout_list_details.html')