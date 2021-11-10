from decimal import Context
from django.core import paginator
from .models import *
from .forms import *
from django.db.models import Sum
from users.models import Customer
from django.shortcuts import redirect, render
from django.contrib import messages
from hashids import Hashids
from django.conf import settings
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from users.decorators import *
from datetime import datetime
from django.utils import timezone
from django.db import IntegrityError
from django.views.decorators.http import require_http_methods 
from .decorators import *   

@login_required(login_url='login')
@allowed_user(allowed_roles=[
        'admin',
        'FLLS', 'MANAGEMENT', 'ICT',
        'MANAGEMENT_OPERATION', 'OPERATIONS',
        'FLM MANAGER', 'TANK', 'IWH', 'MANAGEMENT_RUNYI', 
        'MANAGEMENT_MANAGER', 'MANAGEMENT_OPERATION',
        'MANAGEMENT_CHAIRMAN', 'Marketing',
        'Fleet Manager', 'Front Desk', 
        'MANAGEMENT_ADMIN', 'Fleet Manager', 
        'Front Desk', 'Cashier', 'customer', 
        'Affiliate_customers', 'Affiliate_admin'])
def Affiliate_joinPage(request, user):    
    return render(request, "Affiliate/JoinAffiliate.html")


@login_required(login_url='login')
@allowed_user(allowed_roles=[
        'admin',
        'FLLS', 'MANAGEMENT', 'ICT',
        'MANAGEMENT_OPERATION', 'OPERATIONS',
        'FLM MANAGER', 'TANK', 'IWH', 'MANAGEMENT_RUNYI', 
        'MANAGEMENT_MANAGER', 'MANAGEMENT_OPERATION',
        'MANAGEMENT_CHAIRMAN', 'Marketing',
        'Fleet Manager', 'Front Desk', 
        'MANAGEMENT_ADMIN', 'Fleet Manager', 
        'Front Desk', 'Cashier', 'customer', 
        'Affiliate_customers', 'Affiliate_admin'])
def Creating_referal_code(request, user):    
    Marketer = Customer.objects.get(user = request.user)
    Referal_id = request.user.username.upper()
    check_customer = Affiliate_Group.objects.filter(Referal_ID=Referal_id).exists()    
    if check_customer == False:        
        try:
            Affiliate_Group.objects.create(
                Marketer = Marketer,
                Referal_ID = Referal_id
            )
            group = Group.objects.get(name='Affiliate_customers')
            group.user_set.add(user)
            marketter = Affiliate_Group.objects.get(Referal_ID = Referal_id)
            Notification_admin.objects.create(
                    marketer = marketter,
                    message = f"{marketter} Just joined the affiliate program"
                )  
        except IntegrityError as e:
            e = f"'{Referal_id}' is already registered"
            return render(request, "Affiliate/AlreadyExist.html", {"message": e})
        return redirect('welcome_page', request.user.id)
    else:
        return redirect('affiliate_dashboard', request.user.id)

@login_required(login_url='login')
@allowed_user(allowed_roles=[
        'admin',
        'FLLS', 'MANAGEMENT', 'ICT',
        'MANAGEMENT_OPERATION', 'OPERATIONS',
        'FLM MANAGER', 'TANK', 'IWH', 'MANAGEMENT_RUNYI', 
        'MANAGEMENT_MANAGER', 'MANAGEMENT_OPERATION',
        'MANAGEMENT_CHAIRMAN', 'Marketing',
        'Fleet Manager', 'Front Desk', 
        'MANAGEMENT_ADMIN', 'Fleet Manager', 
        'Front Desk', 'Cashier', 'customer', 
        'Affiliate_customers', 'Affiliate_admin'])
def Welcome_page(request, user):
    customer = Customer.objects.get(user = request.user)
    print(customer)
    affiliate_id  = Affiliate_Group.objects.get(Marketer = customer)
    get_the_code = affiliate_id.Referal_ID
    return render(request, "Affiliate/Welcome_Page.html", {'Referal_id':get_the_code})

