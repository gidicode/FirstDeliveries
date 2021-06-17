from django.shortcuts import render, redirect
from django.conf import settings
from users.models import Customer, adminNotification, Anonymous
from users.forms import  AnonForm
from django.contrib import messages
from hashids import Hashids
from django.db.models import Q

# Create your views here.

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
                item_created = instance,
                order_id = h,
                email = instance.email
            ) 
            messages.success(request, f'Your Request for pickup is Successful, you will recieve a call from us shortly')
            tp_choice_1 = Anonymous.objects.filter(order_id = h).filter(Choice_for_TP= 'Bike' )
            if tp_choice_1:
                messages.success(request, f'Your mode of transportation is Bike Your delivery Fee is N500. Your Request Refrence ID is "{h}" ')
                messages.warning(request, f' An email containing this transaction details has been sent to you, Please Create an account to access more services')
            else:
                messages.success(request, f'Your mode of transportation is Tricycle(Keke) Your delivery Fee is N1000. Your Request Refrence ID is "{h}" ')
                messages.warning(request, f' An email containing this transaction details has been sent to you, Please Create an account to access more services')

            

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

def billing(request):
    return render(request, 'FDS_app/billing.html')

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

def notification(request):
    return render(request, 'FDS_app/notification.html')

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

def dashBase(request, user):
    customer = Customer.objects.get(user= user)
    n_filter = customer.delivered_set.all()
    n = n_filter.filter(viewed = False)

    notification_filter = customer.adminNotification_set.all()
    
    notify = notification_filter.filter(viewed = False)
    return render(request, 'FDS_app/dashBase.html', {'customer':customer, 'n':n, 'notify':notify})

def password_reset(request):
    return render(request, 'FDS_app/password_reset.html')


