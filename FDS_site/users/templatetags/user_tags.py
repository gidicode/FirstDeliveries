from django import template
from django.contrib.auth.models import Group 

register = template.Library() 

@register.filter(name='front_desk') 
def Front_Desk(user, Front_Desk):
    group = Group.objects.filter(name=Front_Desk)
    if group:
        group = group.first()
        return group in user.groups.all()
    else:
        return False

@register.filter(name='fleet') 
def Fleet_Manager(user, Fleet_Manager):
    group = Group.objects.filter(name=Fleet_Manager)
    if group:
        group = group.first()
        return group in user.groups.all()
    else:
        return False

@register.filter(name='cashier') 
def Cashier(user, Cashier):
    group = Group.objects.filter(name=Cashier)
    if group:
        group = group.first()
        return group in user.groups.all()
    else:
        return False
        
@register.filter(name='operations') 
def Operations(user, OPERATIONS):
    group = Group.objects.filter(name=OPERATIONS)
    if group:
        group = group.first()
        return group in user.groups.all()
    else:
        return False

@register.filter(name='Marketing') 
def Marketerting(user, Marketing):
    group = Group.objects.filter(name= Marketing)
    if group:
        group = group.first()
        return group in user.groups.all()
    else:
        return False

@register.filter(name='ICT') 
def ICT(user, ICT):
    group = Group.objects.filter(name=ICT)
    if group:
        group = group.first()
        return group in user.groups.all()
    else:
        return False

@register.filter(name='chairman') 
def Chairman_Group(user, MANAGEMENT_CHAIRMAN):
    group = Group.objects.filter(name= MANAGEMENT_CHAIRMAN)
    if group:
        group = group.first()
        return group in user.groups.all()
    else:
        return False

@register.filter(name='m_operation') 
def Manager_Operation(user, MANAGEMENT_OPERATION):
    group = Group.objects.filter(name= MANAGEMENT_OPERATION)
    if group:
        group = group.first()
        return group in user.groups.all()
    else:
        return False

@register.filter(name='m_manager') 
def Manager_FLLS(user, MANAGEMENT_MANAGER):
    group = Group.objects.filter(name= MANAGEMENT_MANAGER)
    if group:
        group = group.first()
        return group in user.groups.all()
    else:
        return False

@register.filter(name='m_runyi') 
def GM_Admin(user, MANAGEMENT_RUNYI):
    group = Group.objects.filter(name= MANAGEMENT_RUNYI)
    if group:
        group = group.first()
        return group in user.groups.all()
    else:
        return False

@register.filter(name='management') 
def Management(user, MANAGEMENT):
    group = Group.objects.filter(name= MANAGEMENT)
    if group:
        group = group.first()
        return group in user.groups.all()
    else:
        return False

@register.filter(name='admin') 
def Admin_Group(user, MANAGEMENT_ADMIN):
    group = Group.objects.filter(name= MANAGEMENT_ADMIN)
    if group:
        group = group.first()
        return group in user.groups.all()
    else:
        return False

@register.filter(name='IWHADMIN') 
def IWH_GROUP(user, IWH):
    group = Group.objects.filter(name= IWH)
    if group:
        group = group.first()
        return group in user.groups.all()
    else:
        return False

@register.filter(name='FARM_TANK') 
def FARM_TANK_GROUP(user, TANK):
    group = Group.objects.filter(name= TANK)
    if group:
        group = group.first()
        return group in user.groups.all()
    else:
        return False

@register.filter(name='flm_manager') 
def FLM_MANAGER_GROUP(user, FLM_MANAGER):
    group = Group.objects.filter(name = FLM_MANAGER)
    if group:
        group = group.first()
        return group in user.groups.all()
    else:
        return False

@register.filter(name='flls_team') 
def FLLS_GROUP(user, FLLS):
    group = Group.objects.filter(name = FLLS)
    if group:
        group = group.first()
        return group in user.groups.all()
    else:
        return False       

@register.filter(name='COMMERCIAL') 
def COMMERCIAL_GROUP(user, COMMERCIAL):
    group = Group.objects.filter(name = COMMERCIAL)
    if group:
        group = group.first()
        return group in user.groups.all()
    else:
        return False    

@register.filter(name='MAINTENANCE') 
def MAINTENANCE_GROUP(user, MAINTENANCE):
    group = Group.objects.filter(name = MAINTENANCE)
    if group:
        group = group.first()
        return group in user.groups.all()
    else:
        return False   

@register.filter(name='MANAGER_PH') 
def PORTHARCOURT_GROUP(user, MANAGER_PH):
    group = Group.objects.filter(name = MANAGER_PH)
    if group:
        group = group.first()
        return group in user.groups.all()
    else:
        return False    

@register.filter(name='ACCOUNT') 
def ACCOUNT_GROUP(user, ACCOUNT):
    group = Group.objects.filter(name = ACCOUNT)
    if group:
        group = group.first()
        return group in user.groups.all()
    else:
        return False 

@register.filter(name='Affiliate_admin') 
def AFFILIATE_GROUP(user, Affiliate_admin):
    group = Group.objects.filter(name = Affiliate_admin)
    if group:
        group = group.first()
        return group in user.groups.all()
    else:
        return False 
    
    



