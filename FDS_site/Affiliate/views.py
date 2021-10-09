from .models import *
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


# Create your views here.
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
    return render(request, 'Affiliate/Marketer_Dashboard.html')