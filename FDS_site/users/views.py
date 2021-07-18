
from BikeControl.models import RidersDeliveries, RidersProfile
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from django.http import HttpResponseRedirect

from django.contrib.auth.models import Group
from hashids import Hashids
from .models import *

from django.http import Http404

from django.conf import settings

from django.db.models import Sum

from django.contrib import messages #flash message
from .forms import *

from .filters import OrderFilter, AdminFilter, AdminFilterUsers

from .decorators import unauthenticated_user, allowed_user, admin_only

import requests

from django.core.paginator import Paginator

import json

from django.db.models import Q

#Error 404 page
def response_error_handler(request, exception = None):
    return render(request, 'users/404.html', status=404)

#Register Page
@unauthenticated_user
def register(request):
    form = UserRegisterForm
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.customer.first_name = form.cleaned_data.get('first_name')
            user.customer.last_name = form.cleaned_data.get('last_name')
            user.customer.phone_number = form.cleaned_data.get('phone_number')
            user.customer.email = form.cleaned_data.get('email')
            username = form.cleaned_data.get( 'username')
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            user.save()
            
            messages.success(request, f' Hello {username} Your account has been created! You are now able to log in !')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/signUp.html', {'form':form})

#Password update Page
@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'customer', 'Fleet Manager', 'Front Desk', 'Cashier'])
def PasswordChange(request, user):
    customer = Customer.objects.get(user=request.user)
    n_filter = customer.delivered_set.all()
    n = n_filter.filter(viewed = False)
    if request.method == 'POST':
        pc_form = PasswordChangeForm(request.user, request.POST)
        if  pc_form.is_valid(): 
            pc_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, f'Your password has been sucessfully updated!')
            return redirect('profileUpdate', user=user)
        else:
            messages.error(request, f'An error occured, please correct the error below')
    else:
        pc_form =  PasswordChangeForm(request.user)
    context = {
        'customer':customer,
        'pc_form':pc_form,
        'n':n
    }
    return render(request, 'users/changePassword.html', context)

#Profile update Page
@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'customer', 'Fleet Manager', 'Front Desk', 'Cashier'])
def customerProfileUpdatePage(request, user):
    customer = Customer.objects.get(user=request.user)
    n_filter = customer.delivered_set.all()
    n = n_filter.filter(viewed = False)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=customer)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=customer)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Profile has been Updated!')
            return redirect('profileUpdate', user=user)
        else:
            messages.error(request, f'An error occured, please correcthe error below')
    else:
        u_form = UserUpdateForm(instance=customer)
        p_form = ProfileUpdateForm(instance=customer)
    context = {
        'customer':customer,
        'u_form': u_form,
        'p_form': p_form,
        'n':n
    }
    return render(request, 'users/customer_profile.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'Cashier',])
def Cashier(request, user):
    request1 = MakeRequest.objects.all()
    request2 = MakeRequestCash.objects.all()
    request3 = Shopping.objects.all()
    request4 = Anonymous.objects.all()
    request5 = Errand_service.objects.all()
    request6 = Front_desk.objects.all()

    notification_filter = adminNotification.objects.all()
    notify = notification_filter.filter(viewed = False) 

    paginator1 = Paginator(request1, 10)
    page_number1 = request.GET.get('page')
    page_obj1 = paginator1.get_page(page_number1)

    paginator2 = Paginator(request2, 10)
    page_number2 = request.GET.get('page')
    page_obj2 = paginator2.get_page(page_number2)

    paginator3 = Paginator(request3, 10)
    page_number3 = request.GET.get('page')
    page_obj3 = paginator3.get_page(page_number3)
    
    paginator4 = Paginator(request4, 10)
    page_number4 = request.GET.get('page')
    page_obj4 = paginator4.get_page(page_number4)

    paginator5 = Paginator(request5, 10)
    page_number5 = request.GET.get('page')
    page_obj5 = paginator5.get_page(page_number5)

    paginator6 = Paginator(request6, 10)
    page_number6 = request.GET.get('page')
    page_obj6 = paginator6.get_page(page_number6)

    #total amount through diff chanels
    e_req = request1.aggregate(Sum('Amount_paid'))
    e_cash = request2.aggregate(Sum('Amount_Paid'))
    e_shop = request3.aggregate(Sum('Charge'))
    e_anon = request4.aggregate(Sum('Amount_Paid'))
    e_erra = request5.aggregate(Sum('profit'))
    e_front = request6.aggregate(Sum('profit'))
   
    context = {
        
        'e_req':e_req,
        'e_cash':e_cash,
        'e_shop':e_shop,
        'e_anon':e_anon,
        'e_erra':e_erra,
        'e_front':e_front,

        'notify':notify,

        'page_obj1':page_obj1,
        'page_obj2':page_obj2,
        'page_obj3':page_obj3,
        'page_obj4':page_obj4,
        'page_obj5':page_obj5,
        'page_obj6':page_obj6,
    }

    return render(request, 'users/Cashier.html', context)

#Fleet Manager page
@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'Fleet Manager'])
def FleetManager(request, user):    
    request1 = MakeRequest.objects.all()
    request2 = MakeRequestCash.objects.all()
    request3 = Shopping.objects.all()
    request4 = Anonymous.objects.all()
    request5 = Errand_service.objects.all()
    request6 = Front_desk.objects.all()
    
    assign = RidersDeliveries.objects.all()
                
    notification_filter = adminNotification.objects.all()
    notify = notification_filter.filter(viewed = False) 

    chk_pen = request1.filter(status = 'Pending').count()
    chk_pen2 = request2.filter(status = 'Pending').count()
    chk_pen3 = request3.filter(status = 'Pending').count()
    chk_pen4 = request4.filter(status = 'Pending').count()
    chk_pen5 = request5.filter(status = 'Pending').count()
    chk_pen6 = request6.filter(status = 'Pending').count()

    chk_out = request1.filter(status = 'Out for delivery').count()
    chk_out2 = request2.filter(status = 'Out for delivery').count()
    chk_out3 = request3.filter(status = 'At the Mall').count()
    chk_out4 = request4.filter(status = 'Out for delivery').count()
    chk_out5 = request5.filter(status = 'On Route for Delivery').count()
    chk_out5of5 = request5.filter(status = 'Purchase in Process').count()
    chk_out6 = request6.filter(status = 'Out for delivery').count()      

    paginator1 = Paginator(request1, 10)
    page_number1 = request.GET.get('page')
    page_obj1 = paginator1.get_page(page_number1)

    paginator2 = Paginator(request2, 10)
    page_number2 = request.GET.get('page')
    page_obj2 = paginator2.get_page(page_number2)

    paginator3 = Paginator(request3, 10)
    page_number3 = request.GET.get('page')
    page_obj3 = paginator3.get_page(page_number3)
    
    paginator4 = Paginator(request4, 10)
    page_number4 = request.GET.get('page')
    page_obj4 = paginator4.get_page(page_number4)

    paginator5 = Paginator(request5, 10)
    page_number5 = request.GET.get('page')
    page_obj5 = paginator5.get_page(page_number5)

    paginator6 = Paginator(request6, 10)
    page_number6 = request.GET.get('page')
    page_obj6 = paginator6.get_page(page_number6)

   
    
    context = {
        'assign':assign,

        'notify':notify,

        'chk_pen':chk_pen,
        'chk_pen2':chk_pen2,
        'chk_pen3':chk_pen3,
        'chk_pen4':chk_pen4,
        'chk_pen5':chk_pen5,
        'chk_pen6':chk_pen6,
        
        'chk_out':chk_out,
        'chk_out2':chk_out2,
        'chk_out3':chk_out3,
        'chk_out4':chk_out4,
        'chk_out5':chk_out5,
        'chk_out5of5':chk_out5of5,
        'chk_out6':chk_out6,

        'page_obj1':page_obj1,
        'page_obj2':page_obj2,
        'page_obj3':page_obj3,
        'page_obj4':page_obj4,
        'page_obj5':page_obj5,
        'page_obj6':page_obj6,
    }

    return render(request, 'users/FleetManager.html', context)

#Front desk page
@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'Front Desk'])
def front_desk(request, user):
    request1 = MakeRequest.objects.all()
    request2 = MakeRequestCash.objects.all()
    request3 = Shopping.objects.all()
    request4 = Anonymous.objects.all()
    request5 = Errand_service.objects.all()
    request6 = Front_desk.objects.all()

    customer = Customer.objects.get( user= user )
    notification_filter = adminNotification.objects.all()
    notify = notification_filter.filter(viewed = False) 

    chk_pen = request1.filter(status = 'Pending').count()
    chk_pen2 = request2.filter(status = 'Pending').count()
    chk_pen3 = request3.filter(status = 'Pending').count()
    chk_pen4 = request4.filter(status = 'Pending').count()
    chk_pen5 = request5.filter(status = 'Pending').count()
    chk_pen6 = request6.filter(status = 'Pending').count()

    chk_out = request1.filter(status = 'Out for delivery').count()
    chk_out2 = request2.filter(status = 'Out for delivery').count()
    chk_out3 = request3.filter(status = 'At the Mall').count()
    chk_out4 = request4.filter(status = 'Out for delivery').count()
    chk_out5 = request5.filter(status = 'On Route for Delivery').count()
    chk_out5of5 = request5.filter(status = 'Purchase in Process').count()
    chk_out6 = request6.filter(status = 'Out for delivery').count()

    paginator1 = Paginator(request1, 10)
    page_number1 = request.GET.get('page')
    page_obj1 = paginator1.get_page(page_number1)

    paginator2 = Paginator(request2, 10)
    page_number2 = request.GET.get('page')
    page_obj2 = paginator2.get_page(page_number2)

    paginator3 = Paginator(request3, 10)
    page_number3 = request.GET.get('page')
    page_obj3 = paginator3.get_page(page_number3)
    
    paginator4 = Paginator(request4, 10)
    page_number4 = request.GET.get('page')
    page_obj4 = paginator4.get_page(page_number4)

    paginator5 = Paginator(request5, 10)
    page_number5 = request.GET.get('page')
    page_obj5 = paginator5.get_page(page_number5)

    paginator6 = Paginator(request6, 10)
    page_number6 = request.GET.get('page')
    page_obj6 = paginator6.get_page(page_number6)


    context = {
        'notify':notify,

        'chk_pen':chk_pen,
        'chk_pen2':chk_pen2,
        'chk_pen3':chk_pen3,
        'chk_pen4':chk_pen4,
        'chk_pen5':chk_pen5,
        'chk_pen6':chk_pen6,
        
        'chk_out':chk_out,
        'chk_out2':chk_out2,
        'chk_out3':chk_out3,
        'chk_out4':chk_out4,
        'chk_out5':chk_out5,
        'chk_out5of5':chk_out5of5,
        'chk_out6':chk_out6,

        'page_obj1':page_obj1,
        'page_obj2':page_obj2,
        'page_obj3':page_obj3,
        'page_obj4':page_obj4,
        'page_obj5':page_obj5,
        'page_obj6':page_obj6,
    }

    return render(request, 'users/FrontDesk.html', context)

