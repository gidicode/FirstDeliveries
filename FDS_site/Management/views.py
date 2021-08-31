from Management.models import Management_Notification
from django.shortcuts import redirect, render
from.forms import *
from django.contrib import messages
from hashids import Hashids
from django.conf import settings
from users.filters import Staff_Name
from django.core.paginator import Paginator



# Create your views here.
def Front_page(request, user):
    customer = Customer.objects.get(user=request.user)  
    report = customer.office_report_set.filter(submit=False)
    admin = OFFICE_REPORT.objects.filter(admin_seen = False )
    chairman = OFFICE_REPORT.objects.filter(chairman_seen = False )
    operation = OFFICE_REPORT.objects.filter(operations_seen = False )
    runyi_seen = OFFICE_REPORT.objects.filter(runyi_seen = False )
    manager = OFFICE_REPORT.objects.filter(manager_seen = False )

    context = {
        'report':report,
        'admin':admin, 
        'chairman':chairman,
        'operation':operation,
        'runyi':runyi_seen,
        'manager':manager,
    }
    return render(request, 'Management/front_page.html', context)

def Create_Profile_management(request, user):
    customer = Customer.objects.get(user=request.user)    
    m_form =  Management_profile(request.POST, instance=customer)    
    if request.method == 'POST':
        m_form = Management_profile(request.POST, instance=customer)

        if m_form.is_valid():
            instance = m_form.save(commit=False)
            instance.staff_created = True
            instance = m_form.save()
            messages.success(request, f"You have succesfully updated your profile")
            return redirect('management_dashboard', user)
    else:
        m_form =  Management_profile(instance = customer)

    context = {
        'customer':customer,
        'm_form': m_form
    }
    return render(request, 'Management/create_profile.html', context)

def Create_report(request, user):
    customer = Customer.objects.get(user = request.user)
    if customer.staff_created == False:
        messages.error(request, 'please update your profile to create report')
        return redirect('management_dashboard', user)
    if request.method == 'POST' and 'btn_save' in request.POST:
        o_form = Report_Form(request.POST)
        if o_form.is_valid():
            instance = o_form.save(commit=False)
            instance.customer = customer
            instance.Categoty = 'Operations'
            instance.save()
                        
            hashids = Hashids( settings.MANAGEMENT, 5, settings.MANAGEMENT2)
            hashing_the_id = hashids.encode(instance.id)
            customer.office_report_set.filter(id = instance.id).update(ticket_num = hashing_the_id)
            messages.warning(request, "Your Report has been created, Look below to view active report")
            return redirect('management_dashboard', user)

    elif request.method == 'POST' and 'btn_submit' in request.POST:
        o_form = Report_Form(request.POST)
        if o_form.is_valid():
            instance = o_form.save(commit=False)
            instance.customer = customer
            instance.submit = True
            instance.Categoty = 'Operations'
            instance.save()

            hashids = Hashids(settings.MANAGEMENT, 5, settings.MANAGEMENT2)
            hashing_the_id = hashids.encode(instance.id)
            customer.office_report_set.filter(id = instance.id).update(ticket_num = hashing_the_id)            
            messages.success(request, f"Your report has been submitted successfully")
            return redirect('management_dashboard', user)
    else:
        o_form = Report_Form()
    
    context = {
        'o_form':o_form,
    }

    return render(request, 'Management/create_report.html', context)

def Edit_Report(request, pk):
    customer = Customer.objects.get(user=request.user)
    report_form = OFFICE_REPORT.objects.get(id=pk)
    if request.method == 'POST' and 'btn_save' in request.POST:
        E_form = Edit_Report_Form(request.POST, instance=report_form)
        if E_form.is_valid():            
            instance = E_form.save(commit=False)
            instance.customer = customer
            instance.save()

            hashids = Hashids( settings.MANAGEMENT, 5, settings.MANAGEMENT2)
            hashing_the_id = hashids.encode(instance.id)
            customer.office_report_set.filter(id = instance.id).update(ticket_num = hashing_the_id)
            messages.warning(request, "Report successfully updated")
            return redirect('management_dashboard', request.user.pk)

    elif request.method == 'POST' and 'btn_submit' in request.POST:
        E_form = Edit_Report_Form(request.POST, instance=report_form)
        if E_form.is_valid():
            instance = E_form.save(commit=False)
            instance.customer = customer
            instance.Categoty = 'Operations'
            instance.submit = True
            instance.save()
            messages.success(request, f"Your report has been submitted successfully")                      
            return redirect('management_dashboard', request.user.pk)

    else:
        E_form = Edit_Report_Form(instance=report_form)

    context = {
        'E_form':E_form,
        'customer':customer,
            }
    
    return render(request, 'Management/Edit_form.html', context)

