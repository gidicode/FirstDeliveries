from Management.models import Management_Notification
from django.shortcuts import redirect, render
from.forms import *
from django.contrib import messages
from hashids import Hashids
from django.conf import settings
from users.filters import Staff_Name
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from users.decorators import *


def Notification_email(recipient_list, Staff_Name):
              
        send_mas = send_mail(
            subject ='New Request!!!', 
            message = f"{Staff_Name} just sent in a  report, Visit flls.ng/login/ to view report",                
            from_email = 'support@flls.ng',
            recipient_list= recipient_list,
            fail_silently = False,
        )
        return HttpResponse('%s'%send_mas)

@login_required(login_url='login')
@allowed_user(allowed_roles=[
        'FLLS', 'MANAGEMENT', 'ICT',  
        'MANAGEMENT_OPERATION', 'OPERATIONS',
        'FLM MANAGER', 'TANK', 'IWH', 'MANAGEMENT_RUNYI', 
        'MANAGEMENT_MANAGER', 'MANAGEMENT_OPERATION',
        'MANAGEMENT_CHAIRMAN', 'Marketing',
        'Fleet Manager', 'Front Desk', 'MANAGEMENT_ADMIN',
        ])
def Front_page(request, user):
    customer = Customer.objects.get(user=request.user)  
    managers_report = customer.office_report_set.filter(for_chairman_manager=False)         
    flls_team = customer.office_report_set.filter(for_mangerFLLS =False)

    admin = OFFICE_REPORT.objects.filter(for_admin = True).filter(admin_seen = False )
    chairman = OFFICE_REPORT.objects.filter(for_chairman_manager =True).filter(chairman_seen = False )
    operation = OFFICE_REPORT.objects.filter(for_operation = True).filter(operations_seen = False )
    runyi_seen = OFFICE_REPORT.objects.filter(for_runyi = True).filter(runyi_seen = False)
    manager = OFFICE_REPORT.objects.filter(for_mangerFLLS=True).filter(manager_seen = False )
    fllm_manager = OFFICE_REPORT.objects.filter(for_manager_FLM=True).filter(manager_flm_seen = False )

    context = {
        'managers_report': managers_report,
        'flls_team' : flls_team,
        'admin':admin, 
        'chairman':chairman,
        'operation':operation,
        'runyi':runyi_seen,
        'manager':manager,
        'fllm_manager':fllm_manager,
    }
    return render(request, 'Management/front_page.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=[
        'FLLS', 'MANAGEMENT', 'ICT',
        'MANAGEMENT_OPERATION', 'OPERATIONS',
        'FLM MANAGER', 'TANK', 'IWH', 'MANAGEMENT_RUNYI', 
        'MANAGEMENT_MANAGER', 'MANAGEMENT_OPERATION',
        'MANAGEMENT_CHAIRMAN', 'Marketing',
        'Fleet Manager', 'Front Desk', 'MANAGEMENT_ADMIN',
        ])
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

@login_required(login_url='login')
@allowed_user(allowed_roles=[
        'FLLS', 'MANAGEMENT',
        'MANAGEMENT_OPERATION', 'OPERATIONS',
        'FLM MANAGER', 'MANAGEMENT_RUNYI', 
        'MANAGEMENT_MANAGER', 'MANAGEMENT_CHAIRMAN',
        'MANAGEMENT_ADMIN',
        ])
def Logistics(request, user):
    return render(request, "Management/logiscticsPage.html")

@login_required(login_url='login')
@allowed_user(allowed_roles=[
        'FLLS', 'MANAGEMENT',
        'MANAGEMENT_OPERATION', 'OPERATIONS',        
        ])
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
            instance.for_chairman_manager = True
            instance.for_manager_FLM = True
            instance.for_runyi = True
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

@login_required(login_url='login')
@allowed_user(allowed_roles=['FLLS', 'MANAGEMENT', 'MANAGEMENT_OPERATION', 'OPERATIONS',])   
def Edit_Report(request, pk):
    customer = Customer.objects.get(user=request.user)
    report_form = OFFICE_REPORT.objects.get(id=pk)
    if request.method == 'POST' and 'btn_save' in request.POST:
        E_form = Edit_Report_Form(request.POST, instance=report_form)
        if E_form.is_valid():            
            instance = E_form.save(commit=False)
            instance.customer = customer
            instance.save()            
            messages.warning(request, "Report successfully updated")
            return redirect('management_dashboard', request.user.pk)

    elif request.method == 'POST' and 'btn_submit' in request.POST:
        E_form = Edit_Report_Form(request.POST, instance=report_form)
        if E_form.is_valid():
            instance = E_form.save(commit=False)            
            instance.for_chairman_manager = True
            instance.for_manager_FLM = True
            instance.for_runyi = True
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

