from django import template
from django.contrib.auth.models import Group 

register = template.Library() 

@register.filter(name='front_desk') 
def has_group(user, Front_Desk):
    group = Group.objects.filter(name=Front_Desk)
    if group:
        group = group.first()
        return group in user.groups.all()
    else:
        return False

@register.filter(name='fleet') 
def has_group(user, Fleet_Manager):
    group = Group.objects.filter(name=Fleet_Manager)
    if group:
        group = group.first()
        return group in user.groups.all()
    else:
        return False

@register.filter(name='cashier') 
def has_group(user, Cashier):
    group = Group.objects.filter(name=Cashier)
    if group:
        group = group.first()
        return group in user.groups.all()
    else:
        return False
        
@register.filter(name='operations') 
def has_group(user, OPERATIONS):
    group = Group.objects.filter(name=OPERATIONS)
    if group:
        group = group.first()
        return group in user.groups.all()
    else:
        return False

@register.filter(name='Marketing') 
def has_group(user, Marketing):
    group = Group.objects.filter(name= Marketing)
    if group:
        group = group.first()
        return group in user.groups.all()
    else:
        return False

@register.filter(name='ICT') 
def has_group(user, ICT):
    group = Group.objects.filter(name=ICT)
    if group:
        group = group.first()
        return group in user.groups.all()
    else:
        return False


@register.filter(name='chairman') 
def has_group(user, MANAGEMENT_CHAIRMAN):
    group = Group.objects.filter(name= MANAGEMENT_CHAIRMAN)
    if group:
        group = group.first()
        return group in user.groups.all()
    else:
        return False

@register.filter(name='m_operation') 
def has_group(user, MANAGEMENT_OPERATION):
    group = Group.objects.filter(name= MANAGEMENT_OPERATION)
    if group:
        group = group.first()
        return group in user.groups.all()
    else:
        return False

@register.filter(name='m_manager') 
def has_group(user, MANAGEMENT_MANAGER):
    group = Group.objects.filter(name= MANAGEMENT_MANAGER)
    if group:
        group = group.first()
        return group in user.groups.all()
    else:
        return False

@register.filter(name='m_runyi') 
def has_group(user, MANAGEMENT_RUNYI):
    group = Group.objects.filter(name= MANAGEMENT_RUNYI)
    if group:
        group = group.first()
        return group in user.groups.all()
    else:
        return False

@register.filter(name='management') 
def has_group(user, MANAGEMENT):
    group = Group.objects.filter(name= MANAGEMENT)
    if group:
        group = group.first()
        return group in user.groups.all()
    else:
        return False

@register.filter(name='admin') 
def has_group(user, MANAGEMENT_ADMIN):
    group = Group.objects.filter(name= MANAGEMENT_ADMIN)
    if group:
        group = group.first()
        return group in user.groups.all()
    else:
        return False