@login_required(login_url='login')
@allowed_user(allowed_roles=[
        'admin',
        'FLLS', 'MANAGEMENT', 'ICT',
        'MANAGEMENT_OPERATION', 'OPERATIONS',
        'FLM MANAGER', 'TANK', 'IWH', 'MANAGEMENT_RUNYI', 
        'MANAGEMENT_MANAGER', 'MANAGEMENT_OPERATION',
        'MANAGEMENT_CHAIRMAN', 'Marketing',
        'Fleet Manager', 'Front Desk', 
        'MANAGEMENT_ADMIN', 'Fleet Manager', 
        'Front Desk', 'Cashier', 'customer', 
        'Affiliate_customers', 'Affiliate_admin'])
def Marketer_Dashboard(request, user):
    customer = Customer.objects.get(user = request.user)
    marketer = Affiliate_Group.objects.get(Marketer = customer)
    all_customer_referral = Referrals.objects.filter(marketer = marketer)
    count_total_referals = all_customer_referral.count()
    all_time_earnings = marketer.Amount_Credited
    wallet_balance = marketer.Wallet_Balance
    tempoary_balance = marketer.Tempoary_wallet_balance
    payout_history = marketer.request_payout_set.filter(Payment_status = 'Pending').count()
    
    paginator = Paginator(all_customer_referral, 5)
    page_number = request.GET.get('page')
    customer_paginated_referrals = paginator.get_page(page_number)    

    notification = marketer.notification_set.filter(viewed = False)
    
    context = {
        'notification':notification,
        'marketer':marketer,
        'wallet_balance':wallet_balance,
        'all_time_earnings':all_time_earnings,
        'all_customer_referral':all_customer_referral,
        'count_total_referals':count_total_referals,
        'customer_paginated_referrals':customer_paginated_referrals,
        'payout_history':payout_history,
        'tempoary_balance':tempoary_balance,
    }
    return render(request, 'Affiliate/Marketer_Dashboard.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=[
        'admin',
        'FLLS', 'MANAGEMENT', 'ICT',
        'MANAGEMENT_OPERATION', 'OPERATIONS',
        'FLM MANAGER', 'TANK', 'IWH', 'MANAGEMENT_RUNYI', 
        'MANAGEMENT_MANAGER', 'MANAGEMENT_OPERATION',
        'MANAGEMENT_CHAIRMAN', 'Marketing',
        'Fleet Manager', 'Front Desk', 
        'MANAGEMENT_ADMIN', 'Fleet Manager', 
        'Front Desk', 'Cashier', 'customer', 
        'Affiliate_customers', 'Affiliate_admin'])
def Add_bank_account(request, user):    
    customer = Customer.objects.get(user = request.user)
    Makerter = Affiliate_Group.objects.get(Marketer = customer)
    all_account = Makerter.bank_account_details_set.all()      
    if request.method == 'POST':
        bank_form = Add_account(request.POST)
        if bank_form.is_valid():
            instance = bank_form.save(commit=False)
            instance.marketer = Makerter
            instance.save()
            Notification_admin.objects.create(
                marketer = Makerter,
                message = f"{Makerter} Just added an account number, {instance}"
            )
            return redirect('add-bank', user = user)
    else:
        bank_form = Add_account()

    context = {
        'all_account':all_account,
        'bank_form':bank_form,
    }
    return render(request, 'Affiliate/Add_bank.html', context)

