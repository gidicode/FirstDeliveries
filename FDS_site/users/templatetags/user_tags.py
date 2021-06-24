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