@login_required(login_url='login')
@allowed_user(allowed_roles=['FLLS', 'Fleet Manager',])
def Fleet_Report(request, user):
    customer = Customer.objects.get(user=user)
    if customer.staff_created == False:
        messages.error(request, 'please update your profile to create report')
        return redirect('management_dashboard', user)
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
            instance.for_mangerFLLS = True            
            instance.save()  
                 
            hashids = Hashids( settings.MANAGEMENT, 5, settings.MANAGEMENT2)
            hashing_the_id = hashids.encode(instance.id)
            customer.office_report_set.filter(id = instance.id).update(ticket_num = hashing_the_id)

            #email_list = ['benjaminokpodu@gmail.com', 'usuugwo@gmail.com']
           # Staff_Name = instance.customer.first_name
            #Notification_email(email_list, Staff_Name)
            
            messages.success(request, f"Your report has been submitted successfully")
            return redirect('management_dashboard', user)
    else:
        fleet_form = Fleet_Report_Form()

    context = {
        'fleet_form': fleet_form,
        'customer':customer,
    }
    return render(request, 'Management/fleet_create_report.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['FLLS', 'Fleet Manager',])
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
            instance.for_mangerFLLS = True                 
            instance.save()           

            #email_list = ['benjaminokpodu@gmail.com', 'usuugwo@gmail.com']
           # Staff_Name = instance.customer.first_name
            #Notification_email(email_list, Staff_Name)
            messages.success(request, f"Your report has been submitted successfully")
            return redirect('management_dashboard', request.user.pk)
    else:
        fleet_form = Fleet_Report_Form(instance= fleet_report)

    context = {
        'fleet_form': fleet_form,
        'customer':customer,
    }
    return render(request, 'Management/Edit_fleet_report.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['FLLS', 'ICT',])
def ICT_Report(request, user):
    customer = Customer.objects.get(user= request.user)
    if customer.staff_created == False:
        messages.error(request, 'please update your profile to create report')
        return redirect('management_dashboard', user)
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
            instance.for_mangerFLLS = True                         
            instance.save()
                 
            hashids = Hashids( settings.MANAGEMENT, 5, settings.MANAGEMENT2)
            hashing_the_id = hashids.encode(instance.id)
            customer.office_report_set.filter(id = instance.id).update(ticket_num = hashing_the_id)  
            
            #email_list = ['benjaminokpodu@gmail.com', 'usuugwo@gmail.com']
           # Staff_Name = instance.customer.first_name
            #Notification_email(email_list, Staff_Name)          
            messages.success(request, f"Your report has been submitted successfully")
            return redirect('management_dashboard', user)
    else:
        ict_form = ICT_Report_Form()

    context = {
        'ict_form': ict_form,
        'customer':customer,
    }
    return render(request, 'Management/ICT_create_report.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['FLLS', 'ICT',])
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
            instance.for_mangerFLLS = True             
            instance.save()
            
            email_list = ['benjaminokpodu@gmail.com', 'usuugwo@gmail.com']
            Staff_Name = instance.customer.first_name
            Notification_email(email_list, Staff_Name)
            messages.success(request, f"Your report has been submitted successfully")
            return redirect('management_dashboard', request.user.pk)
    else:
        ict_form = EditICT_Report_Form(instance= ICT_report)

    context = {
        'ict_form': ict_form,
        'customer':customer,
    }
    return render(request, 'Management/Edit_ict_form.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['FLLS', 'Marketing',])
def Marketing_Report(request, user):
    customer = Customer.objects.get(user=user)
    if customer.staff_created == False:
        messages.error(request, 'please update your profile to create report')
        return redirect('management_dashboard', user)
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
            instance.for_mangerFLLS = True                         
            instance.save()

            hashids = Hashids( settings.MANAGEMENT, 5, settings.MANAGEMENT2)
            hashing_the_id = hashids.encode(instance.id)
            customer.office_report_set.filter(id = instance.id).update(ticket_num = hashing_the_id)

            #email_list = ['benjaminokpodu@gmail.com', 'usuugwo@gmail.com']
           # Staff_Name = instance.customer.first_name
            #Notification_email(email_list, Staff_Name)
            messages.success(request, f"Your report has been submitted successfully")
            return redirect('management_dashboard', user)
    else:
        Market_form = Marketing_Report_Form()

    context = {
        'Market_form': Market_form,
        'customer':customer,
    }
    return render(request, 'Management/Marketing_report_.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['FLLS', 'Marketing',])
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
            instance.for_mangerFLLS = True                       
            instance.save()

            #email_list = ['benjaminokpodu@gmail.com', 'usuugwo@gmail.com']
           # Staff_Name = instance.customer.first_name
            #Notification_email(email_list, Staff_Name)
            messages.success(request, f"Your report has been submitted successfully")
            return redirect('management_dashboard', request.user.pk)
    else:
        market_form = Marketing_Report_Form(instance= market_report)

    context = {
        'market_form': market_form,
        'customer':customer,
    }
    return render(request, 'Management/Edit_market_report.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['FLLS', 'Front Desk',])
def Front_Desk_Report(request, user):
    customer = Customer.objects.get(user=user)
    if customer.staff_created == False:
        messages.error(request, 'please update your profile to create report')
        return redirect('management_dashboard', user)
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
            instance.for_mangerFLLS = True                      
            instance.save()

            hashids = Hashids( settings.MANAGEMENT, 5, settings.MANAGEMENT2)
            hashing_the_id = hashids.encode(instance.id)
            customer.office_report_set.filter(id = instance.id).update(ticket_num = hashing_the_id)

            #email_list = ['benjaminokpodu@gmail.com', 'usuugwo@gmail.com']
           # Staff_Name = instance.customer.first_name
            #Notification_email(email_list, Staff_Name)          
            messages.success(request, f"Your report has been submitted successfully")
            return redirect('management_dashboard', user)
    else:
        front_form = Front_Report_Form()

    context = {
        'front_form': front_form,
        'customer':customer,
    }
    return render(request, 'Management/Front_report.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['FLLS', 'Front Desk',])
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
            instance.for_mangerFLLS = True                      
            instance.save()

            #email_list = ['benjaminokpodu@gmail.com', 'usuugwo@gmail.com']
           # Staff_Name = instance.customer.first_name
            #Notification_email(email_list, Staff_Name)            
            messages.success(request, f"Your report has been submitted successfully")
            return redirect('management_dashboard', request.user.pk)
    else:
        front_form = Front_Report_Form(instance= front_report)

    context = {
        'front_form': front_form,
        'customer':customer,
    }
    return render(request, 'Management/edit_front_report.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['FLLS', 'MANAGEMENT', 'MANAGEMENT_RUNYI', ])
def Runyi_Report(request, user):
    customer = Customer.objects.get(user=user)
    if customer.staff_created == False:
        messages.error(request, 'please update your profile to create report')
        return redirect('management_dashboard', user)
    if request.method == 'POST' and 'btn_save' in request.POST:        
        runyi_form = RUNYI_Form(request.POST)
        if runyi_form.is_valid():
            instance = runyi_form.save(commit=False)
            instance.customer = customer
            instance.Categoty = 'RUNYI'
            instance.save()

            hashids = Hashids( settings.MANAGEMENT, 5, settings.MANAGEMENT2)
            hashing_the_id = hashids.encode(instance.id)
            customer.office_report_set.filter(id = instance.id).update(ticket_num = hashing_the_id)
            messages.warning(request, "Your Report has been created, Look below to view active report")
            return redirect ('management_dashboard', user)

    elif request.method == 'POST' and 'btn_submit' in request.POST:
        runyi_form = RUNYI_Form(request.POST)
        if runyi_form.is_valid():
            instance = runyi_form.save(commit=False)
            instance.customer = customer
            instance.Categoty = 'RUNYI'                      
            instance.for_chairman_manager = True
            instance.for_manager_FLM = True
            instance.for_operation = True
            instance.for_runyi = True
            instance.save()

            hashids = Hashids( settings.MANAGEMENT, 5, settings.MANAGEMENT2)
            hashing_the_id = hashids.encode(instance.id)
            customer.office_report_set.filter(id = instance.id).update(ticket_num = hashing_the_id) 

            #email_list = ['festybaba80@gmail.com', 'usuugwo@gmail.com']
           # Staff_Name = instance.customer.first_name
            #Notification_email(email_list, Staff_Name)           
            messages.success(request, f"Your report has been submitted successfully")
            return redirect('management_dashboard', user)
    else:
        runyi_form = RUNYI_Form()

    context = {
        'runyi_form': runyi_form,
        'customer':customer,
    }
    return render(request, 'Management/Runyi_report.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['FLLS', 'MANAGEMENT', 'MANAGEMENT_RUNYI', ])
def Edit_Runyi_Report(request, pk):
    customer = Customer.objects.get(user= request.user)
    runyi_report = OFFICE_REPORT.objects.get(id = pk)
    if request.method == 'POST' and 'btn_save' in request.POST:        
        runyi_form =  RUNYI_Form(request.POST, instance= runyi_report)
        if runyi_form.is_valid():
            instance = runyi_form.save(commit=False)
            instance.save()
            
            messages.warning(request, "Saved successfully")
            return redirect ('management_dashboard', request.user.pk)

    elif request.method == 'POST' and 'btn_submit' in request.POST:
        runyi_form = RUNYI_Form(request.POST, instance= runyi_report)
        if runyi_form.is_valid():
            instance = runyi_form.save(commit=False)                                  
            instance.for_chairman_manager = True
            instance.for_manager_FLM = True
            instance.for_operation = True
            instance.save()           

            #email_list = ['festybaba80@gmail.com', 'usuugwo@gmail.com']
           # Staff_Name = instance.customer.first_name
            #Notification_email(email_list, Staff_Name) 
            messages.success(request, f"Your report has been submitted successfully")
            return redirect('management_dashboard', request.user.pk)
    else:
        runyi_form = RUNYI_Form(instance = runyi_report)

    context = {
        'runyi_form': runyi_form,
        'customer': customer,
    }
    return render(request, 'Management/edit_runyi_report.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['FLLS', 'IWH',])
def IWH_Report(request, user):
    customer = Customer.objects.get(user=user)
    if customer.staff_created == False:
        messages.error(request, 'please update your profile to create report')
        return redirect('management_dashboard', user)
    if request.method == 'POST' and 'btn_save' in request.POST:        
        iwh_form = IWH_Form(request.POST)
        if iwh_form.is_valid():
            instance = iwh_form.save(commit=False)
            instance.customer = customer
            instance.Categoty = 'IWH'
            instance.save()

            hashids = Hashids( settings.MANAGEMENT, 5, settings.MANAGEMENT2)
            hashing_the_id = hashids.encode(instance.id)
            customer.office_report_set.filter(id = instance.id).update(ticket_num = hashing_the_id)
            messages.warning(request, "Your Report has been created, Look below to view active report")
            return redirect ('management_dashboard', user)

    elif request.method == 'POST' and 'btn_submit' in request.POST:
        iwh_form = IWH_Form(request.POST)
        if iwh_form.is_valid():
            instance = iwh_form.save(commit=False)
            instance.customer = customer
            instance.Categoty = 'IWH'                 
            instance.for_admin = True
            instance.for_operation = True            
            instance.for_chairman_manager = True
            instance.for_manager_FLM = True
            instance.save()

            hashids = Hashids( settings.MANAGEMENT, 5, settings.MANAGEMENT2)
            hashing_the_id = hashids.encode(instance.id)
            customer.office_report_set.filter(id = instance.id).update(ticket_num = hashing_the_id) 

            #email_list = ['festybaba80@gmail.com', 'usuugwo@gmail.com']
           # Staff_Name = instance.customer.first_name
            #Notification_email(email_list, Staff_Name)           
            messages.success(request, f"Your report has been submitted successfully")
            return redirect('management_dashboard', user)
    else:
        iwh_form = IWH_Form()

    context = {
        'iwh_form': iwh_form,
        'customer':customer,
    }
    return render(request, 'Management/IWH_report.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['FLLS', 'IWH',])
def Edit_IWH_Report(request, pk):
    customer = Customer.objects.get(user= request.user)
    IWH_report = customer.office_report_set.get(id = pk)
    if request.method == 'POST' and 'btn_save' in request.POST:        
        iwh_form =  IWH_Form(request.POST, instance= IWH_report)
        if iwh_form.is_valid():
            instance = iwh_form.save(commit=False)
            instance.save()
            messages.warning(request, "Saved successfully")
            return redirect ('management_dashboard', request.user.pk)

    elif request.method == 'POST' and 'btn_submit' in request.POST:
        iwh_form = IWH_Form(request.POST, instance= IWH_report)
        if iwh_form.is_valid():
            instance = iwh_form.save(commit=False)                                   
            instance.for_admin = True
            instance.for_operation = True            
            instance.for_chairman_manager = True
            instance.for_manager_FLM = True
            instance.save()

            #email_list = ['festybaba80@gmail.com', 'usuugwo@gmail.com']
           # Staff_Name = instance.customer.first_name
            #Notification_email(email_list, Staff_Name)
            messages.success(request, f"Your report has been submitted successfully")
            return redirect('management_dashboard', request.user.pk)
    else:
        iwh_form = IWH_Form(instance = IWH_report)

    context = {
        'iwh_form': iwh_form,
        'customer':customer,
    }
    return render(request, 'Management/edit_iwh_report.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['FLLS', 'TANK',])
def TANK_FARM_Report(request, user):
    customer = Customer.objects.get(user=user)
    if customer.staff_created == False:
        messages.error(request, 'please update your profile to create report')
        return redirect('management_dashboard', user)
    if request.method == 'POST' and 'btn_save' in request.POST:
        Tank_Farm_form = TANK_Form(request.POST)
        if Tank_Farm_form.is_valid():
            instance = Tank_Farm_form.save(commit=False)
            instance.customer = customer
            instance.Categoty = 'Tank Farm'
            instance.save()

            hashids = Hashids( settings.MANAGEMENT, 5, settings.MANAGEMENT2)
            hashing_the_id = hashids.encode(instance.id)
            customer.office_report_set.filter(id = instance.id).update(ticket_num = hashing_the_id)
            messages.warning(request, "Your Report has been created, Look below to view active report")
            return redirect ('management_dashboard', user)

    elif request.method == 'POST' and 'btn_submit' in request.POST:
        Tank_Farm_form = TANK_Form(request.POST)
        if Tank_Farm_form.is_valid():
            instance = Tank_Farm_form.save(commit=False)
            instance.customer = customer
            instance.Categoty = 'Tank Farm'
            instance.for_chairman_manager = True
            instance.for_manager_FLM = True
            instance.save()

            hashids = Hashids( settings.MANAGEMENT, 5, settings.MANAGEMENT2)
            hashing_the_id = hashids.encode(instance.id)
            customer.office_report_set.filter(id = instance.id).update(ticket_num = hashing_the_id)  

            #email_list = ['festybaba80@gmail.com', 'usuugwo@gmail.com']
           # Staff_Name = instance.customer.first_name
            #Notification_email(email_list, Staff_Name)          
            messages.success(request, f"Your report has been submitted successfully")            
            return redirect('management_dashboard', user)
    else:
        Tank_Farm_form = TANK_Form()

    context = {
        'Tank_Farm_form': Tank_Farm_form,
        'customer':customer,
    }
    return render(request, 'Management/Tank_Farm_report.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['FLLS', 'TANK',])
def Edit_Tank_Farm_Report(request, pk):
    customer = Customer.objects.get(user= request.user)
    Tank_Farm_Report = customer.office_report_set.get(id = pk)
    if request.method == 'POST' and 'btn_save' in request.POST:        
        Tank_Farm_form =  TANK_Form(request.POST, instance= Tank_Farm_Report)
        if Tank_Farm_form.is_valid():
            instance = Tank_Farm_form.save(commit=False)
            instance.save()
            messages.warning(request, "Saved successfully")
            return redirect ('management_dashboard', request.user.pk)

    elif request.method == 'POST' and 'btn_submit' in request.POST:
        Tank_Farm_form = TANK_Form(request.POST, instance= Tank_Farm_Report)
        if Tank_Farm_form.is_valid():
            instance = Tank_Farm_form.save(commit=False)                                   
            instance.for_chairman_manager = True
            instance.for_manager_FLM = True       
            instance.save()

            #email_list = ['festybaba80@gmail.com', 'usuugwo@gmail.com']
           # Staff_Name = instance.customer.first_name
            #Notification_email(email_list, Staff_Name)

            messages.success(request, f"Your report has been submitted successfully")
            return redirect('management_dashboard', request.user.pk)
    else:
        Tank_Farm_form = TANK_Form(instance = Tank_Farm_Report)

    context = {
        'Tank_Farm_form': Tank_Farm_form,
        'customer':customer,
    }    
    return render(request, 'Management/edit_TankForm_report.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['FLLS', 'MANAGEMENT', 'MANAGEMENT_MANAGER',])
def Manager_Report(request, user):
    customer = Customer.objects.get(user=user)
    if customer.staff_created == False:
        messages.error(request, 'please update your profile to create report')
        return redirect('management_dashboard', user)
    if request.method == 'POST' and 'btn_save' in request.POST:        
        manager_form = Manager_FLLS_report_Form(request.POST)
        if manager_form.is_valid():
            instance = manager_form.save(commit=False)
            instance.customer = customer
            instance.Categoty = 'MANAGER'
            instance.save()

            hashids = Hashids( settings.MANAGEMENT, 5, settings.MANAGEMENT2)
            hashing_the_id = hashids.encode(instance.id)
            customer.office_report_set.filter(id = instance.id).update(ticket_num = hashing_the_id)

            messages.warning(request, "Your Report has been created, Look below to view active report")
            return redirect ('management_dashboard', user)

    elif request.method == 'POST' and 'btn_submit' in request.POST:
        manager_form = Manager_FLLS_report_Form(request.POST)
        if manager_form.is_valid():
            instance = manager_form.save(commit=False)
            instance.customer = customer
            instance.Categoty = 'MANAGER'                      
            instance.for_admin = True
            instance.for_operation = True
            instance.for_runyi = True        
            instance.save()

            hashids = Hashids( settings.MANAGEMENT, 5, settings.MANAGEMENT2)
            hashing_the_id = hashids.encode(instance.id)
            customer.office_report_set.filter(id = instance.id).update(ticket_num = hashing_the_id)  

            #email_list = ['krischukwuka@gmail.com', 'borowasborn@gmail.com', 'runyi4ojomo@gmail.com', 'usuugwo@gmail.com']
           # Staff_Name = instance.customer.first_name
            #Notification_email(email_list, Staff_Name)        

            messages.success(request, f"Your report has been submitted successfully")
            return redirect('management_dashboard', user)
    else:
        manager_form = Manager_FLLS_report_Form()

    context = {
        'manager_form': manager_form,
        'customer':customer,
    }
    return render(request, 'Management/Manager_report.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['FLLS', 'MANAGEMENT', 'MANAGEMENT_MANAGER',])
def Edit_Manager_Report(request, pk):
    customer = Customer.objects.get(user= request.user)
    FLLS_Report = customer.office_report_set.get(id = pk)
    if request.method == 'POST' and 'btn_save' in request.POST:        
        manager_form = Manager_FLLS_report_Form(request.POST, instance= FLLS_Report)
        if manager_form.is_valid():
            instance = manager_form.save(commit=False)
            instance.save()
            messages.warning(request, "Saved successfully")
            return redirect ('management_dashboard', request.user.pk)

    elif request.method == 'POST' and 'btn_submit' in request.POST:
        manager_form = Manager_FLLS_report_Form(request.POST, instance= FLLS_Report)
        if manager_form.is_valid():
            instance = manager_form.save(commit=False)                       
            instance.for_mangerFLLS = True
            instance.for_admin = True
            instance.for_operation = True
            instance.for_runyi = True                
            instance.save()

            #email_list = ['krischukwuka@gmail.com', 'borowasborn@gmail.com', 'runyi4ojomo@gmail.com', 'usuugwo@gmail.com']
           # Staff_Name = instance.customer.first_name
            #Notification_email(email_list, Staff_Name)  
            messages.success(request, f"Your report has been submitted successfully")
            return redirect('management_dashboard', request.user.pk)
    else:
        manager_form = Manager_FLLS_report_Form(instance = FLLS_Report)

    context = {
        'manager_form': manager_form,
        'customer':customer,
    }    
    return render(request, 'Management/edit_manager_report.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['FLLS', 'COMMERCIAL', 'admin',])
def Commercial_Report(request, user):
    customer = Customer.objects.get(user=user)
    if customer.staff_created == False:
        messages.error(request, 'Please update your profile to create report')
        return redirect('management_dashboard', user)
    if request.method == 'POST' and 'btn_save' in request.POST:        
        commercial_form = Commercial_report_Form(request.POST)
        if commercial_form.is_valid():
            instance = commercial_form.save(commit=False)
            instance.customer = customer
            instance.Categoty = 'COMMERCIAL'
            instance.save()

            hashids = Hashids( settings.MANAGEMENT, 5, settings.MANAGEMENT2)
            hashing_the_id = hashids.encode(instance.id)
            customer.office_report_set.filter(id = instance.id).update(ticket_num = hashing_the_id)

            messages.warning(request, "Your Report has been created, Look below to view active report")
            return redirect ('management_dashboard', user)

    elif request.method == 'POST' and 'btn_submit' in request.POST:
        commercial_form = Commercial_report_Form(request.POST)
        if commercial_form.is_valid():
            instance = commercial_form.save(commit=False)
            instance.customer = customer
            instance.Categoty = 'COMMERCIAL'                      
            instance.for_chairman_manager = True
            instance.for_manager_FLM = True
            instance.for_operation = True
            instance.for_runyi = True        
            instance.save()

            hashids = Hashids( settings.MANAGEMENT, 5, settings.MANAGEMENT2)
            hashing_the_id = hashids.encode(instance.id)
            customer.office_report_set.filter(id = instance.id).update(ticket_num = hashing_the_id)  

            email_list = ['festybaba80@gmail.com', 'borowasborn@gmail.com', 'runyi4ojomo@gmail.com', 'usuugwo@gmail.com']
            Staff_Name = instance.customer.first_name
            Notification_email(email_list, Staff_Name)        

            messages.success(request, f"Your report has been submitted successfully")
            return redirect('management_dashboard', user)
    else:
        commercial_form = Commercial_report_Form()

    context = {
        'commercial_form': commercial_form,
        'customer':customer,
    }
    return render(request, 'Management/Commercial_report.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['FLLS', 'COMMERCIAL', 'admin',])
def Edit_Commercial_Report(request, pk):
    customer = Customer.objects.get(user= request.user)
    FLLS_Report = customer.office_report_set.get(id = pk)
    if request.method == 'POST' and 'btn_save' in request.POST:        
        commercial_form = Commercial_report_Form(request.POST, instance= FLLS_Report)
        if commercial_form.is_valid():
            instance = commercial_form.save(commit=False)
            instance.save()
            messages.warning(request, "Saved")
            return redirect ('management_dashboard', request.user.pk)

    elif request.method == 'POST' and 'btn_submit' in request.POST:
        commercial_form = Commercial_report_Form(request.POST, instance= FLLS_Report)
        if commercial_form.is_valid():
            instance = commercial_form.save(commit=False)                       
            instance.for_chairman_manager = True
            instance.for_manager_FLM = True
            instance.for_operation = True
            instance.for_runyi = True  
            instance.save()

            email_list = ['festybaba80@gmail.com', 'borowasborn@gmail.com', 'runyi4ojomo@gmail.com', 'usuugwo@gmail.com']
            Staff_Name = instance.customer.first_name
            Notification_email(email_list, Staff_Name)  
            messages.success(request, f"Your report has been submitted successfully")
            return redirect('management_dashboard', request.user.pk)
    else:
        commercial_form = Commercial_report_Form(instance = FLLS_Report)

    context = {
        'commercial_form': commercial_form,
        'customer':customer,
    }
    return render(request, 'Management/edit_commercial_report.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['FLLS', 'MANAGEMENT_ADMIN', 'admin',])
def Admin_Report(request, user):
    customer = Customer.objects.get(user=user)
    if customer.staff_created == False:
        messages.error(request, 'Please update your profile to create report')
        return redirect('management_dashboard', user)
    if request.method == 'POST' and 'btn_save' in request.POST:        
        admin_form = Admin_report_form(request.POST)
        if admin_form.is_valid():
            instance = admin_form.save(commit=False)
            instance.customer = customer
            instance.Categoty = 'ADMIN'
            instance.save()

            hashids = Hashids( settings.MANAGEMENT, 5, settings.MANAGEMENT2)
            hashing_the_id = hashids.encode(instance.id)
            customer.office_report_set.filter(id = instance.id).update(ticket_num = hashing_the_id)

            messages.warning(request, "Your Report has been created, Look below to view active report")
            return redirect ('management_dashboard', user)

    elif request.method == 'POST' and 'btn_submit' in request.POST:
        admin_form = Admin_report_form(request.POST)
        if admin_form.is_valid():
            instance = admin_form.save(commit=False)
            instance.customer = customer
            instance.Categoty = 'ADMIN'                      
            instance.for_chairman_manager = True
            instance.for_manager_FLM = True
            instance.for_operation = True
            instance.for_runyi = True        
            instance.save()

            hashids = Hashids( settings.MANAGEMENT, 5, settings.MANAGEMENT2)
            hashing_the_id = hashids.encode(instance.id)
            customer.office_report_set.filter(id = instance.id).update(ticket_num = hashing_the_id)  

            #email_list = ['festybaba80@gmail.com', 'borowasborn@gmail.com', 'runyi4ojomo@gmail.com', 'usuugwo@gmail.com']
            #Staff_Name = instance.customer.first_name
            #Notification_email(email_list, Staff_Name)        

            messages.success(request, f"Your report has been submitted successfully")
            return redirect('management_dashboard', user)
    else:
        admin_form = Admin_report_form()

    context = {
        'admin_form': admin_form,
        'customer':customer,
    }
    return render(request, 'Management/Admin_report.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['FLLS', 'MANAGEMENT_ADMIN',])
def Edit_admin_Report(request, pk):
    customer = Customer.objects.get(user= request.user)
    FLLS_Report = customer.office_report_set.get(id = pk)
    if request.method == 'POST' and 'btn_save' in request.POST:        
        admin_form = Admin_report_form(request.POST, instance= FLLS_Report)
        if admin_form.is_valid():
            instance = admin_form.save(commit=False)
            instance.save()
            messages.warning(request, "Saved")
            return redirect ('management_dashboard', request.user.pk)

    elif request.method == 'POST' and 'btn_submit' in request.POST:
        admin_form = Admin_report_form(request.POST, instance= FLLS_Report)
        if admin_form.is_valid():
            instance = admin_form.save(commit=False)                       
            instance.for_chairman_manager = True
            instance.for_manager_FLM = True
            instance.for_operation = True
            instance.for_runyi = True  
            instance.save()

            #email_list = ['festybaba80@gmail.com', 'borowasborn@gmail.com', 'runyi4ojomo@gmail.com', 'usuugwo@gmail.com']
            #Staff_Name = instance.customer.first_name
            #Notification_email(email_list, Staff_Name)  
            messages.success(request, f"Your report has been submitted successfully")
            return redirect('management_dashboard', request.user.pk)
    else:
        admin_form = Admin_report_form(instance = FLLS_Report)

    context = {
        'admin_form': admin_form,
        'customer':customer,
    }
    return render(request, 'Management/edit_admin_report.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['FLLS', 'COMMERCIAL', 'admin',])
def Account_Report(request, user):
    customer = Customer.objects.get(user=user)
    if customer.staff_created == False:
        messages.error(request, 'Please update your profile to create report')
        return redirect('management_dashboard', user)
    if request.method == 'POST' and 'btn_save' in request.POST:        
        account_form = Account_report_form(request.POST)
        if account_form.is_valid():
            instance = account_form.save(commit=False)
            instance.customer = customer
            instance.Categoty = 'ACCOUNT'
            instance.save()

            hashids = Hashids( settings.MANAGEMENT, 5, settings.MANAGEMENT2)
            hashing_the_id = hashids.encode(instance.id)
            customer.office_report_set.filter(id = instance.id).update(ticket_num = hashing_the_id)

            messages.warning(request, "Your Report has been created, Look below to view active report")
            return redirect ('management_dashboard', user)

    elif request.method == 'POST' and 'btn_submit' in request.POST:
        account_form = Account_report_form(request.POST)
        if account_form.is_valid():
            instance = account_form.save(commit=False)
            instance.customer = customer
            instance.Categoty = 'ACCOUNT'                      
            instance.for_chairman_manager = True
            instance.for_manager_FLM = True           
            instance.for_runyi = True        
            instance.save()

            hashids = Hashids( settings.MANAGEMENT, 5, settings.MANAGEMENT2)
            hashing_the_id = hashids.encode(instance.id)
            customer.office_report_set.filter(id = instance.id).update(ticket_num = hashing_the_id)  

            #email_list = ['festybaba80@gmail.com', 'runyi4ojomo@gmail.com', 'idminat@gmail.com', 'usuugwo@gmail.com']
            #Staff_Name = instance.customer.first_name
            #Notification_email(email_list, Staff_Name)        

            messages.success(request, f"Your report has been submitted successfully")
            return redirect('management_dashboard', user)
    else:
        account_form = Account_report_form()

    context = {
        'account_form': account_form,
        'customer':customer,
    }
    return render(request, 'Management/Account_report.html', context)    

@login_required(login_url='login')
@allowed_user(allowed_roles=['FLLS', 'COMMERCIAL', 'admin',])
def Edit_account_Report(request, pk):
    customer = Customer.objects.get(user= request.user)
    FLLS_Report = customer.office_report_set.get(id = pk)
    if request.method == 'POST' and 'btn_save' in request.POST:        
        account_form = Account_report_form(request.POST, instance= FLLS_Report)
        if account_form.is_valid():
            instance = account_form.save(commit=False)
            instance.save()
            messages.warning(request, "Saved")
            return redirect ('management_dashboard', request.user.pk)

    elif request.method == 'POST' and 'btn_submit' in request.POST:
        account_form = Account_report_form(request.POST, instance= FLLS_Report)
        if account_form.is_valid():
            instance = account_form.save(commit=False)                       
            instance.for_chairman_manager = True
            instance.for_manager_FLM = True            
            instance.for_runyi = True  
            instance.save()

            #email_list = ['festybaba80@gmail.com', 'runyi4ojomo@gmail.com', 'idminat@gmail.com', 'usuugwo@gmail.com']
            #Staff_Name = instance.customer.first_name
            #Notification_email(email_list, Staff_Name)  
            messages.success(request, f"Your report has been submitted successfully")
            return redirect('management_dashboard', request.user.pk)
    else:
        account_form = Account_report_form(instance = FLLS_Report)

    context = {
        'account_form': account_form,
        'customer':customer,
    }
    return render(request, 'Management/edit_account_report.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['FLLS', 'COMMERCIAL', 'admin',])
def MaintenanceAccount_Report(request, user):
    customer = Customer.objects.get(user=user)
    if customer.staff_created == False:
        messages.error(request, 'Please update your profile to create report')
        return redirect('management_dashboard', user)
    if request.method == 'POST' and 'btn_save' in request.POST:        
        maintenace_form = Maintenance_report_form(request.POST)
        if maintenace_form.is_valid():
            instance = maintenace_form.save(commit=False)
            instance.customer = customer
            instance.Categoty = 'MAINTENANCE'
            instance.save()

            hashids = Hashids( settings.MANAGEMENT, 5, settings.MANAGEMENT2)
            hashing_the_id = hashids.encode(instance.id)
            customer.office_report_set.filter(id = instance.id).update(ticket_num = hashing_the_id)

            messages.warning(request, "Your Report has been created, Look below to view active report")
            return redirect ('management_dashboard', user)

    elif request.method == 'POST' and 'btn_submit' in request.POST:
        maintenace_form = Maintenance_report_form(request.POST)
        if maintenace_form.is_valid():
            instance = maintenace_form.save(commit=False)
            instance.customer = customer
            instance.Categoty = 'MAINTENANCE'
            instance.for_chairman_manager = True
            instance.for_manager_FLM = True 
            instance.for_operation = True          
            instance.for_runyi = True        
            instance.save()

            hashids = Hashids( settings.MANAGEMENT, 5, settings.MANAGEMENT2)
            hashing_the_id = hashids.encode(instance.id)
            customer.office_report_set.filter(id = instance.id).update(ticket_num = hashing_the_id)  

            #email_list = ['festybaba80@gmail.com', 'runyi4ojomo@gmail.com', 'idminat@gmail.com', 'usuugwo@gmail.com']
            #Staff_Name = instance.customer.first_name
            #Notification_email(email_list, Staff_Name)        

            messages.success(request, f"Your report has been submitted successfully")
            return redirect('management_dashboard', user)
    else:
        maintenace_form = Maintenance_report_form()

    context = {
        'maintenace_form': maintenace_form,
        'customer':customer,
    }
    return render(request, 'Management/Maintenance_report.html', context)    

@login_required(login_url='login')
@allowed_user(allowed_roles=['FLLS', 'COMMERCIAL', 'admin',])
def Edit_maintenance_Report(request, pk):
    customer = Customer.objects.get(user= request.user)
    FLLS_Report = customer.office_report_set.get(id = pk)
    if request.method == 'POST' and 'btn_save' in request.POST:        
        maintenace_form = Maintenance_report_form(request.POST, instance= FLLS_Report)
        if maintenace_form.is_valid():
            instance = maintenace_form.save(commit=False)
            instance.save()
            messages.warning(request, "Saved")
            return redirect ('management_dashboard', request.user.pk)

    elif request.method == 'POST' and 'btn_submit' in request.POST:
        maintenace_form = Maintenance_report_form(request.POST, instance= FLLS_Report)
        if maintenace_form.is_valid():
            instance = maintenace_form.save(commit=False)                       
            instance.for_chairman_manager = True
            instance.for_manager_FLM = True            
            instance.for_runyi = True
            instance.for_operation = True
            instance.save()

            #email_list = ['festybaba80@gmail.com', 'runyi4ojomo@gmail.com', 'idminat@gmail.com', 'usuugwo@gmail.com']
            #Staff_Name = instance.customer.first_name
            #Notification_email(email_list, Staff_Name)  
            messages.success(request, f"Your report has been submitted successfully")
            return redirect('management_dashboard', request.user.pk)
    else:
        maintenace_form = Maintenance_report_form(instance = FLLS_Report)

    context = {
        'maintenace_form': maintenace_form,
        'customer':customer,
    }
    return render(request, 'Management/edit_maintenance_report.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['FLLS', 'COMMERCIAL', 'admin',])
def PortHatcourt_office_Report(request, user):
    customer = Customer.objects.get(user=user)
    if customer.staff_created == False:
        messages.error(request, 'Please update your profile to create report')
        return redirect('management_dashboard', user)
    if request.method == 'POST' and 'btn_save' in request.POST:        
        ph_report = PH_report_form(request.POST)
        if ph_report.is_valid():
            instance = ph_report.save(commit=False)
            instance.customer = customer
            instance.Categoty = 'MANAGER_PH'
            instance.save()

            hashids = Hashids( settings.MANAGEMENT, 5, settings.MANAGEMENT2)
            hashing_the_id = hashids.encode(instance.id)
            customer.office_report_set.filter(id = instance.id).update(ticket_num = hashing_the_id)

            messages.warning(request, "Your Report has been created, Look below to view active report")
            return redirect ('management_dashboard', user)

    elif request.method == 'POST' and 'btn_submit' in request.POST:
        ph_report = PH_report_form(request.POST)
        if ph_report.is_valid():
            instance = ph_report.save(commit=False)
            instance.customer = customer
            instance.Categoty = 'MANAGER_PH'
            instance.for_chairman_manager = True
            instance.for_manager_FLM = True 
            instance.for_operation = True          
            instance.for_runyi = True 
            instance.for_mangerFLLS = True    
            instance.save()

            hashids = Hashids( settings.MANAGEMENT, 5, settings.MANAGEMENT2)
            hashing_the_id = hashids.encode(instance.id)
            customer.office_report_set.filter(id = instance.id).update(ticket_num = hashing_the_id)  

            #email_list = ['festybaba80@gmail.com', 'runyi4ojomo@gmail.com', 'borowasborn@gmail.com', 'idminat@gmail.com', 'usuugwo@gmail.com']
            #Staff_Name = instance.customer.first_name
            #Notification_email(email_list, Staff_Name)  

            messages.success(request, f"Your report has been submitted successfully")
            return redirect('management_dashboard', user)
    else:
        ph_report = PH_report_form()

    context = {
        'ph_report': ph_report,
        'customer':customer,
    }
    return render(request, 'Management/PH_report.html', context)    


@login_required(login_url='login')
@allowed_user(allowed_roles=['FLLS', 'COMMERCIAL', 'admin',])
def Edit_portharcourt_office_Report(request, pk):
    customer = Customer.objects.get(user= request.user)
    FLLS_Report = customer.office_report_set.get(id = pk)
    if request.method == 'POST' and 'btn_save' in request.POST:        
        ph_report = PH_report_form(request.POST, instance= FLLS_Report)
        if ph_report.is_valid():
            instance = ph_report.save(commit=False)
            instance.save()
            messages.warning(request, "Saved")
            return redirect ('management_dashboard', request.user.pk)

    elif request.method == 'POST' and 'btn_submit' in request.POST:
        ph_report = PH_report_form(request.POST, instance= FLLS_Report)
        if ph_report.is_valid():
            instance = ph_report.save(commit=False)                       
            instance.for_chairman_manager = True
            instance.for_manager_FLM = True 
            instance.for_operation = True          
            instance.for_runyi = True 
            instance.for_mangerFLLS = True   
            instance.save()

            #email_list = ['festybaba80@gmail.com', 'runyi4ojomo@gmail.com', 'borowasborn@gmail.com', 'idminat@gmail.com', 'usuugwo@gmail.com']
            #Staff_Name = instance.customer.first_name
            #Notification_email(email_list, Staff_Name)  
            messages.success(request, f"Your report has been submitted successfully")
            return redirect('management_dashboard', request.user.pk)
    else:
        ph_report = PH_report_form(instance = FLLS_Report)

    context = {
        'ph_report': ph_report,
        'customer':customer,
    }
    return render(request, 'Management/edit_ph_report.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=[
        'FLLS', 'MANAGEMENT', 'ICT',
        'MANAGEMENT_OPERATION', 'OPERATIONS',
        'FLM MANAGER', 'TANK', 'IWH', 'MANAGEMENT_RUNYI', 
        'MANAGEMENT_MANAGER', 'MANAGEMENT_CHAIRMAN', 
        'Marketing', 'Fleet Manager', 'Front Desk', 
        'MANAGEMENT_ADMIN',
        ])
def Status_History(request, user):
    customer = Customer.objects.get(user = user)
    all_fleet_report = customer.office_report_set.filter(for_mangerFLLS = True).filter( Categoty = 'Fleet')   
    all_operations_report = customer.office_report_set.filter(for_chairman_manager = True).filter( Categoty = 'Operations')    
    all_front_report = customer.office_report_set.filter(for_mangerFLLS = True).filter( Categoty = 'Front')   
    all_marketing_report = customer.office_report_set.filter(for_mangerFLLS = True).filter( Categoty = 'Market')  
    all_ict_report = customer.office_report_set.filter(for_mangerFLLS = True).filter( Categoty = 'ICT')    
    all_runyi_report = customer.office_report_set.filter(for_chairman_manager = True).filter( Categoty = 'RUNYI')    
    all_managers_report = customer.office_report_set.filter(for_runyi = True).filter( Categoty = 'MANAGER')    
    all_IWH_report = customer.office_report_set.filter(for_chairman_manager = True).filter( Categoty = 'IWH')    
    all_farm_tank_report = customer.office_report_set.filter(for_chairman_manager = True).filter( Categoty = 'Tank Farm')    
    all_commercial_report = customer.office_report_set.filter(for_chairman_manager = True).filter( Categoty = 'COMMERCIAL')    
    all_admin_report = customer.office_report_set.filter(for_chairman_manager = True).filter( Categoty = 'ADMIN')    
    all_maintainance_report = customer.office_report_set.filter(for_chairman_manager = True).filter( Categoty = 'MAINTENANCE')    
    all_account_report = customer.office_report_set.filter(for_chairman_manager = True).filter( Categoty = 'ACCOUNT')   
    all_PH_report = customer.office_report_set.filter(for_chairman_manager = True).filter( Categoty = 'MANAGER_PH')    
    
    context = {
        'all_fleet_report':all_fleet_report,
        'all_operations_report': all_operations_report,
        'all_front_desk_report': all_front_report,
        'all_marketing_report': all_marketing_report,
        'all_ict_report': all_ict_report,
        'customer':customer,
        'all_runyi_report': all_runyi_report,
        'all_managers_report':all_managers_report,
        'all_IWH_report':all_IWH_report,
        'all_farm_tank_report':all_farm_tank_report,
        'all_commercial_report': all_commercial_report,
        'all_admin_report': all_admin_report,
        'all_maintainance_report':all_maintainance_report,
        'all_account_report': all_account_report,
        'all_PH_report':all_PH_report,
    }
    return render(request, 'Management/Report_History.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=[
        'FLLS', 'MANAGEMENT', 'ICT',
        'MANAGEMENT_OPERATION', 'OPERATIONS',
        'FLM MANAGER', 'TANK', 'IWH', 'MANAGEMENT_RUNYI', 
        'MANAGEMENT_MANAGER', 'MANAGEMENT_CHAIRMAN', 
        'Marketing', 'Fleet Manager', 'Front Desk', 
        'MANAGEMENT_ADMIN',
        ])
def History_details(request, pk):
    customer = Customer.objects.get(user= request.user)
    report = customer.office_report_set.filter( id= pk)

    context = {
        'customer':customer,
        'report':report,
    }
    return render(request, 'Management/History_detail.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=[
        'FLLS', 'MANAGEMENT',
        'MANAGEMENT_OPERATION', 'OPERATIONS',
        'FLM MANAGER', 'MANAGEMENT_RUNYI', 
        'MANAGEMENT_MANAGER', 'MANAGEMENT_CHAIRMAN',          
        'MANAGEMENT_ADMIN',
        ])
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
    elif request.user.groups.filter(name = 'FLM MANAGER'):
        OFFICE_REPORT.objects.filter( id= pk).update(manager_flm_seen = True)   

    actual_form = OFFICE_REPORT.objects.get(id = pk)
    response_form = Manager_Response_Form()
    runyi_form = Runyi_Response_Form()
    response_form_operations = Operations_Response_Form()
    response_form_admin = Admin_Response_Form()
    response_form_chairman = Chairman_Response_Form()
    response_form_GGM = FLLM_Manager_Response_Form()


    if request.method == 'POST' and 'runyi' in request.POST:
        runyi_form  = Runyi_Response_Form(request.POST, instance = actual_form)
        if runyi_form.is_valid():
            runyi_form.save()
            messages.success(request, "Comment Sent")

    elif request.method == 'POST' and 'flls-manager' in request.POST:
        response_form = Manager_Response_Form(request.POST, instance = actual_form)
        if response_form.is_valid():
            response_form.save()
            messages.success(request, "Comment Sent")

    elif request.method == 'POST' and 'operations' in request.POST:
        response_form_operations = Operations_Response_Form(request.POST, instance = actual_form)
        if response_form_operations.is_valid():
            response_form_operations.save()
            messages.success(request, "Comment Sent")

    elif request.method == 'POST' and 'admin' in request.POST:
        response_form_admin = Admin_Response_Form(request.POST, instance = actual_form)
        if response_form_admin.is_valid():
            response_form_admin.save()  
            messages.success(request, "Comment Sent")

    elif request.method == 'POST' and 'chairman' in request.POST:
        response_form_chairman = Chairman_Response_Form(request.POST, instance = actual_form)
        if response_form_chairman.is_valid():
            response_form_chairman.save()   
            messages.success(request, "Comment Sent")

    elif request.method == 'POST' and 'flm-manager' in request.POST:
        response_form_GGM = FLLM_Manager_Response_Form(request.POST, instance = actual_form)
        if response_form_GGM.is_valid():
            response_form_GGM.save()    
            messages.success(request, "Comment Sent")

    context = {
        'customer':customer,
        'report':report,
        'runyi_form':runyi_form,
        'response_form':response_form,
        'response_form_operations':response_form_operations,
        'response_form_admin':response_form_admin,
        'response_form_chairman':response_form_chairman, 
        'response_form_GGM':response_form_GGM,
    }  
    return render(request, 'Management/History_details_management.html', context)

@login_required(login_url='login')
def Management_view(request, user):
    all_report = OFFICE_REPORT.objects.filter(submit = True)
    customer = Customer.objects.get(user = user)
    
    context = {
        'all_report': all_report,
        'customer':customer,
    }
    return render(request,'Management/management_view_report.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=[
        'FLLS', 'MANAGEMENT', 
        'MANAGEMENT_CHAIRMAN',        
        ])
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

@login_required(login_url='login')
@allowed_user(allowed_roles=[
        'FLLS', 'MANAGEMENT', 
        'MANAGEMENT_OPERATION', 'OPERATIONS',        
        ])
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

@login_required(login_url='login')
@allowed_user(allowed_roles=[
        'FLLS', 'MANAGEMENT',        
        'MANAGEMENT_ADMIN',
        ])
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

@login_required(login_url='login')
@allowed_user(allowed_roles=[
        'FLLS', 'MANAGEMENT',
        'MANAGEMENT_MANAGER',        
        ])
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

@login_required(login_url='login')
@allowed_user(allowed_roles=[
        'FLLS', 'MANAGEMENT', 
        'MANAGEMENT_RUNYI',        
        ])
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

@login_required(login_url='login')
@allowed_user(allowed_roles=[
        'FLLS', 'MANAGEMENT', 'FLM MANAGER', 
        ])
def FLM_Response(request, pk):
    customer = Customer.objects.get(user = request.user)
    actual_form = OFFICE_REPORT.objects.get(id = pk)
    if request.method == 'POST':
        response_form = FLLM_Manager_Response_Form(request.POST, instance = actual_form)
        if response_form.is_valid():
            instance = response_form.save()
            customer_name = instance.customer.first_name
            messages.success(request, f'Your response to {customer_name} has been sent')
            return redirect( 'management_list_details', pk)
    else:
        response_form = FLLM_Manager_Response_Form(instance = actual_form)

    context = {
        'response_form':response_form,
        'customer':customer,
        'actual_form':response_form,
    }
    return render(request, 'Management/fllm_response.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=[
        'FLLS', 'MANAGEMENT', 'MANAGEMENT_CHAIRMAN',                
        ])
def Chairman_report_list(request, user):
    customer = Customer.objects.get(user = user)
    
    for_chairman_GM = OFFICE_REPORT.objects.filter(for_chairman_manager = True)
    filter_name  = Staff_Name(request.GET, queryset=for_chairman_GM)
    for_chairman_GM = filter_name.qs

    paginator1 = Paginator(for_chairman_GM, 10)
    page = request.GET.get('page')
    page_obj = paginator1.get_page(page)
    context = {
        'for_chairman_GM':for_chairman_GM,
        'customer':customer,
        'filter_name':filter_name,
        'page_obj':page_obj,
    }
    return render(request, 'Management/chairman_view_list.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=[
        'FLLS', 'MANAGEMENT', 'MANAGEMENT_MANAGER'            
        ])
def FLLS_manager_report_list(request, user):
    customer = Customer.objects.get(user = user)    
    for_flls_manager = OFFICE_REPORT.objects.filter(for_mangerFLLS = True)
    filter_name  = Staff_Name(request.GET, queryset = for_flls_manager)
    for_flls_manager = filter_name.qs

    paginator1 = Paginator(for_flls_manager, 10)
    page = request.GET.get('page')
    page_obj = paginator1.get_page(page)
    context = {
        'for_flls_manager':for_flls_manager,
        'customer':customer,
        'filter_name':filter_name,
        'page_obj':page_obj,
    }
    return render(request, 'Management/flls_manager_view_list.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=[
        'FLLS', 'MANAGEMENT',        
        'FLM MANAGER',
        ])
def FLM_manager_report_list(request, user):
    customer = Customer.objects.get(user = user)
    
    for_flm_manager = OFFICE_REPORT.objects.filter(for_manager_FLM = True)
    filter_name  = Staff_Name(request.GET, queryset = for_flm_manager)
    for_flm_manager = filter_name.qs

    paginator1 = Paginator(for_flm_manager, 10)
    page = request.GET.get('page')
    page_obj = paginator1.get_page(page)
    context = {
        'for_flm_manager':for_flm_manager,
        'customer':customer,
        'filter_name':filter_name,
        'page_obj':page_obj,
    }
    return render(request, 'Management/flm_manager_view_list.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=[
        'FLLS', 'MANAGEMENT', 'MANAGEMENT_RUNYI', 
        ])
def Runyi_report_list(request, user):
    customer = Customer.objects.get(user = user)
    
    for_runyi = OFFICE_REPORT.objects.filter(for_runyi = True)
    filter_name  = Staff_Name(request.GET, queryset = for_runyi)
    for_runyi = filter_name.qs

    paginator1 = Paginator(for_runyi, 10)
    page = request.GET.get('page')
    page_obj = paginator1.get_page(page)
    context = {
        'for_runyi':for_runyi,
        'customer':customer,
        'filter_name':filter_name,
        'page_obj':page_obj,
    }
    return render(request, 'Management/runyi_view_list.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=[
        'FLLS', 'MANAGEMENT', 
        'MANAGEMENT_OPERATION', 'OPERATIONS',
        ])
def Operations_report_list(request, user):
    customer = Customer.objects.get(user = user)
    
    for_operations = OFFICE_REPORT.objects.filter(for_operation = True)
    filter_name  = Staff_Name(request.GET, queryset = for_operations)
    for_operations = filter_name.qs

    paginator1 = Paginator(for_operations, 10)
    page = request.GET.get('page')
    page_obj = paginator1.get_page(page)
    context = {
        'for_operations':for_operations,
        'customer':customer,
        'filter_name':filter_name,
        'page_obj':page_obj,
    }
    return render(request, 'Management/operations_view_list.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=[
        'FLLS', 'MANAGEMENT', 'MANAGEMENT_ADMIN',
        ])
def Admin_report_list(request, user):
    customer = Customer.objects.get(user = user)
    
    for_admin_list = OFFICE_REPORT.objects.filter(for_admin = True)
    filter_name  = Staff_Name(request.GET, queryset = for_admin_list)
    for_admin_list = filter_name.qs

    paginator1 = Paginator(for_admin_list, 10)
    page = request.GET.get('page')
    page_obj = paginator1.get_page(page)
    context = {
        'for_admin_list':for_admin_list,
        'customer':customer,
        'filter_name':filter_name,
        'page_obj':page_obj,
    }
    return render(request, 'Management/admin_view_list.html', context)    