# Front desk pick drop form
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
            Front_desk.objects.filter(pk = instance.id).update(order_id= h)

            adminNotification.objects.create(
                customer=instance.customer,
                item_created = instance,
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

            messages.success(request, f'Hello {request.user.username}, action Successful')

            hashids = Hashids(salt=settings.FRONT_DESK, min_length=7)
            h = hashids.encode(instance.id)
            Front_desk.objects.filter(pk = instance.id).update(order_id= h)

            adminNotification.objects.create(
                customer=instance.customer,
                item_created = instance,
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


def Inhousesearch(request):
    results = []
    results2 = []
    results3 = []
    if request.method == "GET":
        query = request.GET.get('order_id')

        if query == '':
            query = 'None'
        results = Anonymous.objects.filter(Q(order_id = query))
        results2 = Errand_service.objects.filter(Q(order_id = query))
        results3 = Shopping.objects.filter(Q(order_id = query))
        results4 = MakeRequest.objects.filter(Q(order_id = query))
        results5 = MakeRequestCash.objects.filter(Q(order_id = query))
        results6 = Front_desk.objects.filter(Q(order_id = query))
        
    context = {
            'query': query, 
            'results':results, 
            'results2':results2,
            'results3':results3,
            'results4':results4,
            'results5':results5,
            'results6':results6,
    }
    
    return render(request, 'users/Search.html', context)
# Cash Request
@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'customer', 'Fleet Manager', 'Front Desk', 'Cashier'])
def requestForm_Cash(request, user):
    customer = Customer.objects.get(user=request.user)
    n_filter = customer.delivered_set.all()
    n = n_filter.filter(viewed = False)
    if request.method == 'POST':
        c_form = Request_Cash(request.POST)
        if c_form.is_valid():
            instance = c_form.save(commit=False)
            instance.customer = customer
            instance.save()
            messages.success(request, f'Your Request for pickup is Successful, you will recieve a call from us shortly')

            hashids = Hashids(salt=settings.HASH, min_length=7)
            h = hashids.encode(instance.id)
            MakeRequestCash.objects.filter(pk = instance.id).update(order_id= h)
            
            tp_choice_1 = customer.makerequestcash_set.filter(order_id = h).filter(Choice_for_TP= 'Bike' )
            tp_choice_2 = customer.makerequestcash_set.filter(order_id = h).filter(Choice_for_TP= 'Tricycle' )            

            #checking for multiple
            chk_none = customer.makerequestcash_set.get(order_id = h)
                    
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
                count_item2 = item_2.count(None)
                count_item3 = item_3.count(None)
                count_item4 = item_4.count(None)
                count_item5 = item_5.count(None)
                customer.makerequestcash_set.filter(order_id = h).update(Amount_Payable = charge_amount)
                if count_item2 >= 3:
                    pass
                else:
                    charge_amount += 500
                    customer.makerequestcash_set.filter(order_id = h).update(Amount_Payable = charge_amount)

                if count_item3 >= 3:
                    pass
                else:
                    charge_amount += 500
                    customer.makerequestcash_set.filter(order_id = h).update(Amount_Payable = charge_amount)

                if count_item4 >= 3:
                    pass
                else:
                    charge_amount += 500
                    customer.makerequestcash_set.filter(order_id = h).update(Amount_Payable = charge_amount)
                
                if count_item5 >= 3:
                    pass
                else:
                    charge_amount += 500
                    customer.makerequestcash_set.filter(order_id = h).update(Amount_Payable = charge_amount)

                if charge_amount == 1000:
                    messages.success(request, f'Your choice of transportation is Bike Your delivery Fee is NGN{charge_amount}, Total Deliveries is 2 ')
                elif charge_amount == 1500:
                    messages.success(request, f'Your choice of transportation is Bike Your delivery Fee is NGN{charge_amount}, Total Deliveries is 3')
                elif charge_amount == 2000:
                    messages.success(request, f'Your choice of transportation is Bike Your delivery Fee is NGN{charge_amount}, Total Deliveries is 4')
                elif charge_amount == 2500:
                    messages.success(request, f'Your choice of transportation is Bike Your delivery Fee is NGN{charge_amount}, Total Deliveries is 5')
                else:
                    messages.success(request, f'Your choice of transportation is Bike Your delivery Fee is NGN{charge_amount}, Single Delivery.')
            
            if tp_choice_2:
                count_item2 = item_2.count(None)
                count_item3 = item_3.count(None)
                count_item4 = item_4.count(None)
                count_item5 = item_5.count(None)
                charge_amount = 1000
                customer.makerequestcash_set.filter(order_id = h).update(Amount_Payable = charge_amount)
                if count_item2 >= 3:
                    pass
                else:
                    charge_amount += 1000
                    customer.makerequestcash_set.filter(order_id = h).update(Amount_Payable = charge_amount)

                if count_item3 >= 3:
                    pass
                else:
                    charge_amount += 1000
                    customer.makerequestcash_set.filter(order_id = h).update(Amount_Payable = charge_amount)

                if count_item4 >= 3:
                    pass
                else:
                    charge_amount += 1000
                    customer.makerequestcash_set.filter(order_id = h).update(Amount_Payable = charge_amount)
                
                if count_item5 >= 3:
                    pass
                else:
                    charge_amount += 1000
                    customer.makerequestcash_set.filter(order_id = h).update(Amount_Payable = charge_amount)

                if charge_amount == 2000:
                    messages.success(request, f'Your choice of transportation is Bike Your delivery Fee is NGN{charge_amount}, Total Deliveries is 2 ')
                elif charge_amount == 3000:
                    messages.success(request, f'Your choice of transportation is Bike Your delivery Fee is NGN{charge_amount}, Total Deliveries is 3')
                elif charge_amount == 4000:
                    messages.success(request, f'Your choice of transportation is Bike Your delivery Fee is NGN{charge_amount}, Total Deliveries is 4')
                elif charge_amount == 5000:
                    messages.success(request, f'Your choice of transportation is Bike Your delivery Fee is NGN{charge_amount}, Total Deliveries is 5')
                else:
                    messages.success(request, f'Your choice of transportation is Bike Your delivery Fee is NGN{charge_amount}, Single Delivery.')
            ForPayments.objects.create(
                customer = customer,
                For_cash_payment = instance,
                order_id = h
            )

            adminNotification.objects.create(
                customer=instance.customer,
                item_created = instance,
                order_id = h   
            ) 

            return redirect('dashboard', user=user)
    else:
        c_form = Request_Cash(instance=customer)
            
    context = {
        'c_form': c_form,
        'customer':customer,
        'n':n,
        }
    return render(request, 'users/requestForm_Cash.html', context)