def Fleet_Report(request, user):
    customer = Customer.objects.get(user=user)
    if request.method == 'POST' and 'btn_save' in request.POST:        
        fleet_form = Fleet_Report_Form(request.POST)
        if fleet_form.is_valid():
            instance = fleet_form.save(commit=False)
            instance.customer = customer
            instance.Categoty = 'Fleet'
            instance.save()

            hashids = Hashids( settings.MANAGEMENT, 5, settings.MANAGEMENT2)
            hashing_the_id = hashids.encode(instance.id)
            customer.office_report_set.filter(id = instance.id).update(ticket_num = hashing_the_id)
            messages.warning(request, "Your Report has been created, Look below to view active report")
            return redirect ('management_dashboard', user)

    elif request.method == 'POST' and 'btn_submit' in request.POST:
        fleet_form = Fleet_Report_Form(request.POST)
        if fleet_form.is_valid():
            instance = fleet_form.save(commit=False)
            instance.customer = customer
            instance.Categoty = 'Fleet'
            instance.submit = True
            instance.save()

            hashids = Hashids( settings.MANAGEMENT, 5, settings.MANAGEMENT2)
            hashing_the_id = hashids.encode(instance.id)
            customer.office_report_set.filter(id = instance.id).update(ticket_num = hashing_the_id)
            
            messages.success(request, f"Your report has been submitted successfully")
            return redirect('management_dashboard', user)
    else:
        fleet_form = Fleet_Report_Form()

    context = {
        'fleet_form': fleet_form,
        'customer':customer,
    }
    return render(request, 'Management/fleet_create_report.html', context)

def Edit_Fleet_Report(request, pk):
    customer = Customer.objects.get(user= request.user)
    fleet_report = OFFICE_REPORT.objects.get(id = pk)
    if request.method == 'POST' and 'btn_save' in request.POST:        
        fleet_form = Fleet_Report_Form(request.POST, instance= fleet_report)
        if fleet_form.is_valid():
            instance = fleet_form.save(commit=False)                    
            instance.save()
            messages.warning(request, "Saved successfully")
            return redirect ('management_dashboard', request.user.pk)

    elif request.method == 'POST' and 'btn_submit' in request.POST:
        fleet_form = Fleet_Report_Form(request.POST, instance=fleet_report)
        if fleet_form.is_valid():
            instance = fleet_form.save(commit=False)                       
            instance.submit = True
            instance.save()
            Management_Notification.objects.create(
                customer = customer,
                notification_message = f"New report created by {customer.firstname}",
                notification_ID = instance.ticket_num,                
            )
            messages.success(request, f"Your report has been submitted successfully")
            return redirect('management_dashboard', request.user.pk)
    else:
        fleet_form = Fleet_Report_Form(instance= fleet_report)

    context = {
        'fleet_form': fleet_form,
        'customer':customer,
    }
    return render(request, 'Management/Edit_fleet_report.html', context)

def ICT_Report(request, user):
    customer = Customer.objects.get(user=user)
    if request.method == 'POST' and 'btn_save' in request.POST:        
        ict_form = ICT_Report_Form(request.POST)
        if ict_form.is_valid():
            instance = ict_form.save(commit=False)
            instance.customer = customer
            instance.Categoty = 'ICT'
            instance.save()

            hashids = Hashids( settings.MANAGEMENT, 5, settings.MANAGEMENT2)
            hashing_the_id = hashids.encode(instance.id)
            customer.office_report_set.filter(id = instance.id).update(ticket_num = hashing_the_id)
            messages.warning(request, "Your Report has been created, Look below to view active report")
            return redirect ('management_dashboard', user)

    elif request.method == 'POST' and 'btn_submit' in request.POST:
        ict_form = ICT_Report_Form(request.POST)
        if ict_form.is_valid():
            instance = ict_form.save(commit=False)
            instance.customer = customer
            instance.Categoty = 'ICT'
            instance.submit = True
            instance.save()

            hashids = Hashids( settings.MANAGEMENT, 5, settings.MANAGEMENT2)
            hashing_the_id = hashids.encode(instance.id)
            customer.office_report_set.filter(id = instance.id).update(ticket_num = hashing_the_id)            
            messages.success(request, f"Your report has been submitted successfully")
            return redirect('management_dashboard', user)
    else:
        ict_form = ICT_Report_Form()

    context = {
        'ict_form': ict_form,
        'customer':customer,
    }
    return render(request, 'Management/ICT_create_report.html', context)

