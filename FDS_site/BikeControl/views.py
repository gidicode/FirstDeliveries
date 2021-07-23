from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from users.decorators import allowed_user
from users.filters import BikeFilter
from django.contrib.auth.decorators import login_required

# Create your views here.

#Dashboard
@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'Fleet Manager' ])
def Riders_Dashboard(request):    
    return render(request, 'BikeControl/dashboard.html')

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'Fleet Manager' ])
def assigned_Del(request):   
    return render(request, 'BikeControl/assignedRides.html')

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'Fleet Manager' ])
def update_assigned_Del(request, pk):
    assigned_deliveries =RidersDeliveries.objects.get(id=pk)
    riders_profile = RidersProfile.objects.all()
    as_form = updateRidersDelivery(instance=assigned_deliveries)

    if request.method == 'POST':
        as_form = updateRidersDelivery(request.POST, instance=assigned_deliveries)
        if as_form.is_valid():
            instance = as_form.save()
            if instance.staus == "Delivered":
                messages.success(request, "status updated to Delivered ")
            elif instance.staus == "Canceled":
                messages.error(request, "Status updated to Canceled ")
            elif instance.staus == "Transfered":
                messages.warning(request, "status updated to 'Transfered' ")
            else: 
                messages.info(request, "Delivery is still Pending ")

            check_busy = RidersDeliveries.objects.all()            
            all2 = check_busy.filter(rider = instance.rider).filter(staus = 'Pending').exists()            
            if all2 == True:
                pass                

            elif all2 == False:
                riders_profile.filter(pk = instance.rider.pk).update(busy = False)
                                         
            return redirect('assignedRides')
    return render(request, 'BikeControl/updateAssign.html', {'as_form': as_form})

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'Fleet Manager' ])
def AssignedRides(request):    
    assigned_deliveries = RidersDeliveries.objects.all()
    riders_profile = RidersProfile.objects.all()

    f = BikeFilter(request.GET, queryset=assigned_deliveries)
    assigned_deliveries=f.qs

    as_form = ridersdeliveryForm() 

    all_deliveries = assigned_deliveries.filter(staus = "Delivered").count()
    all_pending = assigned_deliveries.filter(staus = "Pending").count()
    e_payments = MakeRequest.objects.all()
    cash = MakeRequestCash.objects.all()
    shop = Shopping.objects.all()
    anon = Anonymous.objects.all()
    errand = Errand_service.objects.all()
    front_desk = Front_desk.objects.all()

    if request.method == 'POST':
        as_form = ridersdeliveryForm(request.POST)
        if as_form.is_valid():
            instance = as_form.save()
                                
            all = riders_profile.get(pk = instance.rider.pk)

            if all.busy == False:
                riders_profile.filter(pk = instance.rider.pk).update(busy = True)
            
            if instance.e_payment_request == None :
                pass
            else:
                #all = RidersDeliveries.objects.all()
                e_payments.filter(order_id = instance.e_payment_request.order_id).update(assigned = True)
                messages.success(request, f"successfuly assigned delivery to a dispatch Rider {instance.e_payment_request.order_id}")

            if instance.cash_request == None:
                pass
            else:
                cash.filter(order_id = instance.cash_request.order_id).update(assigned = True)
                messages.success(request, f"successfuly assigned delivery to a dispatch Rider {instance.cash_request.order_id}")

            if instance.shopping == None:
                pass
            else:
                shop.filter(order_id = instance.shopping.order_id).update(assigned= True)
                messages.success(request, f"successfuly assigned delivery to a dispatch Rider {instance.shopping.order_id}")

            if instance.anonymous == None:
                pass
            else:
                anon.filter(order_id = instance.anonymous.order_id).update(assigned = True)          
                messages.success(request, f"successfuly assigned delivery to a dispatch Rider {instance.anonymous.order_id}")

            if instance.errand == None:
                pass
            else:
                errand.filter(order_id = instance.errand.order_id).update(assigned = True)          
                messages.success(request, f"successfuly assigned delivery to a dispatch Rider {instance.errand.order_id}")

            if instance.front_desk == None:
                pass
            else:
                front_desk.filter(order_id = instance.front_desk.order_id).update(assigned = True)          
                messages.success(request, f"successfuly assigned delivery to a dispatch Rider {instance.front_desk.order_id}")
            
            return redirect('assignedRides')

    else:
        as_form =  ridersdeliveryForm()


    context = {
        'errand':errand,
        'front_desk':front_desk,
        'all_pending':all_pending,
        "all_deliveries":all_deliveries,
        'filter':f,
        "assigned_deliveries":assigned_deliveries,
        'as_form':as_form,
    }
    return render(request, 'BikeControl/assignedRides.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'Fleet Manager' ])
def all_Fleet(request):
    available_fleet = Fleets.fleet_plate_number
    bike_fleet = Fleets.objects.filter(category = "Bike").count()
    bike_fleet_all = Fleets.objects.filter(category = "Bike")

    tricycle = Fleets.objects.filter(category = "Tricycle").count()
    tricycle_fleet_all = Fleets.objects.filter(category = "Tricycle")
    #getting assignee
    rider = RidersProfile.objects.all()
    

    context = {
        'available_fleet':available_fleet,
        'bike_fleet':bike_fleet,
        'tricycle':tricycle,
        'rider':rider,
        'bike_fleet_all':bike_fleet_all,
        'tricycle_fleet_all':tricycle_fleet_all,
  
        #'assignee':assignee
    }

    return render(request, 'BikeControl/Fleet.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'Fleet Manager' ])
def Riders_identity(request):
    profile = RidersProfile.objects.all()    

    driver_count = RidersProfile.objects.all().count()

    total_drivers_tricycle = profile.filter(attached_bike__category = "Tricycle").count()
    total_drivers_bike = profile.filter(attached_bike__category = 'Bike').count()

    context = {
        "driver_count":driver_count,
        "profile": profile,
        "total_drivers_bike":total_drivers_bike,
        "total_drivers_tricycle":total_drivers_tricycle
    }

    return render(request, 'BikeControl/RidersProfile.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'Fleet Manager' ])
def All_riders_deliveries(request, rider):
    
    all_deliveries = RidersDeliveries.objects.filter(rider=rider)
    for_rider = RidersProfile.objects.get(id=rider)
    success = all_deliveries.filter( staus="Delivered").count()
    cancled = all_deliveries.filter( staus="Canceled").count()
    transfered = all_deliveries.filter( staus="Transfered").count()
    pending = all_deliveries.filter( staus="Pending").count()
    
    success_show = all_deliveries.filter( staus="Delivered")
    cancled_show = all_deliveries.filter( staus="Canceled")
    transfered_show = all_deliveries.filter( staus="Transfered")
    pending_show = all_deliveries.filter( staus="Pending")

    context = {
        'pending':pending,
        'transfered':transfered,
        'cancled':cancled,
        'success':success,
        "for_rider":for_rider,
        "all_deliveries":all_deliveries,

        "success_show":success_show,
        "cancled_show":cancled_show,
        "transfered_show":transfered_show,
        "pending_show":pending_show,        

    }

    return render(request, "BikeControl/allRiderDeliveries.html", context)

def AllActive(request):    
    profile = RidersProfile.objects.all()
    return render(request, 'BikeControl/active.html', {'profile':profile})