#Online payment request
@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'customer', 'Fleet Manager', 'Front Desk', 'Cashier'])
def requestForm_Online(request, user):
    customer = Customer.objects.get(user=request.user)
    n_filter = customer.delivered_set.all()
    n = n_filter.filter(viewed = False)
    if request.method == 'POST':
        o_form = OrderForm(request.POST)
        if o_form.is_valid() : 
            instance = o_form.save(commit=False)
            instance.customer = customer
            instance.save()
            messages.success(request, f'Your Request for pickup is Successful, you will recieve a call from us shortly')

            hashids = Hashids(salt=settings.API_KEY, min_length=7)
            h = hashids.encode(instance.id)
            MakeRequest.objects.filter(pk = instance.id).update(order_id=h)
            
            tp_choice_1 = customer.makerequest_set.filter(order_id = h).filter(Choice_for_TP= 'Bike')
            tp_choice_2 = customer.makerequest_set.filter(order_id = h).filter(Choice_for_TP= 'Tricycle')

            #checking for multiple
            chk_none = customer.makerequest_set.get(order_id = h)
                    
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
                count_item2 = item_2.count(None)
                count_item3 = item_3.count(None)
                count_item4 = item_4.count(None)
                count_item5 = item_5.count(None)
                customer.makerequest_set.filter(order_id = h).update(Amount_Payable = charge_amount)
                if count_item2 >= 3:
                    pass
                else:
                    charge_amount += 500
                    customer.makerequest_set.filter(order_id = h).update(Amount_Payable = charge_amount)

                if count_item3 >= 3:
                    pass
                else:
                    charge_amount += 500
                    customer.makerequest_set.filter(order_id = h).update(Amount_Payable = charge_amount)

                if count_item4 >= 3:
                    pass
                else:
                    charge_amount += 500
                    customer.makerequest_set.filter(order_id = h).update(Amount_Payable = charge_amount)
                
                if count_item5 >= 3:
                    pass
                else:
                    charge_amount += 500
                    customer.makerequest_set.filter(order_id = h).update(Amount_Payable = charge_amount)

                if charge_amount == 1000:
                    messages.success(request, f'Your choice of transportation is Bike Your delivery Fee is NGN{charge_amount}, Total Deliveries is 2 ')
                elif charge_amount == 1500:
                    messages.success(request, f'Your choice of transportation is Bike Your delivery Fee is NGN{charge_amount}, Total Deliveries is 3')
                elif charge_amount == 2000:
                    messages.success(request, f'Your choice of transportation is Bike Your delivery Fee is NGN{charge_amount}, Total Deliveries is 4')
                elif charge_amount == 2500:
                    messages.success(request, f'Your choice of transportation is Bike Your delivery Fee is NGN{charge_amount}, Total Deliveries is 5')
                else:
                    messages.success(request, f'Your choice of transportation is Bike Your delivery Fee is NGN{charge_amount}, Single Delivery.')
            
            if tp_choice_2:
                count_item2 = item_2.count(None)
                count_item3 = item_3.count(None)
                count_item4 = item_4.count(None)
                count_item5 = item_5.count(None)
                charge_amount = 1000
                customer.makerequest_set.filter(order_id = h).update(Amount_Payable = charge_amount)
                if count_item2 >= 3:
                    pass
                else:
                    charge_amount += 1000
                    customer.makerequest_set.filter(order_id = h).update(Amount_Payable = charge_amount)

                if count_item3 >= 3:
                    pass
                else:
                    charge_amount += 1000
                    customer.makerequest_set.filter(order_id = h).update(Amount_Payable = charge_amount)

                if count_item4 >= 3:
                    pass
                else:
                    charge_amount += 1000
                    customer.makerequest_set.filter(order_id = h).update(Amount_Payable = charge_amount)
                
                if count_item5 >= 3:
                    pass
                else:
                    charge_amount += 1000
                    customer.makerequest_set.filter(order_id = h).update(Amount_Payable = charge_amount)

                if charge_amount == 2000:
                    messages.success(request, f'Your choice of transportation is Bike Your delivery Fee is NGN{charge_amount}, Total Deliveries is 2 ')
                elif charge_amount == 3000:
                    messages.success(request, f'Your choice of transportation is Bike Your delivery Fee is NGN{charge_amount}, Total Deliveries is 3')
                elif charge_amount == 4000:
                    messages.success(request, f'Your choice of transportation is Bike Your delivery Fee is NGN{charge_amount}, Total Deliveries is 4')
                elif charge_amount == 5000:
                    messages.success(request, f'Your choice of transportation is Bike Your delivery Fee is NGN{charge_amount}, Total Deliveries is 5')
                else:
                    messages.success(request, f'Your choice of transportation is Bike Your delivery Fee is NGN{charge_amount}, Single Delivery.')            
            
            def initialize_card_payent(request, user):                
                url = "https://api.paystack.co/transaction/initialize"
                the_amt = customer.makerequest_set.get(order_id = h)
                amt =the_amt.Amount_Payable                
                if amt >= 2500:
                    get_amount = 1.5001/100 * amt + 100
                    get_amt = amt + get_amount
                    final_amt = int(get_amt * 100)
                    payload = json.dumps({                        
                        'email': request.user.email,
                        'amount': final_amt,                        
                    })
                else:
                    get_amount2 = 1.5001/100 * amt
                    get_amt2 = amt + get_amount2
                    final_amt2 = int(get_amt2) * 100
                    payload = json.dumps({                        
                        'email': request.user.email,
                        'amount': final_amt2,                        
                    })
                headers = {
                    "Authorization": 'Bearer sk_test_1d32c71fd73944bd712f5b94853de7fe325387ec',
                    'Content-Type': 'application/json'
                }

                r = requests.request('POST', url, headers=headers, data=payload)

                if r.status_code != 200:
                    return str(r.status_code)
                result = r.json()                
                return result
            initialized = initialize_card_payent(request, user)            
            customer.makerequest_set.filter(pk = instance.id).update(charge_id = initialized['data']['reference'])
            link = initialized['data']['authorization_url']
            adminNotification.objects.create(
                customer=instance.customer,
                item_created = instance,
                order_id = h  
            ) 
            return HttpResponseRedirect(link)
    else:
        o_form = OrderForm(instance=customer)
    context = {
        'customer':customer, 
        'o_form': o_form,
        'n':n,
         }
    return render(request, 'users/requestForm.html', context)         

#Shopping Request
@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'customer', 'Fleet Manager', 'Front Desk', 'Cashier'])
def ShoppingForm(request, user):
    customer = Customer.objects.get(user=user)
    n_filter = customer.delivered_set.all()
    n = n_filter.filter(viewed = False)
    if request.method == "POST":
        s_form = Shopping_Form(request.POST)
        if s_form.is_valid():
            instance = s_form.save(commit=False)
            instance.customer = customer
            instance.save()

            hashids = Hashids(salt=settings.HASHID_FIELD_SALT, min_length=7)
            h = hashids.encode(instance.id)
            Shopping.objects.filter(pk = instance.id).update(order_id=h)            

            if instance.payment_channel == 'Card/Transfer':
                def initialize_payment(request, user):
                    url = "https://api.paystack.co/transaction/initialize"
                    the_amt = customer.shopping_set.get(order_id = h)  
                    amt = the_amt.Amount  
                    if amt >= 2500:
                        get_amount = 1.5001/100 * amt + 100
                        get_amt = amt + get_amount
                        final_amt = int(get_amt) * 100
                        payload = json.dumps({
                            'email':request.user.email,
                            'amount': final_amt,
                        })
                    else:
                        get_amount2 = 1.5001/100 * amt
                        get_amt2 = amt + get_amount2
                        final_amt = int(get_amt2) * 100
                        payload = json.dumps({
                            'email':request.user.email,
                            'ammount':final_amt,
                        })
                    headers = {
                        "Authorization": settings.PAYSTACK_SECRETKEY,
                        'Content-Type': 'application/json'
                        }
                    r = requests.request('POST', url, headers=headers, data=payload)
                    if r.status_code != 200:
                        return str(r.status_code) 
                    result = r.json()
                    return result
            initialized = initialize_payment(request, user)
            print(initialized)            
            customer.shopping_set.filter(pk = instance.id).update(Ps_reference = initialized['data']['reference'])
            link = initialized['data']['authorization_url']
            
            adminNotification.objects.create(
            customer=instance.customer,
            item_created = instance,
            order_id = h   
            ) 

            messages.success(request, f'Your Request has been recieved')            
            return HttpResponseRedirect(link)        
    else:
        s_form=Shopping_Form(instance=customer)

    return render (request, 'users/shopping.html', {'s_form':s_form, 'n':n})          

#Success Page
@login_required(login_url='login')
def successPage(request, user):
    customer = Customer.objects.get(user=request.user)
    reference = request.GET.get('reference')
    check_pay = customer.makerequest_set.filter(charge_id=reference).exists()
    check_errand_pay = customer.errand_service_set.filter(Ps_reference =reference).exists()
    check_shopping_pay = customer.shopping_set.filter(Ps_reference =reference).exists()
    if check_pay == True: 
        payment = customer.makerequest_set.get(charge_id=reference)
        def verify_payment(request):
            url = "https://api.paystack.co/transaction/verify/"+reference

            headers = { 
            "Authorization": settings.PAYSTACK_SECRETKEY,
            'Content-Type': 'appliation/json'
            }
            payload =json.dumps ({
                "reference": payment.charge_id
            })
            r = requests.get( url, headers=headers, data=payload)
            if r.status_code != 200:
                return str(r.status_code)
            result = r.json()            
            return result
        initialized = verify_payment(request)        
        if initialized['data']['status'] == 'success':                                             
            req2 = initialized['data']['reference']            
            request_p = customer.makerequest_set.filter(charge_id = req2).exists()     
            print('is a', request_p)                        
            customer.makerequest_set.filter(charge_id = req2).update(paid=True, Amount_paid=initialized['data']['amount']/100)

    if  check_errand_pay == True:
        payment = customer.errand_service_set.get(Ps_reference =reference)
        def verify_payment(request):
            url = "https://api.paystack.co/transaction/verify/"+reference

            headers = { 
            "Authorization": settings.PAYSTACK_SECRETKEY,
            'Content-Type': 'appliation/json'
            }

            payload =json.dumps ({
                "reference": payment.Ps_reference
            })

            r = requests.get( url, headers=headers, data=payload)
            if r.status_code != 200:
                return str(r.status_code)
            result = r.json()            
            return result        
        initialized = verify_payment(request)        
        if initialized['data']['status'] == 'success':                                             
            req2 = initialized['data']['reference']
            errand = customer.errand_service_set.filter(Ps_reference = req2).exists()            
            print('is', errand)            
            customer.errand_service_set.filter(Ps_reference = req2).update(paid=True, Amount_Paid=initialized['data']['amount']/100)
    
    if  check_shopping_pay == True:
        payment = customer.shopping_set.get(Ps_reference =reference)
        def verify_payment(request):
            url = "https://api.paystack.co/transaction/verify/"+reference

            headers = { 
            "Authorization": settings.PAYSTACK_SECRETKEY,
            'Content-Type': 'appliation/json'
            }

            payload =json.dumps ({
                "reference": payment.Ps_reference
            })

            r = requests.get( url, headers=headers, data=payload)
            if r.status_code != 200:
                return str(r.status_code)
            result = r.json()            
            return result        
        initialized = verify_payment(request)        
        if initialized['data']['status'] == 'success':                                             
            req2 = initialized['data']['reference']            
            customer.shopping_set.filter(Ps_reference = req2).update(paid=True, amount_paid=initialized['data']['amount']/100)           
    return render(request, 'users/success.html')