@require_http_methods(['DELETE'])
@login_required(login_url='login')
@allowed_user(allowed_roles=[
        'admin',
        'FLLS', 'MANAGEMENT', 'ICT',
        'MANAGEMENT_OPERATION', 'OPERATIONS',
        'FLM MANAGER', 'TANK', 'IWH', 'MANAGEMENT_RUNYI', 
        'MANAGEMENT_MANAGER', 'MANAGEMENT_OPERATION',
        'MANAGEMENT_CHAIRMAN', 'Marketing',
        'Fleet Manager', 'Front Desk', 
        'MANAGEMENT_ADMIN', 'Fleet Manager', 
        'Front Desk', 'Cashier', 'customer', 
        'Affiliate_customers', 'Affiliate_admin'])
def Delete_account(request, pk):
    Bank_Account_Details.objects.filter(id =pk).delete()
    
    return redirect('add-bank', user = request.user.pk)


@login_required(login_url='login')
@allowed_user(allowed_roles=[
        'admin',
        'FLLS', 'MANAGEMENT', 'ICT',
        'MANAGEMENT_OPERATION', 'OPERATIONS',
        'FLM MANAGER', 'TANK', 'IWH', 'MANAGEMENT_RUNYI', 
        'MANAGEMENT_MANAGER', 'MANAGEMENT_OPERATION',
        'MANAGEMENT_CHAIRMAN', 'Marketing',
        'Fleet Manager', 'Front Desk', 
        'MANAGEMENT_ADMIN', 'Fleet Manager', 
        'Front Desk', 'Cashier', 'customer', 
        'Affiliate_customers', 'Affiliate_admin'])
def Request_Payout_form(request, user):
    customer = Customer.objects.get(user= user)
    Marketer = Affiliate_Group.objects.get(Marketer = customer)      
    
    if request.method == "POST":
        request_form = Request_Funds(user=request.user, data=request.POST)
        if request_form.is_valid():
            instance = request_form.save(commit=False)            
            instance.marketer = Marketer
            instance.save()

            #Generating the transactional ID              
            hashids = Hashids(settings.MANAGEMENT, 10, settings.MANAGEMENT2)
            h = hashids.encode(instance.id)
            Request_Payout.objects.filter(id = instance.id).update(Transaction_ID = h)

            #withdrawing from tempoary account balance
            Marketer.Tempoary_wallet_balance -= instance.Debit_amount   
            Marketer.save()

            Notification_admin.objects.create(
                marketer = Marketer,
                message = f"{Marketer} drop a request for funds, amount N{instance.Debit_amount}"
            )  
                        
            messages.success(request, f"Request Successful, Payment is being processed")

            return redirect('affiliate_dashboard', user = user) 
    else:
        request_form = Request_Funds(user=request.user)
    context = {
        'request_form':request_form,
        'Marketer':Marketer,
    }
    return render(request, 'Affiliate/Request_payout.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=[
        'admin',
        'FLLS', 'MANAGEMENT', 'ICT',
        'MANAGEMENT_OPERATION', 'OPERATIONS',
        'FLM MANAGER', 'TANK', 'IWH', 'MANAGEMENT_RUNYI', 
        'MANAGEMENT_MANAGER', 'MANAGEMENT_OPERATION',
        'MANAGEMENT_CHAIRMAN', 'Marketing',
        'Fleet Manager', 'Front Desk', 
        'MANAGEMENT_ADMIN', 'Fleet Manager', 
        'Front Desk', 'Cashier', 'customer', 
        'Affiliate_customers', 'Affiliate_admin'])
def Payout_History_list(request, user):
    customer = Customer.objects.get(user = request.user)
    Marketer = Affiliate_Group.objects.get(Marketer = customer)
    all_payout = Marketer.request_payout_set.all()
    return render(request, 'Affiliate/Payout_history.html', {'all_payout':all_payout},)


@login_required(login_url='login')
@allowed_user(allowed_roles=[
        'admin',
        'FLLS', 'MANAGEMENT', 'ICT',
        'MANAGEMENT_OPERATION', 'OPERATIONS',
        'FLM MANAGER', 'TANK', 'IWH', 'MANAGEMENT_RUNYI', 
        'MANAGEMENT_MANAGER', 'MANAGEMENT_OPERATION',
        'MANAGEMENT_CHAIRMAN', 'Marketing',
        'Fleet Manager', 'Front Desk', 
        'MANAGEMENT_ADMIN', 'Fleet Manager', 
        'Front Desk', 'Cashier', 'customer', 
        'Affiliate_customers', 'Affiliate_admin'])