def Edit_ict_Report(request, pk):
    customer = Customer.objects.get(user= request.user)
    ICT_report = OFFICE_REPORT.objects.get(id = pk)
    if request.method == 'POST' and 'btn_save' in request.POST:
        ict_form = EditICT_Report_Form(request.POST, instance= ICT_report)
        if ict_form.is_valid():
            ict_form.save() 
            messages.warning(request, "Saved successfully")
            return redirect ('management_dashboard', request.user.pk)

    elif request.method == 'POST' and 'btn_submit' in request.POST:
        ict_form = EditICT_Report_Form(request.POST, instance= ICT_report)
        if ict_form.is_valid():
            instance = ict_form.save(commit=False)                       
            instance.submit = True
            instance.save()
            Management_Notification.objects.create(
                customer = customer,
                notification_message = f"New report created by {customer.firstname}",
                notification_ID = instance.ticket_num,                
            )
            messages.success(request, f"Your report has been submitted successfully")
            return redirect('management_dashboard', request.user.pk)
    else:
        ict_form = EditICT_Report_Form(instance= ICT_report)

    context = {
        'ict_form': ict_form,
        'customer':customer,
    }
    return render(request, 'Management/Edit_ict_form.html', context)

def Marketing_Report(request, user):
    customer = Customer.objects.get(user=user)
    if request.method == 'POST' and 'btn_save' in request.POST:        
        Market_form = Marketing_Report_Form(request.POST)
        if Market_form.is_valid():
            instance = Market_form.save(commit=False)
            instance.customer = customer
            instance.Categoty = 'Market'
            instance.save()

            hashids = Hashids( settings.MANAGEMENT, 5, settings.MANAGEMENT2)
            hashing_the_id = hashids.encode(instance.id)
            customer.office_report_set.filter(id = instance.id).update(ticket_num = hashing_the_id)
            messages.warning(request, "Your Report has been created, Look below to view active report")
            return redirect ('management_dashboard', user)

    elif request.method == 'POST' and 'btn_submit' in request.POST:
        Market_form = Marketing_Report_Form(request.POST)
        if Market_form.is_valid():
            instance = Market_form.save(commit=False)
            instance.customer = customer
            instance.Categoty = 'Market'
            instance.submit = True
            instance.save()

            hashids = Hashids( settings.MANAGEMENT, 5, settings.MANAGEMENT2)
            hashing_the_id = hashids.encode(instance.id)
            customer.office_report_set.filter(id = instance.id).update(ticket_num = hashing_the_id)
            
            messages.success(request, f"Your report has been submitted successfully")
            return redirect('management_dashboard', user)
    else:
        Market_form = Marketing_Report_Form()

    context = {
        'Market_form': Market_form,
        'customer':customer,
    }
    return render(request, 'Management/Marketing_report_.html', context)

def Edit_market_Report(request, pk):
    customer = Customer.objects.get(user= request.user)
    market_report = OFFICE_REPORT.objects.get(id = pk)
    if request.method == 'POST' and 'btn_save' in request.POST:        
        market_form = Marketing_Report_Form(request.POST, instance= market_report)
        if market_form.is_valid():
            instance = market_form.save(commit=False)
            instance.save()
            messages.warning(request, "Saved successfully")
            return redirect ('management_dashboard', request.user.pk)

    elif request.method == 'POST' and 'btn_submit' in request.POST:
        market_form = Marketing_Report_Form(request.POST, instance= market_report)
        if market_form.is_valid():
            instance = market_form.save(commit=False)                       
            instance.submit = True
            instance.save()
            messages.success(request, f"Your report has been submitted successfully")

            Management_Notification.objects.create(
                customer = customer,
                notification_message = f"New report created by {customer.firstname}",
                notification_ID = instance.ticket_num,                
            )
            return redirect('management_dashboard', request.user.pk)
    else:
        market_form = Marketing_Report_Form(instance= market_report)

    context = {
        'market_form': market_form,
        'customer':customer,
    }
    return render(request, 'Management/Edit_market_report.html', context)