#Admin Dashboard
@login_required(login_url='login')
@admin_only
def AdminDashboard(request):
    request1 = MakeRequest.objects.all()
    request2 = MakeRequestCash.objects.all()
    request3 = Shopping.objects.all()
    request4 = Anonymous.objects.all()
    request5 = Front_desk.objects.all()
    request6 = Errand_service.objects.all()

    #total amount through diff chanels
    e_req = request1.aggregate(Sum('Amount_paid'))
    e_cash = request2.aggregate(Sum('Amount_Paid'))
    e_shop = request3.aggregate(Sum('Charge'))
    e_anon = request4.aggregate(Sum('Amount_Paid'))
    e_front = request5.aggregate(Sum('profit'))
    e_erra = request6.aggregate(Sum('profit'))

    #amount breakdown
    a_req_1 = request1.filter(Choice_for_TP = "Bike").aggregate(Sum('Amount_paid'))
    a_req_2 = request1.filter(Choice_for_TP = "Tricycle").aggregate(Sum('Amount_paid'))

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
   
    notify = adminNotification.objects.all()
    
    customer = Customer.objects.get( user= request.user )
    customers = Customer.objects.all()

    myFilter5 = AdminFilterUsers(request.GET, queryset = customers)
    customers = myFilter5.qs

    total_request_online = request1.count()
    total_request_cash = request2.count()
    total_request_shopping = request3.count()
    total_request_anonymous = Anonymous.objects.count()
    total_request_front = Front_desk.objects.count()
    total_request_errand = Errand_service.objects.count()

    delivered = request1.filter(status='Delivered').count()
    pending = request1.filter(status='Pending').count()
    canceled = request1.filter(status='Canceled').count()
    out_for_delivery = request1.filter(status='Out for delivery').count()

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

    notification_filter = adminNotification.objects.all()
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

        'a_req_1':a_req_1,
        'a_req_2':a_req_2,
        'a_cash_1':a_cash_1,
        'a_cash_2':a_cash_2,
        'a_anon_1':a_anon_1,
        'a_anon_2':a_anon_2,

        'a_errand_AmtPaid':a_errand_AmtPaid,
        'a_errand_profit':a_errand_profit,

        'a_front_AmtPaid':a_front_AmtPaid,
        'a_front_profit':a_front_profit,

        'e_req':e_req,
        'e_cash': e_cash,
        'e_shop':e_shop,
        'e_anon':e_anon,
        'e_erra':e_erra,
        'e_front':e_front,

        'myFilter5':myFilter5,
        'notify':notify, 

        'request1': request1, 
        'request2':request2,
        'request3':request3,
        'request4':request4,

        'customer':customer,
        'customers' : customers,

        'total_request_online': total_request_online,
        'total_request_cash':total_request_cash,
        'total_request_shopping':total_request_shopping,
        'total_request_anonymous':total_request_anonymous ,
        
        'out_for_delivery':out_for_delivery,
        'out_for_delivery1':out_for_delivery1,
        'out_for_delivery2':out_for_delivery2,

        'pending': pending,
        'pending1': pending1,
        'pending2': pending2,
        'pending3': pending3,

        'canceled': canceled,
        'canceled1': canceled1,
        'canceled2': canceled2, 
        'canceled3': canceled3,        

        'delivered': delivered,
        'delivered1': delivered1,
        'delivered2': delivered2,
        'delivered3':delivered3,

        'at_the_mall': at_the_mall,
        }

    return render(request, 'users/profile.html', context)

@login_required(login_url='login')
@admin_only
def allE_errand(request):
    request1 = MakeRequest.objects.all()
    request2 = MakeRequestCash.objects.all()
    request3 = Shopping.objects.all()
    request4 = Anonymous.objects.all()
    request5 = Errand_service.objects.all()
    request6= Front_desk.objects.all()

    paginator = Paginator(request5, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    notify = adminNotification.objects.all()
    
    customer = Customer.objects.get( user= request.user )
    customers = Customer.objects.all()

    myFilter5 = AdminFilterUsers(request.GET, queryset = customers)
    customers = myFilter5.qs

    total_request_online = request1.count()
    total_request_cash = request2.count()
    total_request_shopping = request3.count()
    total_request_anonymous = Anonymous.objects.count()
    total_request_front = Front_desk.objects.count()
    total_request_errand = Errand_service.objects.count()

    delivered4 = request5.filter(status='Delivered').count()
    pending4 = request5.filter(status = 'Pending').count()
    cancled4 = request5.filter(status = 'Canceled').count()
    out_for_delivery4 = request5.filter(status = 'Out for delivery').count()

    delivered5 = request6.filter(status = "Delivered").count()
    pending5 = request6.filter(status = "Pending").count()
    on_route5 = request6.filter(status = "On Route for Delivery").count()
    pur_in_process = request6.filter(status = 'Purchase in Process').count()

    delivered = request1.filter(status='Delivered').count()
    pending = request1.filter(status='Pending').count()
    canceled = request1.filter(status='Canceled').count()
    out_for_delivery = request1.filter(status='Out for delivery').count()

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

    notification_filter = adminNotification.objects.all()
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

        'myFilter5':myFilter5, 'notify':notify, 'page_obj':page_obj, 'request1':request1,
        'request2':request2,
        'request3':request3,
        'request4':request4,

        'customer':customer,
        'customers' : customers,

        'total_request_online': total_request_online,
        'total_request_cash':total_request_cash,
        'total_request_shopping':total_request_shopping,
        'total_request_anonymous':total_request_anonymous ,

        
        'out_for_delivery':out_for_delivery,
        'out_for_delivery1':out_for_delivery1,
        'out_for_delivery2':out_for_delivery2,

        'pending': pending,
        'pending1': pending1,
        'pending2': pending2,
        'pending3': pending3,

        'canceled': canceled,
        'canceled1': canceled1,
        'canceled2': canceled2, 
        'canceled3': canceled3,        

        'delivered': delivered,
        'delivered1': delivered1,
        'delivered2': delivered2,
        'delivered3':delivered3,

        'at_the_mall': at_the_mall,
    }
    return render(request, 'users/AdminErrand.html', context)

@login_required(login_url='login')
@admin_only
def allFront_Desk(request):
    request1 = MakeRequest.objects.all()
    request2 = MakeRequestCash.objects.all()
    request3 = Shopping.objects.all()
    request4 = Anonymous.objects.all()
    request5 = Errand_service.objects.all()
    request6= Front_desk.objects.all()

    paginator = Paginator(request6, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    notify = adminNotification.objects.all()
    
    customer = Customer.objects.get( user= request.user )
    customers = Customer.objects.all()

    myFilter5 = AdminFilterUsers(request.GET, queryset = customers)
    customers = myFilter5.qs

    total_request_online = request1.count()
    total_request_cash = request2.count()
    total_request_shopping = request3.count()
    total_request_anonymous = Anonymous.objects.count()
    total_request_front = Front_desk.objects.count()
    total_request_errand = Errand_service.objects.count()

    delivered4 = request5.filter(status='Delivered').count()
    pending4 = request5.filter(status = 'Pending').count()
    cancled4 = request5.filter(status = 'Canceled').count()
    out_for_delivery4 = request5.filter(status = 'Out for delivery').count()

    delivered5 = request6.filter(status = "Delivered").count()
    pending5 = request6.filter(status = "Pending").count()
    on_route5 = request6.filter(status = "On Route for Delivery").count()
    pur_in_process = request6.filter(status = 'Purchase in Process').count()

    delivered = request1.filter(status='Delivered').count()
    pending = request1.filter(status='Pending').count()
    canceled = request1.filter(status='Canceled').count()
    out_for_delivery = request1.filter(status='Out for delivery').count()

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

    notification_filter = adminNotification.objects.all()
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

        'myFilter5':myFilter5, 'notify':notify, 'page_obj':page_obj, 'request1':request1,
        'request2':request2,
        'request3':request3,
        'request4':request4,
        'request5':request5,
        'request6':request6,

        'customer':customer,
        'customers' : customers,

        'total_request_online': total_request_online,
        'total_request_cash':total_request_cash,
        'total_request_shopping':total_request_shopping,
        'total_request_anonymous':total_request_anonymous ,

        
        'out_for_delivery':out_for_delivery,
        'out_for_delivery1':out_for_delivery1,
        'out_for_delivery2':out_for_delivery2,

        'pending': pending,
        'pending1': pending1,
        'pending2': pending2,
        'pending3': pending3,

        'canceled': canceled,
        'canceled1': canceled1,
        'canceled2': canceled2, 
        'canceled3': canceled3,        

        'delivered': delivered,
        'delivered1': delivered1,
        'delivered2': delivered2,
        'delivered3':delivered3,

        'at_the_mall': at_the_mall,
    }
    return render(request, 'users/adminFront.html', context)

@login_required(login_url='login')
@admin_only
def  allAnonymous_Request(request):
    request1 = MakeRequest.objects.all()
    request2 = MakeRequestCash.objects.all()
    request3 = Shopping.objects.all()
    request4 = Anonymous.objects.all()
    request5 = Errand_service.objects.all()
    request6= Front_desk.objects.all()

    paginator = Paginator(request4, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    notify = adminNotification.objects.all()
    
    customer = Customer.objects.get( user= request.user )
    customers = Customer.objects.all()

    myFilter5 = AdminFilterUsers(request.GET, queryset = customers)
    customers = myFilter5.qs

    total_request_online = request1.count()
    total_request_cash = request2.count()
    total_request_shopping = request3.count()
    total_request_anonymous = Anonymous.objects.count()
    total_request_front = Front_desk.objects.count()
    total_request_errand = Errand_service.objects.count()

    delivered4 = request5.filter(status='Delivered').count()
    pending4 = request5.filter(status = 'Pending').count()
    cancled4 = request5.filter(status = 'Canceled').count()
    out_for_delivery4 = request5.filter(status = 'Out for delivery').count()

    delivered5 = request6.filter(status = "Delivered").count()
    pending5 = request6.filter(status = "Pending").count()
    on_route5 = request6.filter(status = "On Route for Delivery").count()
    pur_in_process = request6.filter(status = 'Purchase in Process').count()

    delivered = request1.filter(status='Delivered').count()
    pending = request1.filter(status='Pending').count()
    canceled = request1.filter(status='Canceled').count()
    out_for_delivery = request1.filter(status='Out for delivery').count()

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

    notification_filter = adminNotification.objects.all()
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

        'myFilter5':myFilter5, 'notify':notify, 'page_obj':page_obj, 'request1':request1,
        'request2':request2,
        'request3':request3,
        'request4':request4,
        'request5':request5,
        'request6':request6,

        'customer':customer,
        'customers' : customers,

        'total_request_online': total_request_online,
        'total_request_cash':total_request_cash,
        'total_request_shopping':total_request_shopping,
        'total_request_anonymous':total_request_anonymous ,

        
        'out_for_delivery':out_for_delivery,
        'out_for_delivery1':out_for_delivery1,
        'out_for_delivery2':out_for_delivery2,

        'pending': pending,
        'pending1': pending1,
        'pending2': pending2,
        'pending3': pending3,

        'canceled': canceled,
        'canceled1': canceled1,
        'canceled2': canceled2, 
        'canceled3': canceled3,        

        'delivered': delivered,
        'delivered1': delivered1,
        'delivered2': delivered2,
        'delivered3':delivered3,

        'at_the_mall': at_the_mall,
    }
    return render(request, 'users/allAnonymousRequest.html', context)