def Payout_History_Details(request, pk):
    payout_details = Request_Payout.objects.filter(id= pk)
    return render(request, 'Affiliate/Payout_history_details.html', {'payout_details':payout_details})


@login_required(login_url='login')
@allowed_user(allowed_roles=[
        'admin',
        'FLLS', 'MANAGEMENT', 'ICT',
        'MANAGEMENT_OPERATION', 'OPERATIONS',
        'FLM MANAGER', 'TANK', 'IWH', 'MANAGEMENT_RUNYI', 
        'MANAGEMENT_MANAGER', 'MANAGEMENT_OPERATION',
        'MANAGEMENT_CHAIRMAN', 'Marketing',
        'Fleet Manager', 'Front Desk', 
        'MANAGEMENT_ADMIN', 'Fleet Manager', 
        'Front Desk', 'Cashier', 'customer', 
        'Affiliate_customers', 'Affiliate_admin'])
def Balance_status(request, user):
    customer = Customer.objects.get(user = request.user)
    marketer = Affiliate_Group.objects.get(Marketer = customer)        
    context = {        
        'Balance':marketer,
    }
    
    return render(request, 'Affiliate/Balance_status.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=[
        'admin',
        'FLLS', 'MANAGEMENT', 'ICT',
        'MANAGEMENT_OPERATION', 'OPERATIONS',
        'FLM MANAGER', 'TANK', 'IWH', 'MANAGEMENT_RUNYI', 
        'MANAGEMENT_MANAGER', 'MANAGEMENT_OPERATION',
        'MANAGEMENT_CHAIRMAN', 'Marketing',
        'Fleet Manager', 'Front Desk', 
        'MANAGEMENT_ADMIN', 'Fleet Manager', 
        'Front Desk', 'Cashier', 'customer', 
        'Affiliate_customers', 'Affiliate_admin'])
def Delivery_Details(request, pk):
    delivery_details = Referrals.objects.filter(id = pk)
    return render(request, 'Affiliate/DeliveryDetails.html', {'delivery_details':delivery_details})

@login_required(login_url='login')
@allowed_user(allowed_roles=[
        'admin',
        'FLLS', 'MANAGEMENT', 'ICT',
        'MANAGEMENT_OPERATION', 'OPERATIONS',
        'FLM MANAGER', 'TANK', 'IWH', 'MANAGEMENT_RUNYI', 
        'MANAGEMENT_MANAGER', 'MANAGEMENT_OPERATION',
        'MANAGEMENT_CHAIRMAN', 'Marketing',
        'Fleet Manager', 'Front Desk', 
        'MANAGEMENT_ADMIN', 'Fleet Manager', 
        'Front Desk', 'Cashier', 'customer', 
        'Affiliate_customers', 'Affiliate_admin'])
def Notification_markter(request, user):
    customer = Customer.objects.get(user = user)
    marketer = Affiliate_Group.objects.get(Marketer = customer)
    relation_with_notification = marketer.notification_set.filter(viewed = False)
    
    context = {
        'relation_with_notification':relation_with_notification,
    }
    return render(request, 'Affiliate/customer_notification.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=[
        'admin',
        'FLLS', 'MANAGEMENT', 'ICT',
        'MANAGEMENT_OPERATION', 'OPERATIONS',
        'FLM MANAGER', 'TANK', 'IWH', 'MANAGEMENT_RUNYI', 
        'MANAGEMENT_MANAGER', 'MANAGEMENT_OPERATION',
        'MANAGEMENT_CHAIRMAN', 'Marketing',
        'Fleet Manager', 'Front Desk', 
        'MANAGEMENT_ADMIN', 'Fleet Manager', 
        'Front Desk', 'Cashier', 'customer', 
        'Affiliate_customers', 'Affiliate_admin'])
