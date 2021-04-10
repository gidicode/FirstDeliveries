from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.urls import reverse
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from django.contrib import messages #flash message
from .forms import *
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import *
from .filters import OrderFilter
from .decorators import unauthenticated_user, allowed_user, admin_only
import requests
import json

# Create your views here.

@unauthenticated_user
def register(request):

    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.customer.first_name = form.cleaned_data.get('first_name')
            user.customer.last_name = form.cleaned_data.get('last_name')
            user.customer.phone_number = form.cleaned_data.get('phone_number')
            user.customer.State = form.cleaned_data.get('State')
            user.customer.email = form.cleaned_data.get('email')
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            user.save()
            username = form.cleaned_data.get( 'username')
            messages.success(request, f' Hello {username} Your account hasbeen created! You are now able to log in !')
            login(request, user)
            return redirect('login')
    else:
        form = UserRegisterForm() #EMPTYFORM
    return render(request, 'users/signUp.html', {'form':form})


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'customer'])
def customerProfileUpdatePage(request, user):
    customer = Customer.objects.get(user=request.user)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=customer)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.username)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Profile has been Updated!')
            return redirect('dashboard')
    else:
        u_form = UserUpdateForm(instance=customer)
        p_form = ProfileUpdateForm(instance=customer)
    context = {
        'customer':customer,
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/customer_profile.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'customer'])
def requestForm_Cash(request, user):
    customer = Customer.objects.get(user=request.user)
    if request.method == 'POST':
        c_form = Request_Cash(request.POST)
        if c_form.is_valid():
            instance = c_form.save(commit=False)
            instance.customer = customer
            instance.save()
            messages.success(request, f'Your Request for pickup is Successful, you will recieve a call from us shortly')
            messages.success(request, f'Your Fee is NGN 500')
            ForPayments.objects.create(
                customer = customer,
                For_cash_payment = instance
            )
            return redirect('dashboard', user=user)
    else:
        c_form = Request_Cash(instance=customer)
            
    context = {'c_form': c_form,}
    return render(request, 'users/requestForm_Cash.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'customer'])
def requestForm_Online(request, user):
    customer = Customer.objects.get(user=request.user)
    if request.method == 'POST':
        o_form = OrderForm(request.POST)
        if o_form.is_valid() : 
            instance = o_form.save(commit=False)
            instance.customer = customer
            instance.save()
            ForPayments.objects.create(
                customer = customer,
                For_online_payment = instance
            )    
            return redirect('Initialize_requestForm', user=user)       
    else:
        o_form = OrderForm(instance=customer)
    context = {
        'o_form': o_form,
         }
    return render(request, 'users/requestForm.html', context)         

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'customer'])
def ShoppingForm(request, user):
    customer = Customer.objects.get(user=user)
    if request.method == "POST":
        s_form = Shopping_Form(request.POST)
        if s_form.is_valid():
            instance = s_form.save(commit=False)
            instance.customer = customer
            instance.save()
            ForPayments.objects.create(
                customer = customer,
                For_shopping_payment = instance
            )
            messages.success(request, f'Your Request is Successful, Make Your Transfer to the following account ')
            messages.warning(request, f'Please Include your username for easy identification')
            return redirect('/') 
    else:
        s_form=Shopping_Form(instance=customer)

    return render (request, 'users/shopping.html', {'s_form':s_form})    

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'customer'])
def multipleRequest_cash(request, user):
    Request_CashSet = inlineformset_factory(Customer, MakeRequestCash, fields=(
        'reciever_name', 'Address_of_reciever', 'Package_description', 
        'Package_description', 'Choice_for_TP', 'reciever_phone_number', 'Your_location'), extra=5)
    customer = Customer.objects.get(user=request.user)
    c_formset = Request_CashSet()
    if request.method == 'POST':
        c_formset = Request_Cash(request.POST, request.FILES)
        if c_formset.is_valid() : 
            instance1 = c_formset.save(commit=False)
            instance1.customer = customer
            instance1.save()
            ForPayments.objects.create(
                customer = customer,
                For_cash_payment = instance1
            )    
            return redirect('Initialize_requestForm', user=user)       
    else:
        c_form = Request_CashSet()
    context = {
        'c_formset': c_formset,
         }
    return render(request, 'users/multipleRequest.html', context)         

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'customer'])
def Initialize_requestForm(request, user):
    pass       
    
    def pay(request, user):
        url = "https://api.paystack.co/transaction/initialize"
        payload =json.dumps ({
            'email': request.user.email,
            'amount': '50000', 
        })

        headers = { 
        "Authorization": "Bearer sk_test_1d32c71fd73944bd712f5b94853de7fe325387ec",
        'Content-Type': 'appliation/json'
        }

        r = requests.request("POST", url, headers=headers, data=payload)
        print(r.text)
        if r.status_code != 200:
            return str(r.status_code)
        result = r.json()
        return result
   
    initialized = pay(request, user)
    print(initialized['data']['authorization_url'])
    customer = Customer.objects.get( user=user )
    request1= customer.makerequest_set.all()
    ForPayments.objects.filter(For_online_payment__in=request1).update(
        paystack_access_code = initialized['data']["access_code"],
        charge_id = initialized['data']['reference'],
        )
    link = initialized['data']['authorization_url']
    return HttpResponseRedirect(link)
    
    messages.success(request, f'Your Payment Is Successful')
    return render(request, 'users/requestForm.html', context)
    

