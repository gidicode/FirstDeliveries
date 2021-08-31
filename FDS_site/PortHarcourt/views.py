from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from hashids import Hashids
from .models import *
from users.models import Delivered, Anonymous
from .forms import *
from django.http import HttpResponseRedirect
import json
import requests
from django.conf import settings
from users.decorators import unauthenticated_user, allowed_user, admin_only
from django.contrib import messages
from django.db.models import Sum

@login_required(login_url='login')
def TheBase(request):
    return render (request, 'PortHarcourt/DashboardBase.html')

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'customer', 'Fleet Manager', 'Front Desk', 'Cashier'])
def requestForm_Cash_PH(request, user):
    customer = Customer.objects.get(user=request.user)
    n_filter = customer.delivered_set.all()
    n = n_filter.filter(viewed = False)
    if request.method == 'POST':
        c_form = Request_Cash_PH(request.POST)
        if c_form.is_valid():
            instance = c_form.save(commit=False)
            instance.customer = customer
            instance.save()
            messages.success(request, f'Your Request for pickup is Successful, you will recieve a call from us shortly')

            hashids = Hashids(salt=settings.HASH, min_length=7)
            h = hashids.encode(instance.id)
            MakeRequestCash_PH.objects.filter(pk = instance.id).update(order_id= h)
            
            tp_choice_1 = customer.makerequestcash_ph_set.filter(order_id = h).filter(Choice_for_TP= 'Bike' )
            tp_choice_2 = customer.makerequestcash_ph_set.filter(order_id = h).filter(Choice_for_TP= 'Tricycle' )            

            #checking for multiple
            chk_none = customer.makerequestcash_ph_set.get(order_id = h)
                    
            item_2 = [
                    chk_none.Address_of_reciever2, chk_none.reciever_phone_number2, 
                    chk_none.Package_description2, chk_none.reciever_name2
                    ]
            item_3 = [
                    chk_none.Address_of_reciever3, chk_none.Package_description3,
                    chk_none.reciever_phone_number3, chk_none.reciever_name3
                    ]
            item_4 = [
                    chk_none.Address_of_reciever4, chk_none.Package_description4,
                    chk_none.reciever_phone_number4, chk_none.reciever_name4
                    ]
            item_5 = [
                    chk_none.Address_of_reciever5, chk_none.Package_description5,
                    chk_none.reciever_phone_number5, chk_none.reciever_name5
                    ]           
            if tp_choice_1:
                charge_amount = 500
                count_item2 = item_2.count('')
                count_item3 = item_3.count('')
                count_item4 = item_4.count('')
                count_item5 = item_5.count('')
                
                customer.makerequestcash_ph_set.filter(order_id = h).update(Amount_Payable = charge_amount)
                if count_item2 >= 3:
                    pass
                else:
                    charge_amount += 500
                    customer.makerequestcash_ph_set.filter(order_id = h).update(Amount_Payable = charge_amount)

                if count_item3 >= 3:
                    pass
                else:
                    charge_amount += 500
                    customer.makerequestcash_ph_set.filter(order_id = h).update(Amount_Payable = charge_amount)

                if count_item4 >= 3:
                    pass
                else:
                    charge_amount += 500
                    customer.makerequestcash_ph_set.filter(order_id = h).update(Amount_Payable = charge_amount)
                
                if count_item5 >= 3:
                    pass
                else:
                    charge_amount += 500
                    customer.makerequestcash_ph_set.filter(order_id = h).update(Amount_Payable = charge_amount)

                if charge_amount == 1000:
                    messages.success(request, f'Your delivery fee start at N{charge_amount}, Total Deliveries is 2 ')
                elif charge_amount == 1500:
                    messages.success(request, f'Your delivery fee start at N{charge_amount}, Total Deliveries is 3')
                elif charge_amount == 2000:
                    messages.success(request, f'Your delivery fee start at N{charge_amount}, Total Deliveries is 4')
                elif charge_amount == 2500:
                    messages.success(request, f'Your delivery fee start at N{charge_amount}, Total Deliveries is 5')
                else:
                    messages.success(request, f'Your delivery fee start at N{charge_amount}, Single Delivery.')
            
            if tp_choice_2:
                count_item2 = item_2.count('')
                count_item3 = item_3.count('')
                count_item4 = item_4.count('')
                count_item5 = item_5.count('')
                charge_amount = 1000
                customer.makerequestcash_ph_set.filter(order_id = h).update(Amount_Payable = charge_amount)
                if count_item2 >= 3:
                    pass
                else:
                    charge_amount += 1000
                    customer.makerequestcash_ph_set.filter(order_id = h).update(Amount_Payable = charge_amount)

                if count_item3 >= 3:
                    pass
                else:
                    charge_amount += 1000
                    customer.makerequestcash_ph_set.filter(order_id = h).update(Amount_Payable = charge_amount)

                if count_item4 >= 3:
                    pass
                else:
                    charge_amount += 1000
                    customer.makerequestcash_ph_set.filter(order_id = h).update(Amount_Payable = charge_amount)
                
                if count_item5 >= 3:
                    pass
                else:
                    charge_amount += 1000
                    customer.makerequestcash_ph_set.filter(order_id = h).update(Amount_Payable = charge_amount)

                if charge_amount == 2000:
                    messages.success(request, f'Your choice of transportation is Tricycle Your delivery Fee is NGN{charge_amount}, Total Deliveries is 2 ')
                elif charge_amount == 3000:
                    messages.success(request, f'Your choice of transportation is Tricycle Your delivery Fee is NGN{charge_amount}, Total Deliveries is 3')
                elif charge_amount == 4000:
                    messages.success(request, f'Your choice of transportation is Tricycle Your delivery Fee is NGN{charge_amount}, Total Deliveries is 4')
                elif charge_amount == 5000:
                    messages.success(request, f'Your choice of transportation is Tricycle Your delivery Fee is NGN{charge_amount}, Total Deliveries is 5')
                else:
                    messages.success(request, f'Your choice of transportation is Tricycle Your delivery Fee is NGN{charge_amount}, Single Delivery.')

            PH_adminNotification.objects.create(
                customer=instance.customer,
                item_created = instance,
                order_id = h
            ) 

            return redirect('dashboard', user=user)
    else:
        c_form = Request_Cash_PH(instance=customer)
            
    context = {
        'c_form': c_form,
        'customer':customer,
        'n':n,
        }
    return render(request, 'PortHarcourt/Cash_request_PH.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'customer', 'Fleet Manager', 'Front Desk', 'Cashier'])
def ErrandMenu_PH(request, user):
    customer = Customer.objects.get(user= user)
    n_filter = customer.delivered_set.all()
    n = n_filter.filter(viewed = False)

    return render(request, 'PortHarcourt/ErrandService_PH.html', {'n':n, 'customer':customer})

login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'customer', 'Fleet Manager', 'Front Desk', 'Cashier'])
def fuel_errand_ph(request, user):
    customer = Customer.objects.get(user = request.user)
    n_filter = customer.delivered_set.all()
    n = n_filter.filter(viewed = False)
    if request.method == 'POST':
        fuel_form = Fuel_errand_PH(request.POST)
        if fuel_form.is_valid():
            instance = fuel_form.save(commit=False)
            instance.customer = customer
            instance.category = 'Fuel'
            instance.save()
        
            hashids = Hashids(salt = settings.ERRAND, min_length=7)
            h = hashids.encode(instance.id)
            customer.errand_service_ph_set.filter(pk = instance.id).update(order_id = h)
            messages.success(request, f'Your Fuel Errand request has been recieved')
            
            PH_adminNotification.objects.create(
                customer = instance.customer,
                item_created = "Errand",
                order_id = h
            )

            summing_amt_payable = instance.fuel_per_amount + 500
            customer.errand_service_ph_set.filter(pk = instance.id).update(Amount_Payable = summing_amt_payable)

            #initalize payment
            chk_payment_type = customer.errand_service_ph_set.get(pk = instance.id)
            chk_card = chk_payment_type.payment_channel            
            req = chk_payment_type.Amount_Payable 
            if chk_card == 'Card/Transfer':
                def initialize_fuel_payment(request, user):
                    url = "https://api.paystack.co/transaction/initialize"
                    if req >= 2500:
                        get_amount = 1.5001/100 * req + 100
                        amt = req + get_amount
                        final_amount = int(amt * 100)
                        payload = json.dumps({
                            'email': request.user.email,
                            'amount': final_amount
                        })
                        amount_for_update = int(amt)
                        messages.success(request, f'Your Total Fee (item cost + delivery fee) is {amount_for_update}') 
                    else:
                        get_amount = 1.5001/100 * req
                        amt = req + get_amount
                        final_amt = int(amt * 100)
                        payload = json.dumps({
                            'email': request.user.email,
                            'amount': final_amt,
                        })
                        amount_for_update2 = int(amt)
                        messages.success(request, f'Your Total Fee (item cost + delivery fee) is {amount_for_update2}') 
                    headers = {
                        "Authorization": 'Bearer sk_test_1d32c71fd73944bd712f5b94853de7fe325387ec',
                        'Content-Type': 'application/json'
                    }

                    r = requests.request('POST', url, headers=headers, data=payload)

                    if r.status_code != 200:
                        return str(r.status_code) 
                    result = r.json()
                    return result
                initialized =initialize_fuel_payment(request, user)
                customer.errand_service_ph_set.filter(pk=instance.id).update(Ps_reference = initialized['data']['reference'])
                link = initialized['data']['authorization_url']
                return HttpResponseRedirect(link)  
            else:
                messages.success(request, f'Your Total Fee (item cost + delivery fee) is {req}') 
                return redirect('dashboard', user =user)
                    
    else:
        fuel_form = Fuel_errand_PH(instance = customer) 

    context = {
        'fuel_form':fuel_form,
        'customer':customer,
        'n':n
    }
    return render(request, 'PortHarcourt/Fuelerrand_PH.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'customer', 'Fleet Manager', 'Front Desk', 'Cashier'])
def gas_errand_ph(request, user):
    customer = Customer.objects.get(user = request.user)
    n_filter = customer.delivered_set.all()
    n = n_filter.filter(viewed = False)
    if request.method == 'POST':
        gas_form = Gas_errand_PH(request.POST)
        if gas_form.is_valid():
            instance = gas_form.save(commit=False)
            instance.customer = customer
            instance.category = 'Gas'
            instance.save()
        
            hashids = Hashids(salt = settings.ERRAND, min_length=7)
            h = hashids.encode(instance.id)
            customer.errand_service_ph_set.filter(pk = instance.id).update(order_id = h)
            messages.success(request, f'Your Gas Errand request has been recieved')
            
            PH_adminNotification.objects.create(
                customer = instance.customer,
                item_created = "Errand",
                order_id = h
            )

            summing_amt_payable = instance.Gas_Quantity * 460 + 500
            customer.errand_service_ph_set.filter(pk = instance.id).update(Amount_Payable = summing_amt_payable)

            #initalize payment
            chk_payment_type = customer.errand_service_ph_set.get(pk = instance.id)
            chk_card = chk_payment_type.payment_channel
         
            req = chk_payment_type.Amount_Payable 
            if chk_card == 'Card/Transfer':
                def initialize_fuel_payment(request, user):
                    url = "https://api.paystack.co/transaction/initialize"
                    if req >= 2500:
                        get_amount = 1.5001/100 * req + 100
                        amt = req + get_amount
                        final_amount = int(amt * 100)
                        payload = json.dumps({
                            'email': request.user.email,
                            'amount': final_amount
                        })
                        amount_for_update = int(amt)
                        messages.success(request, f'Your Total Fee (item cost + delivery fee) is {amount_for_update}') 
                    else:
                        get_amount = 1.5001/100 * req
                        amt = req + get_amount
                        final_amt = int(amt * 100)
                        payload = json.dumps({
                            'email': request.user.email,
                            'amount': final_amt,
                        })
                        amount_for_update = int(amt)
                        messages.success(request, f'Your Total Fee (item cost + delivery fee) is {amount_for_update}') 
                    headers = {
                        "Authorization": 'Bearer sk_test_1d32c71fd73944bd712f5b94853de7fe325387ec',
                        'Content-Type': 'application/json'
                    }

                    r = requests.request('POST', url, headers=headers, data=payload)

                    if r.status_code != 200:
                        return str(r.status_code) 
                    result = r.json()
                    return result
                initialized =initialize_fuel_payment(request, user)
                customer.errand_service_set.filter(pk=instance.id).update(Ps_reference = initialized['data']['reference'])
                link = initialized['data']['authorization_url']
                return HttpResponseRedirect(link)  
            else:
                messages.success(request, f'Your Total Fee (item cost + delivery fee) is {req}') 
                return redirect('dashboard', user =user)
                    
    else:
        gas_form = Gas_errand_PH(instance = customer) 

    context = {
        'gas_form':gas_form,
        'customer':customer,
        'n':n
    }
    return render(request, 'PortHarcourt/Gaserrand_PH.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'customer', 'Fleet Manager', 'Front Desk', 'Cashier'])            
def drugs_errand_ph(request, user):
    customer = Customer.objects.get(user = request.user)
    n_filter = customer.delivered_set.all()
    n = n_filter.filter(viewed = False)
    if request.method == 'POST':
        drugs_form = Drugs_errand_PH(request.POST, request.FILES)
        if drugs_form.is_valid():
            instance = drugs_form.save(commit=False)
            instance.customer = customer
            instance.category = 'Drugs'
            instance.save()
        
            hashids = Hashids(salt = settings.ERRAND, min_length=7)
            h = hashids.encode(instance.id)
            customer.errand_service_ph_set.filter(pk = instance.id).update(order_id = h)
            messages.success(request, f'Your Drugs Errand request has been recieved')
            
            PH_adminNotification.objects.create(
                customer = instance.customer,
                item_created = "Errand",
                order_id = h
            )

            summing_amt_payable = instance.Enter_amount + 500
            customer.errand_service_ph_set.filter(pk = instance.id).update(Amount_Payable = summing_amt_payable)

            #initalize payment
            chk_payment_type = customer.errand_service_ph_set.get(pk = instance.id)
            chk_card = chk_payment_type.payment_channel
         
            req = chk_payment_type.Amount_Payable 
            if chk_card == 'Card/Transfer':
                def initialize_fuel_payment(request, user):
                    url = "https://api.paystack.co/transaction/initialize"
                    if req >= 2500:
                        get_amount = 1.5001/100 * req + 100
                        amt = req + get_amount
                        final_amount = int(amt * 100)
                        payload = json.dumps({
                            'email': request.user.email,
                            'amount': final_amount
                        })
                        amount_for_update = int(amt)
                        messages.success(request, f'Your Total Fee (item cost + delivery fee) is {amount_for_update}') 
                    else:
                        get_amount = 1.5001/100 * req
                        amt = req + get_amount
                        final_amt = int(amt * 100)
                        payload = json.dumps({
                            'email': request.user.email,
                            'amount': final_amt,
                        })
                        amount_for_update = int(amt)
                        messages.success(request, f'Your Total Fee (item cost + delivery fee) is {amount_for_update}') 
                    headers = {
                        "Authorization": 'Bearer sk_test_1d32c71fd73944bd712f5b94853de7fe325387ec',
                        'Content-Type': 'application/json'
                    }

                    r = requests.request('POST', url, headers=headers, data=payload)

                    if r.status_code != 200:
                        return str(r.status_code) 
                    result = r.json()
                    return result
                initialized =initialize_fuel_payment(request, user)
                customer.errand_service_set.filter(pk=instance.id).update(Ps_reference = initialized['data']['reference'])
                link = initialized['data']['authorization_url']
                return HttpResponseRedirect(link)  
            else:
                messages.success(request, f'Your Total Fee (item cost + delivery fee) is {req}') 
                return redirect('dashboard', user =user)
                    
    else:
        drugs_form = Drugs_errand_PH(instance = customer) 

    context = {
        'drugs_form':drugs_form,
        'customer':customer,
        'n':n
    }
    return render(request, 'PortHarcourt/Drugserrand_PH.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'customer', 'Fleet Manager', 'Front Desk', 'Cashier'])
def bread_errand_ph(request, user):
    customer = Customer.objects.get(user = request.user)
    n_filter = customer.delivered_set.all()
    n = n_filter.filter(viewed = False)
    if request.method == 'POST':
        bread_form = Bread_errand_PH(request.POST)
        if bread_form.is_valid():
            instance = bread_form.save(commit=False)
            instance.customer = customer
            instance.category = 'Bread'
            instance.save()
        
            hashids = Hashids(salt = settings.ERRAND, min_length=7)
            h = hashids.encode(instance.id)
            customer.errand_service_ph_set.filter(pk = instance.id).update(order_id = h)
            messages.success(request, f'Your Bread Errand request has been recieved')
            
            PH_adminNotification.objects.create(
                customer = instance.customer,
                item_created = "Errand",
                order_id = h
            )

            summing_amt_payable = instance.Enter_amount + 500
            customer.errand_service_ph_set.filter(pk = instance.id).update(Amount_Payable = summing_amt_payable)

            #initalize payment
            chk_payment_type = customer.errand_service_ph_set.get(pk = instance.id)
            chk_card = chk_payment_type.payment_channel
         
            req = chk_payment_type.Amount_Payable 
            if chk_card == 'Card/Transfer':
                def initialize_fuel_payment(request, user):
                    url = "https://api.paystack.co/transaction/initialize"
                    if req >= 2500:
                        get_amount = 1.5001/100 * req + 100
                        amt = req + get_amount
                        final_amount = int(amt * 100)
                        payload = json.dumps({
                            'email': request.user.email,
                            'amount': final_amount
                        })
                        amount_for_update = int(amt)
                        messages.success(request, f'Your Total Fee (item cost + delivery fee) is {amount_for_update}') 
                    else:
                        get_amount = 1.5001/100 * req
                        amt = req + get_amount
                        final_amt = int(amt * 100)
                        payload = json.dumps({
                            'email': request.user.email,
                            'amount': final_amt,
                        })
                        amount_for_update = int(amt)
                        messages.success(request, f'Your Total Fee (item cost + delivery fee) is {amount_for_update}') 
                    headers = {
                        "Authorization": 'Bearer sk_test_1d32c71fd73944bd712f5b94853de7fe325387ec',
                        'Content-Type': 'application/json'
                    }

                    r = requests.request('POST', url, headers=headers, data=payload)

                    if r.status_code != 200:
                        return str(r.status_code) 
                    result = r.json()
                    return result
                initialized =initialize_fuel_payment(request, user)
                customer.errand_service_set.filter(pk=instance.id).update(Ps_reference = initialized['data']['reference'])
                link = initialized['data']['authorization_url']
                return HttpResponseRedirect(link)  
            else:
                messages.success(request, f'Your Total Fee (item cost + delivery fee) is {req}') 
                return redirect('dashboard', user =user)      
    else:
        bread_form = Bread_errand_PH(instance=customer) 

    context = {
        'bread_form':bread_form,
        'customer':customer,
        'n':n
    }
    return render(request, 'PortHarcourt/Breaderrand_ph.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'customer', 'Fleet Manager', 'Front Desk', 'Cashier'])
def shawarma_errand_ph(request, user):
    customer = Customer.objects.get(user = request.user)
    n_filter = customer.delivered_set.all()
    n = n_filter.filter(viewed = False)
    if request.method == 'POST':
        shawarma_form = Shawarma_errand_PH(request.POST)
        if shawarma_form.is_valid():
            instance = shawarma_form.save(commit=False)
            instance.customer = customer
            instance.category = 'Shawarma'
            instance.save()
        
            hashids = Hashids(salt = settings.ERRAND, min_length=7)
            h = hashids.encode(instance.id)
            customer.errand_service_set.filter(pk = instance.id).update(order_id = h)
            messages.success(request, f'Your Shawarma Errand request has been recieved')
            
            PH_adminNotification.objects.create(
                customer = instance.customer,
                item_created = "Errand",
                order_id = h
            )

            summing_amt_payable = instance.Enter_amount + 500
            customer.errand_service_set.filter(pk = instance.id).update(Amount_Payable = summing_amt_payable)

            #initalize payment
            chk_payment_type = customer.errand_service_set.get(pk = instance.id)
            chk_card = chk_payment_type.payment_channel
         
            req = chk_payment_type.Amount_Payable 
            if chk_card == 'Card/Transfer':
                def initialize_fuel_payment(request, user):
                    url = "https://api.paystack.co/transaction/initialize"
                    if req >= 2500:
                        get_amount = 1.5001/100 * req + 100
                        amt = req + get_amount
                        final_amount = int(amt * 100)
                        payload = json.dumps({
                            'email': request.user.email,
                            'amount': final_amount
                        })
                        amount_for_update = int(amt)
                        messages.success(request, f'Your Total Fee (fuel + delivery) is {amount_for_update}') 
                    else:
                        get_amount = 1.5001/100 * req
                        amt = req + get_amount
                        final_amt = int(amt * 100)
                        payload = json.dumps({
                            'email': request.user.email,
                            'amount': final_amt,
                        })
                        amount_for_update = int(amt)
                        messages.success(request, f'Your Total Fee (item cost + delivery fee) is {amount_for_update}') 
                    headers = {
                        "Authorization": 'Bearer sk_test_1d32c71fd73944bd712f5b94853de7fe325387ec',
                        'Content-Type': 'application/json'
                    }

                    r = requests.request('POST', url, headers=headers, data=payload)

                    if r.status_code != 200:
                        return str(r.status_code) 
                    result = r.json()
                    return result
                initialized =initialize_fuel_payment(request, user)
                customer.errand_service_set.filter(pk=instance.id).update(Ps_reference = initialized['data']['reference'])
                link = initialized['data']['authorization_url']
                return HttpResponseRedirect(link)  
            else:
                messages.success(request, f'Your Total Fee (item cost + delivery fee) is {req}') 
                return redirect('dashboard', user =user)
                    
    else:
        shawarma_form = Shawarma_errand_PH(instance = customer) 

    context = {
        'shawarma_form':shawarma_form,
        'customer':customer,
        'n':n
    }
    return render(request, 'PortHarcourt/Shawarmaerrand_PH.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'customer', 'Fleet Manager', 'Front Desk', 'Cashier'])
def pizza_errand_PH(request, user):
    customer = Customer.objects.get(user = request.user)
    n_filter = customer.delivered_set.all()
    n = n_filter.filter(viewed = False)
    if request.method == 'POST':
        pizza_form = Pizza_errand(request.POST)
        if pizza_form.is_valid():
            instance = pizza_form.save(commit=False)
            instance.customer = customer
            instance.category = 'Pizza'
            instance.save()
        
            hashids = Hashids(salt = settings.ERRAND, min_length=7)
            h = hashids.encode(instance.id)
            customer.errand_service_set.filter(pk = instance.id).update(order_id = h)
            messages.success(request, f'Your Pizza Errand request has been recieved')
            
            PH_adminNotification.objects.create(
                customer = instance.customer,
                item_created = "Errand",
                order_id = h
            )

            summing_amt_payable = instance.Enter_amount + 500
            customer.errand_service_set.filter(pk = instance.id).update(Amount_Payable = summing_amt_payable)

            #initalize payment
            chk_payment_type = customer.errand_service_set.get(pk = instance.id)
            chk_card = chk_payment_type.payment_channel
         
            req = chk_payment_type.Amount_Payable 
            if chk_card == 'Card/Transfer':
                def initialize_fuel_payment(request, user):
                    url = "https://api.paystack.co/transaction/initialize"
                    if req >= 2500:
                        get_amount = 1.5001/100 * req + 100
                        amt = req + get_amount
                        final_amount = int(amt * 100)
                        payload = json.dumps({
                            'email': request.user.email,
                            'amount': final_amount
                        })
                        amount_for_update = int(amt)
                        messages.success(request, f'Your Total Fee (item cost + delivery fee) is {amount_for_update}') 
                    else:
                        get_amount = 1.5001/100 * req
                        amt = req + get_amount
                        final_amt = int(amt * 100)
                        payload = json.dumps({
                            'email': request.user.email,
                            'amount': final_amt,
                        })
                        amount_for_update = int(amt)
                        messages.success(request, f'Your Total Fee (item cost + delivery fee) is {amount_for_update}') 
                    headers = {
                        "Authorization": 'Bearer sk_test_1d32c71fd73944bd712f5b94853de7fe325387ec',
                        'Content-Type': 'application/json'
                    }

                    r = requests.request('POST', url, headers=headers, data=payload)

                    if r.status_code != 200:
                        return str(r.status_code) 
                    result = r.json()
                    return result
                initialized =initialize_fuel_payment(request, user)
                customer.errand_service_set.filter(pk=instance.id).update(Ps_reference = initialized['data']['reference'])
                link = initialized['data']['authorization_url']
                return HttpResponseRedirect(link)  
            else:
                messages.success(request, f'Your Total Fee (item cost + delivery fee) is {req}') 
                return redirect('dashboard', user =user)
                    
    else:
        pizza_form = Pizza_errand(instance = customer) 

    context = {
        'pizza_form':pizza_form,
        'customer':customer,
        'n':n,
    }
    return render(request, 'users/Pizzaerrand.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'customer', 'Fleet Manager', 'Front Desk', 'Cashier'])
def fruits_errand(request, user):
    customer = Customer.objects.get(user = request.user)
    n_filter = customer.delivered_set.all()
    n = n_filter.filter(viewed = False)
    if request.method == 'POST':
        fruits_form = Fruits_errand(request.POST)
        if fruits_form.is_valid():
            instance  = fruits_form.save(commit=False)
            instance.customer = customer
            instance.category = 'Fruits'
            instance.save()
        
            hashids = Hashids(salt = settings.ERRAND, min_length=7)
            h = hashids.encode(instance.id)
            customer.errand_service_set.filter(pk = instance.id).update(order_id = h)
            messages.success(request, f'Your Fruits Errand request has been recieved')
            
            PH_adminNotification.objects.create(
                customer = instance.customer,
                item_created = "Errand",
                order_id = h
            )

            summing_amt_payable = instance.Enter_amount + 500
            customer.errand_service_set.filter(pk = instance.id).update(Amount_Payable = summing_amt_payable)

            #initalize payment
            chk_payment_type = customer.errand_service_set.get(pk = instance.id)
            chk_card = chk_payment_type.payment_channel
         
            req = chk_payment_type.Amount_Payable 
            if chk_card == 'Card/Transfer':
                def initialize_fuel_payment(request, user):
                    url = "https://api.paystack.co/transaction/initialize"
                    if req >= 2500:
                        get_amount = 1.5001/100 * req + 100
                        amt = req + get_amount
                        final_amount = int(amt * 100)
                        payload = json.dumps({
                            'email': request.user.email,
                            'amount': final_amount
                        })
                        amount_for_update = int(amt)
                        messages.success(request, f'Your Total Fee (item cost + delivery fee) is {amount_for_update}') 
                    else:
                        get_amount = 1.5001/100 * req
                        amt = req + get_amount
                        final_amt = int(amt * 100)
                        payload = json.dumps({
                            'email': request.user.email,
                            'amount': final_amt,
                        })
                        amount_for_update = int(amt)
                        messages.success(request, f'Your Total Fee (item cost + delivery fee) is {amount_for_update}') 
                    headers = {
                        "Authorization": 'Bearer sk_test_1d32c71fd73944bd712f5b94853de7fe325387ec',
                        'Content-Type': 'application/json'
                    }

                    r = requests.request('POST', url, headers=headers, data=payload)

                    if r.status_code != 200:
                        return str(r.status_code) 
                    result = r.json()
                    return result
                initialized =initialize_fuel_payment(request, user)
                customer.errand_service_set.filter(pk=instance.id).update(Ps_reference = initialized['data']['reference'])
                link = initialized['data']['authorization_url']
                return HttpResponseRedirect(link)  
            else:
                messages.success(request, f'Your Total Fee (item cost + delivery fee) is {req}') 
                return redirect('dashboard', user =user)
                    
    else:
        fruits_form = Fruits_errand(instance = customer) 

    context = {
        'fruits_form':fruits_form,
        'customer':customer,
        'n':n
    }
    return render(request, 'users/Fruitserrand.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'customer', 'Fleet Manager', 'Front Desk', 'Cashier'])
def icecream_errand(request, user):
    customer = Customer.objects.get(user = request.user)
    n_filter = customer.delivered_set.all()
    n = n_filter.filter(viewed = False)
    if request.method == 'POST':
        icecream_form = Icecream_errand(request.POST)
        if icecream_form.is_valid():
            instance = icecream_form.save(commit=False)
            instance.customer = customer
            instance.category = 'Ice Cream'
            instance.save()
        
            hashids = Hashids(salt = settings.ERRAND, min_length=7)
            h = hashids.encode(instance.id)
            customer.errand_service_set.filter(pk = instance.id).update(order_id = h)
            messages.success(request, f'Your Ice cream Errand request has been recieved')
            
            PH_adminNotification.objects.create(
                customer = instance.customer,
                item_created = "Errand",
                order_id = h
            )

            summing_amt_payable = instance.Enter_amount + 500
            customer.errand_service_set.filter(pk = instance.id).update(Amount_Payable = summing_amt_payable)

            #initalize payment
            chk_payment_type = customer.errand_service_set.get(pk = instance.id)
            chk_card = chk_payment_type.payment_channel
         
            req = chk_payment_type.Amount_Payable 
            if chk_card == 'Card/Transfer':
                def initialize_fuel_payment(request, user):
                    url = "https://api.paystack.co/transaction/initialize"
                    if req >= 2500:
                        get_amount = 1.5001/100 * req + 100
                        amt = req + get_amount
                        final_amount = int(amt * 100)
                        payload = json.dumps({
                            'email': request.user.email,
                            'amount': final_amount
                        })
                        amount_for_update = int(amt)
                        messages.success(request, f'Your Total Fee (item cost + delivery fee) is {amount_for_update}') 
                    else:
                        get_amount = 1.5001/100 * req
                        amt = req + get_amount
                        final_amt = int(amt * 100)
                        payload = json.dumps({
                            'email': request.user.email,
                            'amount': final_amt,
                        })
                        amount_for_update = int(amt)
                        messages.success(request, f'Your Total Fee (item cost + delivery fee) is {amount_for_update}') 
                    headers = {
                        "Authorization": 'Bearer sk_test_1d32c71fd73944bd712f5b94853de7fe325387ec',
                        'Content-Type': 'application/json'
                    }

                    r = requests.request('POST', url, headers=headers, data=payload)

                    if r.status_code != 200:
                        return str(r.status_code) 
                    result = r.json()
                    return result
                initialized =initialize_fuel_payment(request, user)
                customer.errand_service_set.filter(pk=instance.id).update(Ps_reference = initialized['data']['reference'])
                link = initialized['data']['authorization_url']
                return HttpResponseRedirect(link)  
            else:
                messages.success(request, f'Your Total Fee (item cost + delivery fee) is {req}') 
                return redirect('dashboard', user =user)
                    
    else:
        icecream_form = Icecream_errand(instance = customer) 

    context = {
        'icecream_form':icecream_form,
        'customer':customer,
        'n':n
    }
    return render(request, 'users/Icecreamerrand.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'customer', 'Fleet Manager', 'Front Desk', 'Cashier'])
def food_errand(request, user):
    customer = Customer.objects.get(user = request.user)
    n_filter = customer.delivered_set.all()
    n = n_filter.filter(viewed = False)
    if request.method == 'POST':
        food_form = Food_errand(request.POST)
        if food_form.is_valid():
            instance = food_form.save(commit=False)
            instance.customer = customer
            instance.category = 'Food'
            instance.save()
        
            hashids = Hashids(salt = settings.ERRAND, min_length=7)
            h = hashids.encode(instance.id)
            customer.errand_service_set.filter(pk = instance.id).update(order_id = h)
            messages.success(request, f'Your Food Errand request has been recieved')
            
            PH_adminNotification.objects.create(
                customer = instance.customer,
                item_created = "Errand",
                order_id = h
            )

            summing_amt_payable = instance.Enter_amount + 500
            customer.errand_service_set.filter(pk = instance.id).update(Amount_Payable = summing_amt_payable)

            #initalize payment
            chk_payment_type = customer.errand_service_set.get(pk = instance.id)
            chk_card = chk_payment_type.payment_channel
         
            req = chk_payment_type.Amount_Payable 
            if chk_card == 'Card/Transfer':
                def initialize_fuel_payment(request, user):
                    url = "https://api.paystack.co/transaction/initialize"
                    if req >= 2500:
                        get_amount = 1.5001/100 * req + 100
                        amt = req + get_amount
                        final_amount = int(amt * 100)
                        payload = json.dumps({
                            'email': request.user.email,
                            'amount': final_amount
                        })
                        amount_for_update = int(amt)
                        messages.success(request, f'Your Total Fee (item cost + delivery fee) is {amount_for_update}') 
                    else:
                        get_amount = 1.5001/100 * req
                        amt = req + get_amount
                        final_amt = int(amt * 100)
                        payload = json.dumps({
                            'email': request.user.email,
                            'amount': final_amt,
                        })
                        amount_for_update = int(amt)
                        messages.success(request, f'Your Total Fee (item cost + delivery fee) is {amount_for_update}') 
                    headers = {
                        "Authorization": 'Bearer sk_test_1d32c71fd73944bd712f5b94853de7fe325387ec',
                        'Content-Type': 'application/json'
                    }

                    r = requests.request('POST', url, headers=headers, data=payload)

                    if r.status_code != 200:
                        return str(r.status_code) 
                    result = r.json()
                    return result
                initialized =initialize_fuel_payment(request, user)
                customer.errand_service_set.filter(pk=instance.id).update(Ps_reference = initialized['data']['reference'])
                link = initialized['data']['authorization_url']
                return HttpResponseRedirect(link)  
            else:
                messages.success(request, f'Your Total Fee (item cost + delivery fee) is {req}') 
                return redirect('dashboard', user =user)
                    
    else:
        food_form = Food_errand(instance = customer) 

    context = {
        'food_form':food_form,
        'customer':customer,
        'n':n
    }
    return render(request, 'users/Fooderrand.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'customer', 'Fleet Manager', 'Front Desk', 'Cashier'])
def other_errand(request, user):
    customer = Customer.objects.get(user = request.user)
    n_filter = customer.delivered_set.all()
    n = n_filter.filter(viewed = False)
    if request.method == 'POST':
        general_form = Other_errand(request.POST)
        if general_form.is_valid():
            instance = general_form.save(commit=False)
            instance.customer = customer
            instance.category = 'Other'
            instance.save()
        
            hashids = Hashids(salt = settings.ERRAND, min_length=7)
            h = hashids.encode(instance.id)
            customer.errand_service_set.filter(pk = instance.id).update(order_id = h)
            messages.success(request, f'Your Errand request has been recieved')
            
            PH_adminNotification.objects.create(
                customer = instance.customer,
                item_created = "Errand",
                order_id = h
            )

            summing_amt_payable = instance.Enter_amount + 500
            customer.errand_service_set.filter(pk = instance.id).update(Amount_Payable = summing_amt_payable)

            #initalize payment
            chk_payment_type = customer.errand_service_set.get(pk = instance.id)
            chk_card = chk_payment_type.payment_channel
         
            req = chk_payment_type.Amount_Payable 
            if chk_card == 'Card/Transfer':
                def initialize_fuel_payment(request, user):
                    url = "https://api.paystack.co/transaction/initialize"
                    if req >= 2500:
                        get_amount = 1.5001/100 * req + 100
                        amt = req + get_amount
                        final_amount = int(amt * 100)
                        payload = json.dumps({
                            'email': request.user.email,
                            'amount': final_amount
                        })
                        amount_for_update = int(amt)
                        messages.success(request, f'Your Total Fee (item cost + delivery fee) is {amount_for_update}') 
                    else:
                        get_amount = 1.5001/100 * req
                        amt = req + get_amount
                        final_amt = int(amt * 100)
                        payload = json.dumps({
                            'email': request.user.email,
                            'amount': final_amt,
                        })
                        amount_for_update = int(amt)
                        messages.success(request, f'Your Total Fee (item cost + delivery fee) is {amount_for_update}') 
                    headers = {
                        "Authorization": 'Bearer sk_test_1d32c71fd73944bd712f5b94853de7fe325387ec',
                        'Content-Type': 'application/json'
                    }

                    r = requests.request('POST', url, headers=headers, data=payload)

                    if r.status_code != 200:
                        return str(r.status_code) 
                    result = r.json()
                    return result
                initialized =initialize_fuel_payment(request, user)
                customer.errand_service_set.filter(pk=instance.id).update(Ps_reference = initialized['data']['reference'])
                link = initialized['data']['authorization_url']
                return HttpResponseRedirect(link)  
            else:
                messages.success(request, f'Your Total Fee (item cost + delivery fee) is {req}') 
                return redirect('dashboard', user =user)
                    
    else:
        general_form = Other_errand(instance = customer) 

    context = {
        'general_form':general_form,
        'customer':customer,
        'n':n
    }
    return render(request, 'users/Othererrand.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'Front Desk'])
def PickDrop(request, user):
    customer = Customer.objects.get(user = request.user)
    if request.method == "POST":
        pickdrop_Form = Front_desk_pick(request.POST)
        if pickdrop_Form.is_valid():
            instance = pickdrop_Form.save(commit = False)
            instance.customer = customer
            instance.Delivery_type = 'Pick & Drop'
            instance.save()

            messages.success(request, f'Hello {request.user.username}, action Successful')

            hashids = Hashids(salt=settings.FRONT_DESK, min_length=7)
            h = hashids.encode(instance.id)
            Front_desk_PH.objects.filter(pk = instance.id).update(order_id= h)

            PH_adminNotification.objects.create(
                customer=instance.customer,
                item_created = "Front Desk",
                order_id = h   
            )             
            return redirect('frontdesk', user=user)
    else:
        pickdrop_Form = Front_desk_pick(instance = customer)

    context = {
        'customer':customer,
        'pickdrop_Form':pickdrop_Form,
    }
    return render(request, 'users/FrontDeskPickUp.html', context )

# Front desk Errand form
@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'Front Desk'])
def FrontErrand(request, user):
    customer = Customer.objects.get(user = request.user)
    if request.method == "POST":
        errand_Form = Front_desk_errand(request.POST)
        if errand_Form.is_valid():
            instance = errand_Form.save(commit = False)
            instance.customer = customer
            instance.Delivery_type = 'Errand'
            instance.save()            

            hashids = Hashids(salt=settings.FRONT_DESK, min_length=7)
            h = hashids.encode(instance.id)
            Front_desk_PH.objects.filter(pk = instance.id).update(order_id= h)

            messages.success(request, f'Hello {request.user.username}, action Successful {h}')            
            chk_none = instance.Enter_amount

            if chk_none == None:
                Front_desk_PH.objects.filter(pk = instance.id).update(Total= instance.Delivery_Fee)
            elif chk_none!= None:
                get_total = instance.Enter_amount + instance.Delivery_Fee
                Front_desk_PH.objects.filter(pk = instance.id).update(Total= get_total)                                                
        
            PH_adminNotification.objects.create(     
                customer=instance.customer,
                item_created = "Front Desk",
                order_id = h   
            )                 
            
            return redirect('frontdesk', user=user)
    else:
        errand_Form = Front_desk_errand(instance = customer)

    context = {
        'customer':customer,
        'errand_Form':errand_Form,
    }
    return render(request, 'users/FrontDeskErrand.html', context )

##########################  UPDATE  #####################################

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin','Fleet_Manager'])
def Update_Errand_Form(request, pk):
    r_request =Errand_service_PH.objects.get(id=pk)
    o_form = AdminErrandForm(instance= r_request)
    customer = Customer.objects.get(user=request.user)          

    if request.method == 'POST':
        o_form = AdminErrandForm(request.POST,instance=r_request)
        if o_form.is_valid():
            obj = o_form.save(commit=False)
            obj.save()    
            get_rider = obj.riders

            if obj.status != 'Delivered' and get_rider == None:
                messages.warning(request, f'You just updated a customer status to {obj.status}')                     
            elif obj.status != 'Delivered' and get_rider != None:
                RidersProfile_PH.objects.filter(pk = get_rider.pk).update(busy = True)
                messages.warning(request, f'You just updated a customer status to {obj.status}')
            elif obj.status == 'Canceled' and get_rider == None:
                messages.warning(request, f'You just updated a customer status to canceled: {obj.order_id} and No rider was assigned')                
            elif obj.status == 'Canceled' and get_rider != None: 
                RidersProfile_PH.objects.filter(pk = get_rider.pk).update(busy = False)
                messages.warning(request, f'You just updated a customer status to canceled: {obj.order_id}')

            if get_rider != None:
                Errand_service_PH.objects.filter(pk = obj.pk).update(assigned = True)

            if obj.status == 'Delivered':                                               
                #search_makeRequest = MakeRequest.objects.filter(riders = get_rider).filter(status = 'Pending').exists()
                #search_makeRequest_out = MakeRequest.objects.filter(riders = get_rider).filter(status = 'Out for delivery').exists()
                search_makeRequestCash = MakeRequestCash_PH.objects.filter(riders = get_rider).filter(status = 'Pending').exists()
                search_makeRequestCash_out = MakeRequestCash_PH.objects.filter(riders = get_rider).filter(status = 'Out for delivery').exists()
                search_errand = Errand_service_PH.objects.filter(riders = get_rider).filter(status = 'Pending').exists()
                search_errand_process = Errand_service_PH.objects.filter(riders = get_rider).filter(status = 'Purchase in Process').exists()
                search_errand_out = Errand_service_PH.objects.filter(riders = get_rider).filter(status = 'On Route for Delivery').exists()
                #search_anon = Anonymous.objects.filter(riders = get_rider).filter(status = 'Pending').exists()
                #search_anon_out = Anonymous.objects.filter(riders = get_rider).filter(status = 'Out for delivery').exists()
                search_shopping = Shopping_PH.objects.filter(riders = get_rider).filter(status = 'Pending').exists()
                search_shopping_out = Shopping_PH.objects.filter(riders = get_rider).filter(status = 'At the Mall').exists()
                search_frontDesk = Front_desk_PH.objects.filter(riders = get_rider).filter(status = 'Pending').exists()
                search_frontDesk_out = Front_desk_PH.objects.filter(riders = get_rider).filter(status = 'Out for delivery').exists()

                all_search = [
                            #search_makeRequest, search_makeRequest_out, 
                            search_makeRequestCash, search_makeRequestCash_out, 
                            search_errand, search_errand_process, search_errand_out,
                            #search_anon, search_anon_out,
                            search_shopping, search_shopping_out, 
                            search_frontDesk, search_frontDesk_out
                            ]                
                                                       
                the_count = all_search.count(False)
                if the_count >= 13:
                    RidersProfile_PH.objects.filter(pk = get_rider.pk).update(busy = False)

            chk_delivered = customer.delivered_set.filter(order_id = obj.order_id).exists()            
            if obj.status == 'Delivered' and chk_delivered == True:                
                messages.success(request, f'You just updated a customer satus: {obj.order_id}')
            elif obj.status == 'Delivered' and chk_delivered == False: 
                Delivered.objects.create(
                                customer=obj.customer,
                                Item_delivered = obj,
                                order_id = obj.order_id
                                )
                messages.success(request, f'You just updated a customer satus to delivered: {obj.order_id}')
            return redirect('allerrand-request')
    context = {'o_form': o_form,
              'customer':customer 
              }
    return render(request, 'users/AdminUpdateErrand.html', context)

#adminUpdateFront
@login_required(login_url='login')
@allowed_user(allowed_roles=['admin','Fleet_Manager'])
def Update_Front_Fesk_Form(request, pk):
    r_request = Front_desk_PH.objects.get(id=pk)
    o_form = AdminFrontForm(instance= r_request)
    customer = Customer.objects.get(user = request.user)         

    if request.method == 'POST':
        o_form = AdminFrontForm(request.POST, instance=r_request)
        if o_form.is_valid():
            obj = o_form.save(commit=False)
            obj.save()
            get_rider = obj.riders
            
            if obj.status != 'Delivered' and get_rider == None:
                messages.warning(request, f'You just updated a customer status to {obj.status}')                     
            elif obj.status != 'Delivered' and get_rider != None:
                RidersProfile_PH.objects.filter(pk = get_rider.pk).update(busy = True)
                messages.warning(request, f'You just updated a customer status to {obj.status}')
            elif obj.status == 'Canceled' and get_rider == None:
                messages.warning(request, f'You just updated a customer status to canceled: {obj.order_id} and No rider was assigned')                
            elif obj.status == 'Canceled' and get_rider != None: 
                RidersProfile_PH.objects.filter(pk = get_rider.pk).update(busy = False)
                messages.warning(request, f'You just updated a customer status to canceled: {obj.order_id}')

            if get_rider != None:
                Front_desk_PH.objects.filter(pk = obj.pk).update(assigned = True)

            if obj.status == 'Delivered':                                               
                #search_makeRequest = MakeRequest.objects.filter(riders = get_rider).filter(status = 'Pending').exists()
                #search_makeRequest_out = MakeRequest.objects.filter(riders = get_rider).filter(status = 'Out for delivery').exists()
                search_makeRequestCash = MakeRequestCash_PH.objects.filter(riders = get_rider).filter(status = 'Pending').exists()
                search_makeRequestCash_out = MakeRequestCash_PH.objects.filter(riders = get_rider).filter(status = 'Out for delivery').exists()
                search_errand = Errand_service_PH.objects.filter(riders = get_rider).filter(status = 'Pending').exists()
                search_errand_process = Errand_service_PH.objects.filter(riders = get_rider).filter(status = 'Purchase in Process').exists()
                search_errand_out = Errand_service_PH.objects.filter(riders = get_rider).filter(status = 'On Route for Delivery').exists()
                #search_anon = Anonymous.objects.filter(riders = get_rider).filter(status = 'Pending').exists()
                #search_anon_out = Anonymous.objects.filter(riders = get_rider).filter(status = 'Out for delivery').exists()
                search_shopping = Shopping_PH.objects.filter(riders = get_rider).filter(status = 'Pending').exists()
                search_shopping_out = Shopping_PH.objects.filter(riders = get_rider).filter(status = 'At the Mall').exists()
                search_frontDesk = Front_desk_PH.objects.filter(riders = get_rider).filter(status = 'Pending').exists()
                search_frontDesk_out = Front_desk_PH.objects.filter(riders = get_rider).filter(status = 'Out for delivery').exists()

                all_search = [
                            #search_makeRequest, search_makeRequest_out, 
                            search_makeRequestCash, search_makeRequestCash_out, 
                            search_errand, search_errand_process, search_errand_out,
                            #search_anon, search_anon_out,
                            search_shopping, search_shopping_out, 
                            search_frontDesk, search_frontDesk_out
                            ]                
                                                       
                the_count = all_search.count(False)    
                if the_count >= 13:
                    RidersProfile_PH.objects.filter(pk = get_rider.pk).update(busy = False)

            chk_delivered = customer.delivered_set.filter(order_id = obj.order_id).exists()            
            if obj.status == 'Delivered' and chk_delivered == True:                
                messages.success(request, f'You just updated a customer satus: {obj.order_id}')
            elif obj.status == 'Delivered' and chk_delivered == False: 
                Delivered.objects.create(
                                customer=obj.customer,
                                Item_delivered = obj,
                                order_id = obj.order_id
                                )
                messages.success(request, f'You just updated a customer satus to delivered: {obj.order_id}')

            return redirect('allfront-request')
    context = {'o_form': o_form,
              'customer':customer 
              }
    return render(request, 'users/AdminUpdateFront.html', context)

#Update request Anon
@login_required(login_url='login')
@admin_only
def updateRequestAnon(request, pk):
    r_request = Anonymous.objects.get(id=pk)
    a_form = AdminAnonForm(instance= r_request)        

    if request.method == 'POST':
        a_form = AdminAnonForm(request.POST,instance=r_request)
        if a_form.is_valid():
            instance = a_form.save(commit=False)
            instance.save()
            get_rider = instance.riders

            if instance.status != 'Delivered' and get_rider == None:
                messages.warning(request, f'You just updated a customer status to {instance.status}')                     
            elif instance.status != 'Delivered' and get_rider != None:
                RidersProfile_PH.objects.filter(pk = get_rider.pk).update(busy = True)
                messages.warning(request, f'You just updated a customer status to {instance.status}')
            elif instance.status == 'Canceled' and get_rider == None:
                messages.warning(request, f'You just updated a customer status to canceled: {instance.order_id} and No rider was assigned')                
            elif instance.status == 'Canceled' and get_rider != None: 
                RidersProfile_PH.objects.filter(pk = get_rider.pk).update(busy = False)
                messages.warning(request, f'You just updated a customer status to canceled: {instance.order_id}')

            if get_rider != None:
                Anonymous.objects.filter(pk = instance.pk).update(assigned = True)

            if instance.status == 'Delivered':                                               
                #search_makeRequest = MakeRequest.objects.filter(riders = get_rider).filter(status = 'Pending').exists()
                #search_makeRequest_out = MakeRequest.objects.filter(riders = get_rider).filter(status = 'Out for delivery').exists()
                search_makeRequestCash = MakeRequestCash_PH.objects.filter(riders = get_rider).filter(status = 'Pending').exists()
                search_makeRequestCash_out = MakeRequestCash_PH.objects.filter(riders = get_rider).filter(status = 'Out for delivery').exists()
                search_errand = Errand_service_PH.objects.filter(riders = get_rider).filter(status = 'Pending').exists()
                search_errand_process = Errand_service_PH.objects.filter(riders = get_rider).filter(status = 'Purchase in Process').exists()
                search_errand_out = Errand_service_PH.objects.filter(riders = get_rider).filter(status = 'On Route for Delivery').exists()
                search_anon = Anonymous.objects.filter(riders = get_rider).filter(status = 'Pending').exists()
                search_anon_out = Anonymous.objects.filter(riders = get_rider).filter(status = 'Out for delivery').exists()
                search_shopping = Shopping_PH.objects.filter(riders = get_rider).filter(status = 'Pending').exists()
                search_shopping_out = Shopping_PH.objects.filter(riders = get_rider).filter(status = 'At the Mall').exists()
                search_frontDesk = Front_desk_PH.objects.filter(riders = get_rider).filter(status = 'Pending').exists()
                search_frontDesk_out = Front_desk_PH.objects.filter(riders = get_rider).filter(status = 'Out for delivery').exists()

                all_search = [
                            #search_makeRequest, search_makeRequest_out, 
                            search_makeRequestCash, search_makeRequestCash_out, 
                            search_errand, search_errand_process, search_errand_out,
                            search_anon, search_anon_out,
                            search_shopping, search_shopping_out, 
                            search_frontDesk, search_frontDesk_out
                            ]                
                                                       
                the_count = all_search.count(False)  
                if the_count >= 13:
                    RidersProfile_PH.objects.filter(pk = get_rider.pk).update(busy = False)
            messages.success(request, f'Successful:{instance.order_id}')

            return redirect('anonymous-request')
    context = {'a_form': a_form}
    return render(request, 'users/anonform.html', context)

##### ADMIN PAGE ##################
@login_required(login_url='login')
@admin_only
def AdminDashboard_PH(request):
    #request1 = MakeRequest.objects.all()
    request2 = MakeRequestCash_PH.objects.all()
    request3 = Shopping_PH.objects.all()
    request4 = Anonymous.objects.all()
    request5 = Front_desk_PH.objects.all()
    request6 = Errand_service_PH.objects.all()

    #total amount through diff chanels
    #e_req = request1.aggregate(Sum('Amount_paid'))
    e_cash = request2.aggregate(Sum('Amount_Paid'))
    e_shop = request3.aggregate(Sum('Charge'))
    e_anon = request4.aggregate(Sum('Amount_Paid'))
    e_front = request5.aggregate(Sum('profit'))
    e_erra = request6.aggregate(Sum('profit'))

    #amount breakdown
    #a_req_1 = request1.filter(Choice_for_TP = "Bike").aggregate(Sum('Amount_paid'))
    #a_req_2 = request1.filter(Choice_for_TP = "Tricycle").aggregate(Sum('Amount_paid'))

    a_cash_1 = request2.filter(Choice_for_TP = "Bike").aggregate(Sum('Amount_Paid'))
    a_cash_2 = request2.filter(Choice_for_TP = "Tricycle").aggregate(Sum('Amount_Paid'))

    a_anon_1 = request4.filter(Choice_for_TP = "Bike").aggregate(Sum('Amount_Paid'))
    a_anon_2 = request4.filter(Choice_for_TP = "Tricycle").aggregate(Sum('Amount_Paid'))

    a_shop_paid = request3.aggregate(Sum('amount_paid'))
    a_shop_charge = request3.aggregate(Sum('Charge'))
    a_shop_cost = request3.aggregate(Sum('Item_Cost'))
    a_shop_refund = request3.aggregate(Sum('Amount_Refunded'))

    a_errand_AmtPaid = request6.aggregate(Sum('Amount_Paid'))
    a_errand_profit = request6.aggregate(Sum('profit'))

    a_front_AmtPaid = request5.aggregate(Sum('Amount_Paid'))
    a_front_profit = request5.aggregate(Sum('profit'))    
    
    customer = Customer.objects.get( user= request.user )
    customers = Customer.objects.all()

    #myFilter5 = AdminFilterUsers(request.GET, queryset = customers)
    #customers = myFilter5.qs

    #total_request_online = request1.count()
    total_request_cash = request2.count()
    total_request_shopping = request3.count()
    total_request_anonymous = request4.count()
    total_request_front = request5.count()
    total_request_errand = request6.count()

    #delivered = request1.filter(status='Delivered').count()
    #pending = request1.filter(status='Pending').count()
    #canceled = request1.filter(status='Canceled').count()
    #out_for_delivery = request1.filter(status='Out for delivery').count()

    delivered1 = request2.filter(status='Delivered').count()
    pending1 = request2.filter(status='Pending').count()
    canceled1 = request2.filter(status='Canceled').count()
    out_for_delivery1 = request2.filter(status='Out for delivery').count()

    delivered2 = request3.filter(status='Delivered').count()
    pending2 = request3.filter(status='Pending').count()
    canceled2 = request3.filter(status='Canceled').count()
    at_the_mall = request3.filter(status='At the Mall').count()

    delivered3 = Anonymous.objects.filter(status = 'Delivered').count()
    pending3 = Anonymous.objects.filter(status = 'Pending').count()
    canceled3 = Anonymous.objects.filter(status = 'Canceled').count()
    out_for_delivery2 = Anonymous.objects.filter(status = 'Out for delivery').count()

    delivered4 = request5.filter(status='Delivered').count()
    pending4 = request5.filter(status = 'Pending').count()
    cancled4 = request5.filter(status = 'Canceled').count()
    out_for_delivery4 = request5.filter(status = 'Out for delivery').count()

    delivered5 = request6.filter(status = "Delivered").count()
    pending5 = request6.filter(status = "Pending").count()
    on_route5 = request6.filter(status = "On Route for Delivery").count()
    pur_in_process = request6.filter(status = 'Purchase in Process').count()

    notification_filter =  PH_adminNotification.objects.all()
    notify = notification_filter.filter(viewed = False) 
    
    context = {
        'total_request_front':total_request_front,
        'total_request_errand':total_request_errand,
        'delivered4':delivered4,
        'pending4':pending4,
        'cancled4':cancled4,
        'out_for_delivery4':out_for_delivery4,

        'delivered5':delivered5,
        'pending5':pending5,
        'on_route5':on_route5,
        'pur_in_process':pur_in_process,

        'a_shop_paid':a_shop_paid,
        'a_shop_charge':a_shop_charge,
        'a_shop_cost':a_shop_cost,
        'a_shop_refund':a_shop_refund,

        #'a_req_1':a_req_1,
        #'a_req_2':a_req_2,
        'a_cash_1':a_cash_1,
        'a_cash_2':a_cash_2,
        'a_anon_1':a_anon_1,
        'a_anon_2':a_anon_2,

        'a_errand_AmtPaid':a_errand_AmtPaid,
        'a_errand_profit':a_errand_profit,

        'a_front_AmtPaid':a_front_AmtPaid,
        'a_front_profit':a_front_profit,

        #'e_req':e_req,
        'e_cash': e_cash,
        'e_shop':e_shop,
        'e_anon':e_anon,
        'e_erra':e_erra,
        'e_front':e_front,

        #'myFilter5':myFilter5,
        'notify':notify, 

        #'request1': request1, 
        'request2':request2,
        'request3':request3,
        'request4':request4,

        'customer':customer,
        'customers' : customers,

        #'total_request_online': total_request_online,
        'total_request_cash':total_request_cash,
        'total_request_shopping':total_request_shopping,
        'total_request_anonymous':total_request_anonymous ,
        
        #'out_for_delivery':out_for_delivery,
        'out_for_delivery1':out_for_delivery1,
        'out_for_delivery2':out_for_delivery2,

        #'pending': pending,
        'pending1': pending1,
        'pending2': pending2,
        'pending3': pending3,

        #'canceled': canceled,
        'canceled1': canceled1,
        'canceled2': canceled2, 
        'canceled3': canceled3,        

        #'delivered': delivered,
        'delivered1': delivered1,
        'delivered2': delivered2,
        'delivered3':delivered3,

        'at_the_mall': at_the_mall,
        }

    return render(request, 'PortHarcourt/DashboardBase.html', context)
