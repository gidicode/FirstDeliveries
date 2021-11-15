from django.shortcuts import render, redirect
from django.conf import settings
from users.models import Customer, adminNotification, Anonymous
from users.forms import  AnonForm
from django.contrib import messages
from hashids import Hashids
from django.db.models import Q
import requests
import json
from  users.decorators import allowed_user
from django.contrib.auth.decorators import login_required

def index(request):
    if request.method == 'POST':
        c_form = AnonForm(request.POST)
        if c_form.is_valid():
            instance = c_form.save(commit=False)
            instance.save()

            hashids = Hashids(salt= settings.HASHANON, min_length=7)
            h= hashids.encode(instance.id)
            Anonymous.objects.filter(pk = instance.id).update(order_id= h)
            adminNotification.objects.create(
                item_created = "Anonymous",
                order_id = h,                
            )
            if instance.Choice_for_TP == 'Bike':
                
                
                def SendSms():
                    url = 'https://app.multitexter.com/v2/app/sendsms'
                    link = f'https://flls.ng/search/?order_id={h}'
                    sms_message = f"Created succesfully, to check status visit {link}, Delivery Fee is a Minimum of N500 "
                    number = instance.Your_phone_number             
                    payload = json.dumps({         
                        'message' : sms_message,
                        'sender_name' : 'FLLS',
                        'recipients' : number,                
                        })
                    headers = {                
                        'Authorization': 'Bearer E9jriOUBg5ssOLSAc6DzE94O9cjxQ5kB6iW7DEv6mEADXs5Q2QcPXgOS0AVL',
                        'Content-Type': 'application/json',
                    }
                    response = requests.request('POST', url, headers=headers, data=payload)                            
                    result = response.json()
        
                    return result
                SendSms()
                

            elif instance.Choice_for_TP == 'Tricycle':
                
                def SendSms():
                    url = 'https://app.multitexter.com/v2/app/sendsms'
                    link = f'https://flls.ng/search/?order_id={h}'
                    sms_message = f"Created succesfully, to check status visit {link}, Fee is a Minimum of N1000 "
                    number = instance.Your_phone_number               
                    payload = json.dumps({         
                        'message' : sms_message,
                        'sender_name' : 'FLLS',
                        'recipients' : number,                
                        })
                    headers = {                
                        'Authorization': 'Bearer E9jriOUBg5ssOLSAc6DzE94O9cjxQ5kB6iW7DEv6mEADXs5Q2QcPXgOS0AVL',
                        'Content-Type': 'application/json',
                    }
                    response = requests.request('POST', url, headers=headers, data=payload)                            
                    result = response.json()
        
                    return result
                SendSms()

            messages.success(request, f'Your request for pickup is successful, you will recieve a call from us shortly')
            tp_choice_1 = Anonymous.objects.filter(order_id = h).filter(Choice_for_TP= 'Bike' )
            if tp_choice_1:
                messages.success(request, f'Mode of transportation: Bike, Delivery Fee: N500, Refrence ID: "{h}" ')
                messages.warning(request, f' An SMS containing a link to this transaction details has been sent to you, please create an account to access more services.')
            else:
                messages.success(request, f'Mode of transportation: Tricycle(Keke), Delivery Fee: N1000, Refrence ID: "{h}" ')
                messages.warning(request, f' An SMS containing a link to this transaction details has been sent to you, Please create an account to access more services.')

            

            return redirect('register')
    else:
        c_form = AnonForm()
                
    context = {
        'c_form': c_form,
        }
    return render(request, 'FDS_app/index.html', context)

def about(request):
    return render(request, 'FDS_app/about.html')

def userRegPage(request):
    return render(request, 'FDS_app/userRegPage.html')

def Terms(request):
    return render(request, 'FDS_app/Terms&Condition.html')

def error(request):
    return render(request, 'FDS_app/error.html')

def search(request):
    results = []

    if request.method == "GET":
        query = request.GET.get('order_id')

        if query == '':
            query = 'None'
        results = Anonymous.objects.filter(Q(order_id = query))
            
    return render(request, 'FDS_app/Search.html', {'query': query, 'results':results})

def SignUpBase(request):
    return render(request, 'FDS_app/signupBase.html')

def order(request):
    return render(request, 'FDS_app/order.html')

def passReset(request):
    return render(request, 'FDS_app/passReset.html')

def payment_success(request):
    return render(request, 'FDS_app/payment_success.html')

def pricing(request):
    return render(request, 'FDS_app/pricing.html')

def userSettings(request):
    return render(request, 'FDS_app/userSettings.html')

def signup(request):
    return render(request, 'FDS_app/signup.html')

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'customer', 'Fleet Manager', 'Front Desk', 'Cashier'])
def dashBase(request, user):
    customer = Customer.objects.get(user= user)
    n_filter = customer.delivered_set.all()
    n = n_filter.filter(viewed = False)

    notification_filter = customer.adminNotification_set.all()
    
    notify = notification_filter.filter(viewed = False)
    return render(request, 'FDS_app/dashBase.html', {'customer':customer, 'n':n, 'notify':notify})

def password_reset(request):
    return render(request, 'FDS_app/password_reset.html')