def Front_Desk_Report(request, user):
    customer = Customer.objects.get(user=user)
    if request.method == 'POST' and 'btn_save' in request.POST:        
        front_form = Front_Report_Form(request.POST)
        if front_form.is_valid():
            instance = front_form.save(commit=False)
            instance.customer = customer
            instance.Categoty = 'Front'
            instance.save()

            hashids = Hashids( settings.MANAGEMENT, 5, settings.MANAGEMENT2)
            hashing_the_id = hashids.encode(instance.id)
            customer.office_report_set.filter(id = instance.id).update(ticket_num = hashing_the_id)
            messages.warning(request, "Your Report has been created, Look below to view active report")
            return redirect ('management_dashboard', user)

    elif request.method == 'POST' and 'btn_submit' in request.POST:
        front_form = Front_Report_Form(request.POST)
        if front_form.is_valid():
            instance = front_form.save(commit=False)
            instance.customer = customer
            instance.Categoty = 'Front'
            instance.submit = True
            instance.save()

            hashids = Hashids( settings.MANAGEMENT, 5, settings.MANAGEMENT2)
            hashing_the_id = hashids.encode(instance.id)
            customer.office_report_set.filter(id = instance.id).update(ticket_num = hashing_the_id)            
            messages.success(request, f"Your report has been submitted successfully")
            return redirect('management_dashboard', user)
    else:
        front_form = Front_Report_Form()

    context = {
        'front_form': front_form,
        'customer':customer,
    }
    return render(request, 'Management/Front_report.html', context)

def Edit_front_Report(request, pk):
    customer = Customer.objects.get(user= request.user)
    front_report = OFFICE_REPORT.objects.get(id = pk)
    if request.method == 'POST' and 'btn_save' in request.POST:        
        front_form = Front_Report_Form(request.POST, instance= front_report)
        if front_form.is_valid():
            instance = front_form.save(commit=False)
            instance.save()
            messages.warning(request, "Saved successfully")
            return redirect ('management_dashboard', request.user.pk)

    elif request.method == 'POST' and 'btn_submit' in request.POST:
        front_form = Front_Report_Form(request.POST, instance= front_report)
        if front_form.is_valid():
            instance = front_form.save(commit=False)                       
            instance.submit = True
            instance.save()

            Management_Notification.objects.create(
                customer = customer,
                notification_message = f"New report created by {customer.firstname}",
                notification_ID = instance.ticket_num,                
            )
            messages.success(request, f"Your report has been submitted successfully")
            return redirect('management_dashboard', request.user.pk)
    else:
        front_form = Front_Report_Form(instance= front_report)

    context = {
        'front_form': front_form,
        'customer':customer,
    }
    return render(request, 'Management/edit_front_report.html', context)

def Status_History(request, user):
    customer = Customer.objects.get(user = user)
    all_fleet_report = customer.office_report_set.filter(submit = True).filter( Categoty = 'Fleet')   
    all_operations_report = customer.office_report_set.filter(submit = True).filter( Categoty = 'Operations')    
    all_front_report = customer.office_report_set.filter(submit = True).filter( Categoty = 'Front')   
    all_marketing_report = customer.office_report_set.filter(submit = True).filter( Categoty = 'Market')  
    all_ict_report = customer.office_report_set.filter(submit = True).filter( Categoty = 'ICT')    
    context = {
        'all_submitted_report':all_fleet_report,
        'all_operations_report': all_operations_report,
        'all_front_desk_report': all_front_report,
        'all_marketing_report': all_marketing_report,
        'all_ict_report': all_ict_report,
        'customer':customer,
    }
    return render(request, 'Management/Report_History.html', context)

def History_details(request, pk):
    customer = Customer.objects.get(user= request.user)
    report = customer.office_report_set.filter( id= pk)

    context = {
        'customer':customer,
        'report':report,
    }
    return render(request, 'Management/History_detail.html', context)

def History_details_management(request, pk):
    customer = Customer.objects.get(user= request.user)
    report = OFFICE_REPORT.objects.filter( id= pk)
    if request.user.groups.filter(name = 'MANAGEMENT_OPERATION'):        
        OFFICE_REPORT.objects.filter( id= pk).update(operations_seen = True)
    elif request.user.groups.filter(name = 'MANAGEMENT_CHAIRMAN'):
        OFFICE_REPORT.objects.filter( id= pk).update(chairman_seen = True)
    elif request.user.groups.filter(name = 'MANAGEMENT_MANAGER'):
        OFFICE_REPORT.objects.filter( id= pk).update(manager_seen = True)
    elif request.user.groups.filter(name = "MANAGEMENT_RUNYI"):
        OFFICE_REPORT.objects.filter( id= pk).update(runyi_seen = True)
    elif request.user.groups.filter(name = 'MANAGEMENT_ADMIN'):
        OFFICE_REPORT.objects.filter( id= pk).update(admin_seen = True)        
    context = {
        'customer':customer,
        'report':report,
    }  
    return render(request, 'Management/History_details_management.html', context)