@login_required(login_url='login')
@admin_only
def allE_request(request):
    request1 = MakeRequest.objects.all()
    request2 = MakeRequestCash.objects.all()
    request3 = Shopping.objects.all()
    request4 = Anonymous.objects.all()
    request5 = Front_desk.objects.all()
    request6 = Errand_service.objects.all()

    paginator = Paginator(request1, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    notify = adminNotification.objects.all()
    
    customer = Customer.objects.get( user= request.user )
    customers = Customer.objects.all()

    myFilter5 = AdminFilterUsers(request.GET, queryset = customers)
    customers = myFilter5.qs

    total_request_online = request1.count()
    total_request_cash = request2.count()
    total_request_shopping = request3.count()
    total_request_anonymous = Anonymous.objects.count()
    total_request_front = Front_desk.objects.count()
    total_request_errand = Errand_service.objects.count()

    delivered = request1.filter(status='Delivered').count()
    pending = request1.filter(status='Pending').count()
    canceled = request1.filter(status='Canceled').count()
    out_for_delivery = request1.filter(status='Out for delivery').count()

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

    notification_filter = adminNotification.objects.all()
    notify = notification_filter.filter(viewed = False) 

    context = {
        'myFilter5':myFilter5, 'notify':notify, 'page_obj':page_obj, 'request1':request1,
        'request2':request2,
        'request3':request3,
        'request4':request4,

        'delivered4':delivered4,
        'pending4':pending4,
        'cancled4':cancled4,
        'out_for_delivery4':out_for_delivery4,

        'delivered5':delivered5,
        'pending5':pending5,
        'on_route5':on_route5,
        'pur_in_process':pur_in_process,

        'customer':customer,
        'customers' : customers,

        'total_request_online': total_request_online,
        'total_request_cash':total_request_cash,
        'total_request_shopping':total_request_shopping,
        'total_request_anonymous':total_request_anonymous,
        'total_request_front':total_request_front,
        'total_request_errand':total_request_errand,
        
        'out_for_delivery':out_for_delivery,
        'out_for_delivery1':out_for_delivery1,
        'out_for_delivery2':out_for_delivery2,

        'pending': pending,
        'pending1': pending1,
        'pending2': pending2,
        'pending3': pending3,

        'canceled': canceled,
        'canceled1': canceled1,
        'canceled2': canceled2, 
        'canceled3': canceled3,        

        'delivered': delivered,
        'delivered1': delivered1,
        'delivered2': delivered2,
        'delivered3':delivered3,

        'at_the_mall': at_the_mall,
    }
    return render(request, 'users/allEpaymentsRequest.html', context )

@login_required(login_url='login')
@admin_only
def allCash_Request(request):
    request1 = MakeRequest.objects.all()
    request2 = MakeRequestCash.objects.all()
    request3 = Shopping.objects.all()
    request4 = Anonymous.objects.all()
    request5 = Front_desk.objects.all()
    request6 = Errand_service.objects.all()

    paginator2 = Paginator(request2, 10)
    page_number2 = request.GET.get('page')
    page_obj2 = paginator2.get_page(page_number2)

    notify = adminNotification.objects.all()
    
    customer = Customer.objects.get( user= request.user )
    customers = Customer.objects.all()

    myFilter5 = AdminFilterUsers(request.GET, queryset = customers)
    customers = myFilter5.qs

    total_request_online = request1.count()
    total_request_cash = request2.count()
    total_request_shopping = request3.count()
    total_request_anonymous = Anonymous.objects.count()
    total_request_front = Front_desk.objects.count()
    total_request_errand = Errand_service.objects.count()

    delivered = request1.filter(status='Delivered').count()
    pending = request1.filter(status='Pending').count()
    canceled = request1.filter(status='Canceled').count()
    out_for_delivery = request1.filter(status='Out for delivery').count()

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

    notification_filter = adminNotification.objects.all()
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

        'myFilter5':myFilter5, 

        'notify':notify, 

        'page_obj2':page_obj2, 

        'request1':request1,
        'request2':request2,
        'request3':request3,
        'request4':request4,

        'customer':customer,
        'customers' : customers,

        'total_request_online': total_request_online,
        'total_request_cash':total_request_cash,
        'total_request_shopping':total_request_shopping,
        'total_request_anonymous':total_request_anonymous ,

        
        'out_for_delivery':out_for_delivery,
        'out_for_delivery1':out_for_delivery1,
        'out_for_delivery2':out_for_delivery2,

        'pending': pending,
        'pending1': pending1,
        'pending2': pending2,
        'pending3': pending3,

        'canceled': canceled,
        'canceled1': canceled1,
        'canceled2': canceled2, 
        'canceled3': canceled3,        

        'delivered': delivered,
        'delivered1': delivered1,
        'delivered2': delivered2,
        'delivered3':delivered3,

        'at_the_mall': at_the_mall,
    }
    return render(request, 'users/allCashRequest.html', context )

def allShopping_Request(request):
    request1 = MakeRequest.objects.all()
    request2 = MakeRequestCash.objects.all()
    request3 = Shopping.objects.all()
    request4 = Anonymous.objects.all()
    request5 = Front_desk.objects.all()
    request6 = Errand_service.objects.all()

    paginator3 = Paginator(request3, 10)
    page_number3 = request.GET.get('page')
    page_obj3 = paginator3.get_page(page_number3)

    notify = adminNotification.objects.all()
    
    customer = Customer.objects.get( user= request.user )
    customers = Customer.objects.all()

    myFilter5 = AdminFilterUsers(request.GET, queryset = customers)
    customers = myFilter5.qs

    total_request_online = request1.count()
    total_request_cash = request2.count()
    total_request_shopping = request3.count()
    total_request_anonymous = Anonymous.objects.count()
    total_request_front = Front_desk.objects.count()
    total_request_errand = Errand_service.objects.count()

    delivered = request1.filter(status='Delivered').count()
    pending = request1.filter(status='Pending').count()
    canceled = request1.filter(status='Canceled').count()
    out_for_delivery = request1.filter(status='Out for delivery').count()

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

    notification_filter = adminNotification.objects.all()
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

        'myFilter5':myFilter5, 
        
        'notify':notify, 

        'page_obj3':page_obj3, 

        'request1':request1,
        'request2':request2,
        'request3':request3,
        'request4':request4,

        'customer':customer,
        'customers' : customers,

        'total_request_online': total_request_online,
        'total_request_cash':total_request_cash,
        'total_request_shopping':total_request_shopping,
        'total_request_anonymous':total_request_anonymous ,

        
        'out_for_delivery':out_for_delivery,
        'out_for_delivery1':out_for_delivery1,
        'out_for_delivery2':out_for_delivery2,

        'pending': pending,
        'pending1': pending1,
        'pending2': pending2,
        'pending3': pending3,

        'canceled': canceled,
        'canceled1': canceled1,
        'canceled2': canceled2, 
        'canceled3': canceled3,        

        'delivered': delivered,
        'delivered1': delivered1,
        'delivered2': delivered2,
        'delivered3':delivered3,

        'at_the_mall': at_the_mall,
    }
    return render(request, 'users/allShoppingRequest.html', context )

#General Order
@login_required(login_url='login')
@admin_only
def customers_list(request):
    request1 = MakeRequest.objects.all()
    request2 = MakeRequestCash.objects.all()
    request3 = Shopping.objects.all()
    request4 = Anonymous.objects.all()

    myFilter2 = AdminFilter(request.GET, queryset = request1)
    request1 = myFilter2.qs

    myFilter3 = AdminFilter(request.GET, queryset = request2)
    request2 = myFilter3.qs

    myFilter4 = AdminFilter(request.GET, queryset = request3)
    request3 = myFilter4.qs

    myFilter5 = AdminFilter(request.GET, queryset = request4)
    request4 = myFilter5.qs

    context = {

        'myFilter2':myFilter2,
        'request1': request1, 'request2':request2,
        'request3':request3, 'request4':request4,
    }
    return render(request, 'users/customer_list.html', context)