@login_required(login_url='login')
def successPage(request):
    reference = request.GET.get('reference')
    print(reference)
    check_pay = ForPayments.objects.filter(charge_id=reference).exists()
    if check_pay == False:
        print('Error')
    else:
        payment = ForPayments.objects.filter(charge_id=reference).first()

        def verify_payment(request):
            url = "https://api.paystack.co/transaction/verify/"+reference

            headers = { 
            "Authorization": "Bearer sk_test_1d32c71fd73944bd712f5b94853de7fe325387ec",
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
    print(initialized['data']['status'])
    print(initialized['data']['reference'])
    if initialized['data']['status'] == 'success':
        ForPayments.objects.filter(charge_id=initialized['data']['reference']).update(paid=True, money_paid=initialized['data']['amount']/100)
    return render(request, 'users/success.html')

@login_required(login_url='login')
@admin_only
def AdminDashboard(request):
    request1 = MakeRequest.objects.all()
    customers = Customer.objects.all()
    
    total_customers = customers.count()

    total_request = request1.count()
    delivered = request1.filter(status='Delivered').count()
    pending = request1.filter(status='Pending').count()
    canceled = request1.filter(status='Canceled').count()
    out_for_delivery = request1.filter(status='Out for delivery').count()
    context = {
        'request1': request1, 
        'customers' : customers,
        'total_request': total_request,
        'delivered': delivered,
        'pending': pending,
        'canceled': canceled,
        'out_for_delivery':out_for_delivery,
    }

    return render(request, 'users/profile.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'customer'])
def customerDashboardPage(request, user):
    customer = Customer.objects.get( user=user )
    request_filter = customer.makerequest_set.all()
    request_filter_cash = customer.makerequestcash_set.all()

    pending1 = request_filter.filter(status='Pending')
    out_for_delivery = request_filter.filter(status='Out for delivery')
    delivered = request_filter.filter(status='Delivered')

    pending2 = request_filter_cash.filter(status='Pending')
    out_for_delivery2 = request_filter_cash.filter(status='Out for delivery')
    delivered2 = request_filter_cash.filter(status='Delivered')

    context = {
        'pending2':pending2,
        'out_for_delivery2': out_for_delivery2,
        'delivered2':delivered2,

        'pending1':pending1,
        'out_for_delivery': out_for_delivery,
        'delivered':delivered,
        'customer':customer,

    }
    
    return render(request, 'users/customerDashboard.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def updateRequestForm(request, pk):

    r_request = MakeRequest.objects.get(id=pk)
    o_form = adminform(instance= r_request) 

    if request.method == 'POST':
        o_form = adminform(request.POST,instance=r_request)
        if o_form.is_valid():
            obj = o_form.save(commit=False)
            by_user = request.user
            obj.save()
            return redirect('adminDashboard')
    context = {'o_form': o_form, }
    return render(request, 'users/requestForm.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def deleteRequestForm(request, pk):

    r_request = MakeRequest.objects.get(id=pk)
    o_form = OrderForm(instance= r_request) 

    if request.method == 'POST':
        o_form = OrderForm(request.POST,instance=r_request)
        if o_form.is_valid():
            obj = o_form.save(commit=False)
            by_user = request.user
            obj.save()
            return redirect('adminDashboard')
    context = {'o_form': o_form, }
    return render(request, 'users/requestForm.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'customer'])
def cancelRequest(request, pk):
    r_request = MakeRequest.objects.get(id=pk)
    if request.method == "POST":
        r_request.delete()
        return redirect('adminDashboard')
    context = {'item':r_request}
    return render(request, 'users/delete.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'customer'])
def orderHistory(request, user):
    customer = Customer.objects.get( user=user )

    request1 = customer.makerequest_set.all()
    request2 = customer.makerequestcash_set.all()
    shop_request = customer.shopping_set.all()

    request_count = request1.count()
    request2_count = request2.count()
    shop_request_count = shop_request.count()

    myFilter = OrderFilter(request.GET, queryset=request1)
    request1 = myFilter.qs

    myFilter2 = OrderFilter(request.GET, queryset=request2)
    request2 = myFilter2.qs

    context = {
        'shop_request_count':shop_request_count,
        'shop_request': shop_request,
        'myFilter2':myFilter2,
        'request2':request2,
        'request1':request1,
        'request_count':request_count,
        'request2_count':request2_count,
        'myFilter':myFilter,
    }
    return render(request, 'users/orderHistory.html', context)





#message.info
#message.warning
#message.success
#message.error