def Management_view(request, user):
    all_report = OFFICE_REPORT.objects.filter(submit = True)
    customer = Customer.objects.get(user = user)
    
    context = {
        'all_report': all_report,
        'customer':customer,
    }

    return render(request,'Management/management_view_report.html', context)

def Chairman_response(request, pk):
    customer = Customer.objects.get(user = request.user)
    actual_form = OFFICE_REPORT.objects.get(id = pk)
    if request.method == 'POST':
        response_form = Chairman_Response_Form(request.POST, instance = actual_form)
        if response_form.is_valid():
            instance = response_form.save()
            customer_name = instance.customer.first_name
            messages.success(request, f'Your response to {customer_name} has been sent')
            return redirect( 'management_list_details', pk)
    else:
        response_form = Chairman_Response_Form(instance=actual_form)

    context = {
        'response_form':response_form,
        'customer':customer,
        'actual_form':actual_form,
    }
    return render(request, 'Management/Chairman_response.html', context)

def Operations_response(request, pk):
    customer = Customer.objects.get(user = request.user)
    actual_form = OFFICE_REPORT.objects.get(id = pk)
    if request.method == 'POST':
        response_form = Operations_Response_Form(request.POST, instance = actual_form)
        if response_form.is_valid():
            instance = response_form.save()
            customer_name = instance.customer.first_name
            messages.success(request, f'Your response to {customer_name} has been sent')
            return redirect( 'management_list_details', pk)
    else:
        response_form = Operations_Response_Form(instance=actual_form)

    context = {
        'response_form':response_form,
        'customer':customer,
        'actual_form':actual_form,
    }
    return render(request, 'Management/Operations_Response.html', context)

def Admin_response(request, pk):
    customer = Customer.objects.get(user = request.user)
    actual_form = OFFICE_REPORT.objects.get(id = pk)
    if request.method == 'POST':
        response_form = Admin_Response_Form(request.POST, instance = actual_form)
        if response_form.is_valid():
            instance = response_form.save()
            customer_name = instance.customer.first_name
            messages.success(request, f'Your response to {customer_name} has been sent')
            return redirect( 'management_list_details', pk)
    else:
        response_form = Admin_Response_Form(instance=actual_form)

    context = {
        'response_form':response_form,
        'customer':customer,
        'actual_form':actual_form,
    }
    return render(request, 'Management/Admin_response.html', context)

def Manager_response(request, pk):
    customer = Customer.objects.get(user = request.user)
    actual_form = OFFICE_REPORT.objects.get(id = pk)
    if request.method == 'POST':
        response_form = Manager_Response_Form(request.POST, instance = actual_form)
        if response_form.is_valid():
            instance = response_form.save()
            customer_name = instance.customer.first_name
            messages.success(request, f'Your response to {customer_name} has been sent')
            return redirect( 'management_list_details', pk)
    else:
        response_form = Manager_Response_Form(instance=actual_form)

    context = {
        'response_form':response_form,
        'customer':customer,
        'actual_form':actual_form,
    }
    return render(request, 'Management/Manager_response.html', context)

def Runyi_Response(request, pk):
    customer = Customer.objects.get(user = request.user)
    actual_form = OFFICE_REPORT.objects.get(id = pk)
    if request.method == 'POST':
        response_form = Runyi_Response_Form(request.POST, instance = actual_form)
        if response_form.is_valid():
            instance = response_form.save()
            customer_name = instance.customer.first_name
            messages.success(request, f'Your response to {customer_name} has been sent')
            return redirect( 'management_list_details', pk)
    else:
        response_form = Runyi_Response_Form(instance = actual_form)

    context = {
        'response_form':response_form,
        'customer':customer,
        'actual_form':response_form,
    }
    return render(request, 'Management/Runyi_response.html', context)


def Management_report_list(request, user):
    customer = Customer.objects.get(user = user)
    all_submitted_report = OFFICE_REPORT.objects.filter(submit = True)
    filter_name  = Staff_Name(request.GET, queryset=all_submitted_report)
    all_submitted_report = filter_name.qs

    paginator1 = Paginator(all_submitted_report, 10)
    page = request.GET.get('page')
    page_obj = paginator1.get_page(page)
    context = {
        'all_submitted_report':all_submitted_report,
        'customer':customer,
        'filter_name':filter_name,
        'page_obj':page_obj,
    }
    return render(request, 'Management/management_view_list.html', context)

