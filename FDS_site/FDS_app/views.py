from django.shortcuts import render
from django.http import HttpResponse
from users.models import Customer, Delivered, adminNotification

# Create your views here.
def index(request):
    return render(request, 'FDS_app/index.html')

def about(request):
    return render(request, 'FDS_app/about.html')

def userRegPage(request):
    return render(request, 'FDS_app/userRegPage.html')

def billing(request):
    return render(request, 'FDS_app/billing.html')

def error(request):
    return render(request, 'FDS_app/error.html')

def history(request):
    return render(request, 'FDS_app/history.html')

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