#Customer Dashboard
@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'customer', 'Fleet Manager', 'Front Desk', 'Cashier'])
def customerDashboardPage(request, user):
    customer = Customer.objects.get( user= user )
    request_filter = customer.makerequest_set.all()
    request_filter_cash = customer.makerequestcash_set.all()
    request_filter_errand = customer.errand_service_set.all()
    request_filter_shopping = customer.shopping_set.all()

    n_filter = customer.delivered_set.all()
    n = n_filter.filter(viewed = False)

    context = {
        'request_filter_cash':request_filter_cash,
        'request_filter':request_filter,
        'request_filter_errand':request_filter_errand,
        'request_filter_shopping':request_filter_shopping,
        'customer':customer,
        'n':n
    }
    return render(request, 'users/customerDashboard.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'Cashier'])
def CashierUpdateE_RequestForm(request, pk):
    r_request = MakeRequest.objects.get(id=pk)  
    customer = Customer.objects.get(user=request.user) 
    Ca_form = CashierFormE(request.POST,instance=r_request)

    if request.method == 'POST':
        Ca_form = CashierFormE(request.POST,instance=r_request)
        if Ca_form.is_valid():
            obj = Ca_form.save(commit=False)
            obj.save()
            messages.success(request, f'Successful')

            return redirect('cashier', user = pk)
    context = {'Ca_form': Ca_form,
              'customer':customer 
              }
    return render(request, 'users/CashierUpdateE.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'Cashier'])
def CashierUpdateCash_RequestForm(request, pk):
    r_request = MakeRequestCash.objects.get(id=pk)  
    customer = Customer.objects.get(user=request.user) 
    Ca_form = CashierFormE(request.POST,instance=r_request)

    if request.method == 'POST':
        Ca_form = CashierFormE(request.POST,instance=r_request)
        if Ca_form.is_valid():
            obj = Ca_form.save(commit=False)
            obj.save()
            messages.success(request, f'Successful')

            return redirect('cashier', user = pk)
    context = {'Ca_form': Ca_form,
              'customer':customer 
              }
    return render(request, 'users/CashierUpdateC.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'Cashier'])
def CashierUpdateShoppingForm(request, pk):
    r_request = Shopping.objects.get(id=pk)  
    customer = Customer.objects.get(user=request.user) 
    Ca_form = CashierFormShopping(request.POST,instance=r_request)

    if request.method == 'POST':
        Ca_form = CashierFormShopping(request.POST,instance=r_request)
        if Ca_form.is_valid():
            obj = Ca_form.save(commit=False)
            obj.save()
            messages.success(request, f'Successful')

            return redirect('cashier', user=pk)
    context = {'Ca_form': Ca_form,
              'customer':customer 
              }
    return render(request, 'users/CashierUpdateS.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'Cashier'])
def CashierUpdateAnonForm(request, pk):
    r_request = Anonymous.objects.get(id=pk)  
    customer = Customer.objects.get(user=request.user) 
    Ca_form = CashierFormErrand(request.POST,instance=r_request)

    if request.method == 'POST':
        Ca_form = CashierFormErrand(request.POST,instance=r_request)
        if Ca_form.is_valid():
            obj = Ca_form.save(commit=False)
            obj.save()
            messages.success(request, f'Successful')

            return redirect('cashier', user=pk)
    context = {'Ca_form': Ca_form,
              'customer':customer 
              }
    return render(request, 'users/CashierUpdateA.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'Cashier'])
def CashierUpdateErrandForm(request, pk):
    r_request = Errand_service.objects.get(id=pk)  
    customer = Customer.objects.get(user=request.user) 
    Ca_form = CashierFormErrand(request.POST,instance=r_request)

    if request.method == 'POST':
        Ca_form = CashierFormErrand(request.POST,instance=r_request)
        if Ca_form.is_valid():
            obj = Ca_form.save(commit=False)
            obj.save()
            messages.success(request, f'Successful')

            return redirect('cashier', user=pk)
    context = {'Ca_form': Ca_form,
              'customer':customer 
              }
    return render(request, 'users/CashierUpdateErr.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'Cashier'])
def CashierUpdateFrontForm(request, pk):
    r_request = Front_desk.objects.get(id=pk)  
    customer = Customer.objects.get(user=request.user) 
    Ca_form = CashierFormFront(request.POST,instance=r_request)

    if request.method == 'POST':
        Ca_form = CashierFormFront(request.POST,instance=r_request)
        if Ca_form.is_valid():
            obj = Ca_form.save(commit=False)
            obj.save()
            messages.success(request, f'Successful')

            return redirect('cashier', user = pk)
    context = {'Ca_form': Ca_form,
              'customer':customer 
              }
    return render(request, 'users/CashierUpdatefront.html', context)

#Fleet Manager Update E
@login_required(login_url='login')
@allowed_user(allowed_roles=['admin','Fleet_Manager'])
def UpdateEForm(request, pk):
    r_request = MakeRequest.objects.get(id=pk)
    o_form = FleetManagerUpdateE(instance= r_request)
    customer = Customer.objects.get(user=request.user) 
    rider = RidersDeliveries.objects.all()
    riders_profile = RidersProfile.objects.all()

    if request.method == 'POST':
        o_form = FleetManagerUpdateE(request.POST,instance=r_request)
        if o_form.is_valid():
            obj = o_form.save(commit=False)
            obj.save()

            if obj.status == 'Delivered':
                rider.filter(e_payment_request = obj).update(staus = 'Delivered')
                try:
                    all4 = rider.filter(e_payment_request = obj).get(rider__in = riders_profile)
                    at = all4.rider     
                    all3 = RidersDeliveries.objects.filter(rider = at).filter(staus = 'Pending').exists()                                          
                    if all3 == True:
                        pass                
                    elif all3 == False:
                        riders_profile.filter(pk = all4.rider.pk).update(busy = False)
                except RidersDeliveries.DoesNotExist:
                    raise Http404(f'Hello {request.user.username} You havent assigned this order to a rider please do so.')
           
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

            return redirect('fleetManager', user = pk)
    context = {'o_form': o_form,
              'customer':customer 
              }
    return render(request, 'users/FleetManagerUpdateE.html', context)

#Fleet Manager Update C
@login_required(login_url='login')
@allowed_user(allowed_roles=['admin','Fleet_Manager'])
def UpdateCForm(request, pk):
    r_request = MakeRequestCash.objects.get(id=pk)
    o_form = FleetManagerUpdateC(instance= r_request)
    customer = Customer.objects.get(user=request.user)
    rider = RidersDeliveries.objects.all()
    riders_profile = RidersProfile.objects.all()

    if request.method == 'POST':
        o_form = FleetManagerUpdateC(request.POST,instance=r_request)
        if o_form.is_valid():
            obj = o_form.save(commit=False)
            obj.save()

            if obj.status == 'Delivered':
                rider.filter(cash_request = obj).update(staus = 'Delivered')
                try:
                    all4 = rider.filter(cash_request = obj).get(rider__in = riders_profile)
                    at = all4.rider     
                    all3 = RidersDeliveries.objects.filter(rider = at).filter(staus = 'Pending').exists()                                          
                    if all3 == True:
                        pass                
                    elif all3 == False:
                        riders_profile.filter(pk = all4.rider.pk).update(busy = False)
                except RidersDeliveries.DoesNotExist:
                    raise Http404(f'Hello {request.user.username} You havent assigned this order to a rider please do so.')
           
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

            return redirect('fleetManager', user = pk)
    context = {'o_form': o_form,
              'customer':customer 
              }
    return render(request, 'users/FleetManagerUpdateC.html', context)

#Fleet Manager Update S
@login_required(login_url='login')
@allowed_user(allowed_roles=['admin','Fleet_Manager'])
def UpdateSForm(request, pk):
    r_request = Shopping.objects.get(id=pk)
    o_form = FleetManagerUpdateS(instance= r_request)
    customer = Customer.objects.get(user=request.user)
    rider = RidersDeliveries.objects.all()
    riders_profile = RidersProfile.objects.all()

    if request.method == 'POST':
        o_form = FleetManagerUpdateS(request.POST,instance=r_request)
        if o_form.is_valid():
            obj = o_form.save(commit=False)
            obj.save()
           
            if obj.status == 'Delivered':
                rider.filter(shopping = obj).update(staus = 'Delivered')
                try:
                    all4 = rider.filter(shopping = obj).get(rider__in = riders_profile)
                    at = all4.rider     
                    all3 = RidersDeliveries.objects.filter(rider = at).filter(staus = 'Pending').exists()                                          
                    if all3 == True:
                        pass                
                    elif all3 == False:
                        riders_profile.filter(pk = all4.rider.pk).update(busy = False)
                except RidersDeliveries.DoesNotExist:
                    raise Http404(f'Hello {request.user.username} You havent assigned this order to a rider please do so.')

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

            return redirect('fleetManager', user = pk)
    context = {'o_form': o_form,
              'customer':customer 
              }
    return render(request, 'users/FleetManagerUpdateS.html', context)

#Fleet Manager Update Errand Service
@login_required(login_url='login')
@allowed_user(allowed_roles=['admin','Fleet_Manager'])
def UpdateErrForm(request, pk):
    r_request = Errand_service.objects.get(id=pk)
    o_form = FleetManagerUpdateErr(instance= r_request)
    customer = Customer.objects.get(user=request.user) 
    rider = RidersDeliveries.objects.all()
    riders_profile = RidersProfile.objects.all()

    if request.method == 'POST':
        o_form = FleetManagerUpdateErr(request.POST,instance=r_request)
        if o_form.is_valid():
            obj = o_form.save(commit=False)
            obj.save()
           
            if obj.status == 'Delivered':
                rider.filter(errand = obj).update(staus = 'Delivered')                
                try:
                    all4 = rider.filter(errand = obj).get(rider__in = riders_profile)
                    at = all4.rider     
                    all3 = RidersDeliveries.objects.filter(rider = at).filter(staus = 'Pending').exists()                                          
                    if all3 == True:
                        pass                
                    elif all3 == False:
                        riders_profile.filter(pk = all4.rider.pk).update(busy = False)
                except RidersDeliveries.DoesNotExist:
                    raise Http404(f'Hello {request.user.username} You havent assigned this order to a rider please do so.')
                        
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

            return redirect('fleetManager', user = pk)
    context = {'o_form': o_form,
              'customer':customer 
              }
    return render(request, 'users/FleetManagerUpdateErr.html', context)

#Fleet Manager Update Anon
@login_required(login_url='login')
@allowed_user(allowed_roles=['admin','Fleet_Manager'])
def UpdateAForm(request, pk):
    r_request = Anonymous.objects.get(id=pk)
    o_form = FleetManagerUpdateA(instance= r_request)
    customer = Customer.objects.get(user=request.user) 
    rider = RidersDeliveries.objects.all()
    riders_profile = RidersProfile.objects.all()

    if request.method == 'POST':
        o_form = FleetManagerUpdateA(request.POST,instance=r_request)
        if o_form.is_valid():
            obj = o_form.save(commit=False)
            obj.save()
            
            if obj.status == 'Delivered':
                rider.filter(anonymous = obj).update(staus = 'Delivered')
                try:
                    all4 = rider.filter(anonymous = obj).get(rider__in = riders_profile)
                    at = all4.rider     
                    all3 = RidersDeliveries.objects.filter(rider = at).filter(staus = 'Pending').exists()                                          
                    if all3 == True:
                        pass                
                    elif all3 == False:
                        riders_profile.filter(pk = all4.rider.pk).update(busy = False)
                except RidersDeliveries.DoesNotExist:
                    raise Http404(f'Hello {request.user.username} You havent assigned this order to a rider please do so.')
            messages.success(request, f'You just updated a customer satus to delivered {obj.order_id}')

            return redirect('fleetManager', user = pk)
    context = {'o_form': o_form,
              'customer':customer 
              }
    return render(request, 'users/FleetManagerUpdateAnon.html', context)

#Fleet Manager Update Front Desk form
@login_required(login_url='login')
@allowed_user(allowed_roles=['admin','Fleet_Manager'])
def UpdateFForm(request, pk):
    r_request = Front_desk.objects.get(id=pk)
    o_form = FleetManagerUpdateF(instance= r_request)
    customer = Customer.objects.get(user=request.user) 
    rider = RidersDeliveries.objects.all()
    riders_profile = RidersProfile.objects.all()

    if request.method == 'POST':
        o_form = FleetManagerUpdateF(request.POST,instance=r_request)
        if o_form.is_valid():
            obj = o_form.save(commit=False)
            obj.save()
            
            if obj.status == 'Delivered':
                rider.filter(front_desk = obj).update(staus = 'Delivered')
                try:
                    all4 = rider.filter(front_desk = obj).get(rider__in = riders_profile)
                    at = all4.rider     
                    all3 = RidersDeliveries.objects.filter(rider = at).filter(staus = 'Pending').exists()                                          
                    if all3 == True:
                        pass                
                    elif all3 == False:
                        riders_profile.filter(pk = all4.rider.pk).update(busy = False)
                except RidersDeliveries.DoesNotExist:
                    raise Http404(f'Hello {request.user.username} You havent assigned this order to a rider please do so.')
           
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

            return redirect('fleetManager', user = pk)
    context = {'o_form': o_form,
              'customer':customer 
              }
    return render(request, 'users/FleetManagerUpdateF.html', context)
#adminUpdateErrand
@login_required(login_url='login')
@allowed_user(allowed_roles=['admin','Fleet_Manager'])
def Update_Errand_Form(request, pk):
    r_request =Errand_service.objects.get(id=pk)
    o_form = AdminErrandForm(instance= r_request)
    customer = Customer.objects.get(user=request.user)  
    rider = RidersDeliveries.objects.all()  
    riders_profile = RidersProfile.objects.all()

    if request.method == 'POST':
        o_form = AdminErrandForm(request.POST,instance=r_request)
        if o_form.is_valid():
            obj = o_form.save(commit=False)
            obj.save()            

            if obj.status == 'Delivered':
                rider.filter(errand = obj).update(staus = 'Delivered')
                try:
                    all4 = rider.filter(errand = obj).get(rider__in = riders_profile)
                    at = all4.rider     
                    all3 = RidersDeliveries.objects.filter(rider = at).filter(staus = 'Pending').exists()                                          
                    if all3 == True:
                        pass                
                    elif all3 == False:
                        riders_profile.filter(pk = all4.rider.pk).update(busy = False)
                except RidersDeliveries.DoesNotExist:
                    raise Http404(f'Hello {request.user.username} You havent assigned this order to a rider please do so.')

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
    r_request = Front_desk.objects.get(id=pk)
    o_form = AdminFrontForm(instance= r_request)
    customer = Customer.objects.get(user = request.user) 
    rider = RidersDeliveries.objects.all()
    riders_profile = RidersProfile.objects.all()

    if request.method == 'POST':
        o_form = AdminFrontForm(request.POST, instance=r_request)
        if o_form.is_valid():
            obj = o_form.save(commit=False)
            obj.save()

            if obj.status == 'Delivered':
                rider.filter(front_desk = obj).update(staus = 'Delivered')
                try:
                    all4 = rider.filter(front_desk = obj).get(rider__in = riders_profile)
                    at = all4.rider     
                    all3 = RidersDeliveries.objects.filter(rider = at).filter(staus = 'Pending').exists()                                          
                    if all3 == True:
                        pass                
                    elif all3 == False:
                        riders_profile.filter(pk = all4.rider.pk).update(busy = False)
                except RidersDeliveries.DoesNotExist:
                    raise Http404(f'Hello {request.user.username} You havent assigned this order to a rider please do so.')

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
    rider = RidersDeliveries.objects.all()
    riders_profile = RidersProfile.objects.all()

    if request.method == 'POST':
        a_form = AdminAnonForm(request.POST,instance=r_request)
        if a_form.is_valid():
            instance = a_form.save(commit=False)
            instance.save()

            if instance.status == 'Delivered':
                rider.filter(anonymous = instance).update(staus = 'Delivered')
                try:
                    all4 = rider.filter(anonymous = instance).get(rider__in = riders_profile)
                    at = all4.rider     
                    all3 = RidersDeliveries.objects.filter(rider = at).filter(staus = 'Pending').exists()                                          
                    if all3 == True:
                        pass                
                    elif all3 == False:
                        riders_profile.filter(pk = all4.rider.pk).update(busy = False)
                except RidersDeliveries.DoesNotExist:
                    raise Http404(f'Hello {request.user.username} You havent assigned this order to a rider please do so.')

            messages.success(request, f'Successful:{instance.order_id}')

            return redirect('anonymous-request')
    context = {'a_form': a_form}
    return render(request, 'users/anonform.html', context)

#Delete Request Anon
@login_required(login_url='login')
@admin_only
def cancelRequestErrand(request, pk):
    r_request2 =Errand_service.objects.get(id=pk)
    customer = Customer.objects.get(user = request.user) 
    if request.method == "POST":
        r_request2.delete()  
        messages.success(request, f'You just deleted an order: {r_request2.order_id}')
        return redirect('allerrand-request')
    context = {
        'item3':r_request2,
        'customer':customer,
    }
    return render(request, 'users/deleteErrand.html', context)

#cancelRequestFront
@login_required(login_url='login')
@admin_only
def cancelRequestFront(request, pk):
    r_request2 =Front_desk.objects.get(id=pk)
    customer = Customer.objects.get(user = request.user) 
    if request.method == "POST":
        r_request2.delete()  
        messages.success(request, f'You just deleted an order: {r_request2.order_id}')
        return redirect('allfront-request')
    context = {
        'item3':r_request2,
        'customer':customer,
    }
    return render(request, 'users/deleteFront.html', context)

#Delete Request Anon
@login_required(login_url='login')
@admin_only
def cancelRequestAnon(request, pk):
    r_request2 =Anonymous.objects.get(id=pk)
    if request.method == "POST":
        r_request2.delete()  
        messages.success(request, f'You just deleted an order: {r_request2.order_id}')
        return redirect('anonymous-request')
    context = {
        'item3':r_request2
    }
    return render(request, 'users/deleteAnon.html', context)


#Update Request 
@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def updateRequestForm(request, pk):
    r_request = MakeRequest.objects.get(id=pk)
    o_form = adminform(instance= r_request)    
    customer = Customer.objects.get(user=request.user) 
    rider = RidersDeliveries.objects.all()
    riders_profile = RidersProfile.objects.all()

    if request.method == 'POST':
        o_form = adminform(request.POST,instance=r_request)
        if o_form.is_valid():
            obj = o_form.save(commit=False)        
            obj.save()     

            if obj.status == 'Delivered':
                rider.filter(e_payemnt_request = obj).update(staus = 'Delivered')
                try:
                    all4 = rider.filter(e_payment_request = obj).get(rider__in = riders_profile)
                    at = all4.rider     
                    all3 = RidersDeliveries.objects.filter(rider = at).filter(staus = 'Pending').exists()                                          
                    if all3 == True:
                        pass                
                    elif all3 == False:
                        riders_profile.filter(pk = all4.rider.pk).update(busy = False)
                except RidersDeliveries.DoesNotExist:
                    raise Http404(f'Hello {request.user.username} You havent assigned this order to a rider please do so.')

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

            return redirect('e-request')
    context = {'o_form': o_form,
              'customer':customer 
              }
    return render(request, 'users/adminUpdateCard.html', context)

#Update Request Cash
@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def updateRequestFormCash(request, pk):
    r_request1 = MakeRequestCash.objects.get(id=pk)
    c_form = adminformCash(instance= r_request1)
    customer = Customer.objects.get(user=request.user) 
    rider = RidersDeliveries.objects.all()
    riders_profile = RidersProfile.objects.all()

    if request.method == 'POST':
        c_form = adminformCash(request.POST,instance = r_request1)
        if c_form.is_valid():
            obj = c_form.save(commit=False)            
            obj.save()

            if obj.status == 'Delivered':
                rider.filter(cash_request = obj).update(staus = 'Delivered')
                try:
                    all4 = rider.filter(cash_request = obj).get(rider__in = riders_profile)
                    at = all4.rider     
                    all3 = RidersDeliveries.objects.filter(rider = at).filter(staus = 'Pending').exists()                                          
                    if all3 == True:
                        pass                
                    elif all3 == False:
                        riders_profile.filter(pk = all4.rider.pk).update(busy = False)
                except RidersDeliveries.DoesNotExist:
                    raise Http404(f'Hello {request.user.username} You havent assigned this order to a rider please do so.')

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

            return redirect('cash-request')
    context = {'c_form': c_form,
            'customer':customer
             }
    return render(request, 'users/adminUpdateCash.html', context)


#Update Request Shopping
@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def updateRequestFormShopping(request, pk):
    r_request2 = Shopping.objects.get(id=pk)
    s_form = adminformShopping(instance= r_request2)
    customer = Customer.objects.get(user=request.user) 
    rider = RidersDeliveries.objects.all()
    riders_profile = RidersProfile.objects.all()

    if request.method == 'POST':
        s_form = adminformShopping(request.POST,instance = r_request2)
        if s_form.is_valid():
            obj = s_form.save(commit=False)            
            obj.save()

            if obj.status == 'Delivered':
                rider.filter(shoppng = obj).update(staus = 'Delivered')
                try:
                    all4 = rider.filter(shopping = obj).get(rider__in = riders_profile)
                    at = all4.rider     
                    all3 = RidersDeliveries.objects.filter(rider = at).filter(staus = 'Pending').exists()                                          
                    if all3 == True:
                        pass                
                    elif all3 == False:
                        riders_profile.filter(pk = all4.rider.pk).update(busy = False)
                except RidersDeliveries.DoesNotExist:
                    raise Http404(f'Hello {request.user.username} You havent assigned this order to a rider please do so.')

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

            return redirect('shopping-request')
    context = {'s_form': s_form,
              'customer':customer }
    return render(request, 'users/adminUpdateShop.html', context)


#Delete Request
@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def deleteRequestForm(request, pk):

    r_request = MakeRequest.objects.get(id=pk)
    o_form = OrderForm(instance= r_request) 

    if request.method == 'POST':
        o_form = OrderForm(request.POST,instance=r_request)
        if o_form.is_valid():
            obj = o_form.save(commit=False)            
            obj.save()
            messages.success(f'You just deleted {obj.customer} order')
            return redirect('e-request')
            
    context = {'o_form': o_form}
    return render(request, 'users/requestForm.html', context)

@login_required(login_url='login')
@admin_only
def cancelRequest(request, pk):
    r_request = MakeRequest.objects.get(id=pk)
    if request.method == "POST":
        r_request.delete()
        messages.success(request, f'You just deleted an order')
        return redirect('adminDashboard')
    context = {'item':r_request}
    return render(request, 'users/delete.html', context)

#Delete Request Cash
@login_required(login_url='login')
@admin_only
def cancelRequestCash(request, pk):
    r_request2 = MakeRequestCash.objects.get(id=pk)
    if request.method == "POST":
        r_request2.delete()
        messages.success(request, f'You just deleted an order')
        return redirect('cash-request')
    context = {
        'item2':r_request2
    }
    return render(request, 'users/deleteCash.html', context)

#delete request Shopping
@login_required(login_url='login')
@admin_only
def cancelRequestShopping(request, pk):
    r_request3 = Shopping.objects.get(id=pk)
    if request.method == "POST":
        r_request3.delete()
        messages.success(request, f'You just deleted an order')
        return redirect('shopping-request')
    context = {
        'item3':r_request3
    }
    return render(request, 'users/deleteShopping.html', context)

#Delete Request Order History
@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'customer', 'Fleet Manager', 'Front Desk', 'Cashier'])
def orderHistory(request, user):
    customer = Customer.objects.get( user=user )

    request1 = customer.makerequest_set.all()
    request2 = customer.makerequestcash_set.all()
    shop_request = customer.shopping_set.all()
    errand_request = customer.errand_service_set.all()

    request_count = request1.count()
    request2_count = request2.count()
    shop_request_count = shop_request.count()

    myFilter = OrderFilter(request.GET, queryset=request1)
    request1 = myFilter.qs
    myFilter3 = OrderFilter(request.GET, queryset=request2)
    request2 = myFilter3.qs
    myFilter4 = OrderFilter(request.GET, queryset=shop_request)
    shop_request = myFilter4.qs
    myFilter5 = OrderFilter(request.GET, queryset=errand_request)
    errand_request = myFilter5.qs

    myFilter2 = OrderFilter(request.GET, queryset=request2)
    request2 = myFilter2.qs

    n_filter = customer.delivered_set.all()
    n = n_filter.filter(viewed = False)

    context = {
        'n':n,
        'errand_request':errand_request,
        'shop_request_count':shop_request_count,
        'shop_request': shop_request,
        'myFilter2':myFilter2,
        'request2':request2,
        'request1':request1,
        'request_count':request_count,
        'request2_count':request2_count,
        'myFilter':myFilter,
        'customer':customer,
    }
    return render(request, 'users/orderHistory.html', context)

#Customer Notification
@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'customer', 'Fleet Manager', 'Front Desk', 'Cashier'])
def Notifications_show(request, user): 
    customer = Customer.objects.get(user= user)
    n_filter = customer.delivered_set.all()
    n = n_filter.filter(viewed = False)
    return render(request, 'users/notification.html', {'n':n, 'customer':customer})

#Mark As Read
@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'customer', 'Fleet Manager', 'Front Desk', 'Cashier'])
def Notifications_delete(request, pk):    
    cust = Delivered.objects.get(id = pk)
    cust.viewed = True
    cust.save()
    return redirect('show_Notification', user=request.user.id)