def Notification_view(request, pk):
    get_notification = Notification.objects.get(id = pk)
    get_notification.viewed = True
    get_notification.save()
    return redirect('customer_view_notification', user = request.user.pk)

#COMPANY-DASHBOARD

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'Affiliate_admin'])
def Dashboard_Affilite(request):    
    notification = Notification_admin.objects.filter(viewed=False)
    return render(request, 'Affiliate/Affiliate_dashboard.html', {'notification':notification})


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'Affiliate_admin'])
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

    #Notiication
    notification = Notification_admin.objects.filter(viewed=False)

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
        'notification':notification,
    }
    return render(request, 'Affiliate/Dashboard_Summary.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'Affiliate_admin'])
def Deliveries_list(request):
    notification = Notification_admin.objects.filter(viewed=False)
    all_referrals = Referrals.objects.all()
    context = {
        'notification':notification,
        'all_referrals': all_referrals,
    }
    return render(request, 'Affiliate/Delivery_list.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'Affiliate_admin'])
def Customer_List(request):
    notification = Notification_admin.objects.filter(viewed=False)
    all_marketers = Affiliate_Group.objects.all()
    context = {
        'notification':notification,
        'all_marketers':all_marketers,
    }
    return render(request, 'Affiliate/Customers_List.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'Affiliate_admin'])
def Payout_List(request):
    notification = Notification_admin.objects.filter(viewed=False)
    payout_list = Request_Payout.objects.all()

    context = {
        'notification':notification,
        "payout_list":payout_list,
    }
    return render(request, 'Affiliate/Payout_list_details.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'Affiliate_admin'])
def Process_payout(request, pk):      
    notification = Notification_admin.objects.filter(viewed=False)
    item = Request_Payout.objects.get(id = pk)
    if request.method == 'POST':
        Process_payment_form = Update_cash_out(request.POST, instance=item)
        if Process_payment_form.is_valid():
            instance = Process_payment_form.save(commit=False)
            instance.Payment_date =  timezone.now()
            instance.save()
            #Withdrawing the money
            if instance.Payment_status == "Paid":
                Marketer = Affiliate_Group.objects.get(Marketer = instance.marketer.Marketer)  
                Marketer.Wallet_Balance -= instance.Amount_credited
                Marketer.cashed_out += instance.Amount_credited
                Marketer.save()
                messages.success(request, f'Payment status updated to "PAID" successfully') 

                Notification.objects.create(
                    marketer = instance.marketer,
                    message = f"Hello {instance.marketer}, funds withdrawal has been processed to you successfully"
                )

            if instance.Payment_status == "Canceled":
                messages.warning(request, f'You have changed payment status to Canceled')        
                Notification.objects.create(
                    marketer = instance.marketer,
                    message = f"Hello {instance.marketer}, funds withdrawal request has been canceled"
                )
            return redirect('payout_list')
    
    else:
        Process_payment_form = Update_cash_out(instance=item)

    context = {
        'notification':notification,
        'Process_payment_form':Process_payment_form,
        'item':item,
    }
    return render(request, 'Affiliate/Process_Payment.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'Affiliate_admin'])
def admin_view_notification(request):
    notification = Notification_admin.objects.filter(viewed=False)
    all_notification = Notification_admin.objects.filter(viewed =False)

    context = {
        'notification':notification,
        'all_notification':all_notification,
    }
    return render(request, 'Affiliate/Admin_view_notification_list.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'Affiliate_admin'])
def update_admin_notification(request, pk):
    get_notification = Notification_admin.objects.get(id = pk)
    get_notification.viewed = True
    get_notification.save()
    return redirect('view_notification')
    