#Admin Notification
@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'Fleet Manager', 'Front Desk', 'Cashier'])
def adminNotificationShow(request):
    customer = Customer.objects.get(user=request.user)
    notification_filter = adminNotification.objects.all()
    notify = notification_filter.filter(viewed = False)
    return render(request, 'users/adminNotification.html', {'notify':notify, 'customer':customer})


#Admin Notification Delete
@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'Fleet Manager'])
def adminNotificationDelete(request, pk): 
    cust1 = adminNotification.objects.get(id=pk)
    cust1.viewed = True
    cust1.save()
    return redirect('adminNotificationShow')

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'customer', 'Fleet Manager', 'Front Desk', 'Cashier'])
def ErrandMenu(request, user):
    customer = Customer.objects.get(user=request.user)
    n_filter = customer.delivered_set.all()
    n = n_filter.filter(viewed = False)

    return render(request, 'users/ErrandService.html', {'n':n})

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'customer', 'Fleet Manager', 'Front Desk', 'Cashier'])
def fuel_errand(request, user):
    customer = Customer.objects.get(user = request.user)
    n_filter = customer.delivered_set.all()
    n = n_filter.filter(viewed = False)
    if request.method == 'POST':
        fuel_form = Fuel_errand(request.POST)
        if fuel_form.is_valid():
            instance = fuel_form.save(commit=False)
            instance.customer = customer
            instance.category = 'Fuel'
            instance.save()
        
            hashids = Hashids(salt = settings.ERRAND, min_length=7)
            h = hashids.encode(instance.id)
            customer.errand_service_set.filter(pk = instance.id).update(order_id = h)
            messages.success(request, f'Your Fuel Errand request has been recieved')
            
            adminNotification.objects.create(
                customer = instance.customer,
                item_created = instance,
                order_id = h
            )

            summing_amt_payable = instance.fuel_per_amount + 500
            customer.errand_service_set.filter(pk = instance.id).update(Amount_Payable = summing_amt_payable)

            #initalize payment
            chk_payment_type = customer.errand_service_set.get(pk = instance.id)
            chk_card = chk_payment_type.payment_channel
            print(chk_card)
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
                        "Authorization": settings.PAYSTACK_SECRETKEY,
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
        fuel_form = Fuel_errand(instance = customer) 

    context = {
        'fuel_form':fuel_form,
        'customer':customer,
        'n':n
    }
    return render(request, 'users/Fuelerrand.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'customer', 'Fleet Manager', 'Front Desk', 'Cashier'])
def gas_errand(request, user):
    customer = Customer.objects.get(user = request.user)
    n_filter = customer.delivered_set.all()
    n = n_filter.filter(viewed = False)
    if request.method == 'POST':
        gas_form = Gas_errand(request.POST)
        if gas_form.is_valid():
            instance = gas_form.save(commit=False)
            instance.customer = customer
            instance.category = 'Gas'
            instance.save()
        
            hashids = Hashids(salt = settings.ERRAND, min_length=7)
            h = hashids.encode(instance.id)
            customer.errand_service_set.filter(pk = instance.id).update(order_id = h)
            messages.success(request, f'Your Gas Errand request has been recieved')
            
            adminNotification.objects.create(
                customer = instance.customer,
                item_created = instance,
                order_id = h
            )

            summing_amt_payable = instance.Gas_Quantity * 460 + 500
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
                        "Authorization": settings.PAYSTACK_SECRETKEY,
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
        gas_form = Gas_errand(instance = customer) 

    context = {
        'gas_form':gas_form,
        'customer':customer,
        'n':n
    }
    return render(request, 'users/Gaserrand.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'customer', 'Fleet Manager', 'Front Desk', 'Cashier'])            
def drugs_errand(request, user):
    customer = Customer.objects.get(user = request.user)
    n_filter = customer.delivered_set.all()
    n = n_filter.filter(viewed = False)
    if request.method == 'POST':
        drugs_form = Drugs_errand(request.POST, request.FILES)
        if drugs_form.is_valid():
            instance = drugs_form.save(commit=False)
            instance.customer = customer
            instance.category = 'Drugs'
            instance.save()
        
            hashids = Hashids(salt = settings.ERRAND, min_length=7)
            h = hashids.encode(instance.id)
            customer.errand_service_set.filter(pk = instance.id).update(order_id = h)
            messages.success(request, f'Your Drugs Errand request has been recieved')
            
            adminNotification.objects.create(
                customer = instance.customer,
                item_created = instance,
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
                        "Authorization": settings.PAYSTACK_SECRETKEY,
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
        drugs_form = Drugs_errand(instance = customer) 

    context = {
        'drugs_form':drugs_form,
        'customer':customer,
        'n':n
    }
    return render(request, 'users/Drugserrand.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'customer', 'Fleet Manager', 'Front Desk', 'Cashier'])
def bread_errand(request, user):
    customer = Customer.objects.get(user = request.user)
    n_filter = customer.delivered_set.all()
    n = n_filter.filter(viewed = False)
    if request.method == 'POST':
        bread_form = Bread_errand(request.POST)
        if bread_form.is_valid():
            instance = bread_form.save(commit=False)
            instance.customer = customer
            instance.category = 'Bread'
            instance.save()
        
            hashids = Hashids(salt = settings.ERRAND, min_length=7)
            h = hashids.encode(instance.id)
            customer.errand_service_set.filter(pk = instance.id).update(order_id = h)
            messages.success(request, f'Your Bread Errand request has been recieved')
            
            adminNotification.objects.create(
                customer = instance.customer,
                item_created = instance,
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
                        "Authorization": settings.PAYSTACK_SECRETKEY,
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
        bread_form = Bread_errand(instance=customer) 

    context = {
        'bread_form':bread_form,
        'customer':customer,
        'n':n
    }
    return render(request, 'users/Breaderrand.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'customer', 'Fleet Manager', 'Front Desk', 'Cashier'])
def shawarma_errand(request, user):
    customer = Customer.objects.get(user = request.user)
    n_filter = customer.delivered_set.all()
    n = n_filter.filter(viewed = False)
    if request.method == 'POST':
        shawarma_form = Shawarma_errand(request.POST)
        if shawarma_form.is_valid():
            instance = shawarma_form.save(commit=False)
            instance.customer = customer
            instance.category = 'Shawarma'
            instance.save()
        
            hashids = Hashids(salt = settings.ERRAND, min_length=7)
            h = hashids.encode(instance.id)
            customer.errand_service_set.filter(pk = instance.id).update(order_id = h)
            messages.success(request, f'Your Shawarma Errand request has been recieved')
            
            adminNotification.objects.create(
                customer = instance.customer,
                item_created = instance,
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
                        "Authorization": settings.PAYSTACK_SECRETKEY,
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
        shawarma_form = Shawarma_errand(instance = customer) 

    context = {
        'shawarma_form':shawarma_form,
        'customer':customer,
        'n':n
    }
    return render(request, 'users/Shawarmaerrand.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'customer', 'Fleet Manager', 'Front Desk', 'Cashier'])
def pizza_errand(request, user):
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
            
            adminNotification.objects.create(
                customer = instance.customer,
                item_created = instance,
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
                        "Authorization": settings.PAYSTACK_SECRETKEY,
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
            
            adminNotification.objects.create(
                customer = instance.customer,
                item_created = instance,
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
                        "Authorization": settings.PAYSTACK_SECRETKEY,
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
            
            adminNotification.objects.create(
                customer = instance.customer,
                item_created = instance,
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
                        "Authorization": settings.PAYSTACK_SECRETKEY,
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
            
            adminNotification.objects.create(
                customer = instance.customer,
                item_created = instance,
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
                        "Authorization": settings.PAYSTACK_SECRETKEY,
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
            
            adminNotification.objects.create(
                customer = instance.customer,
                item_created = instance,
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
                        "Authorization": settings.PAYSTACK_SECRETKEY,
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

