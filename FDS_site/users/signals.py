#signaling for new users profile
from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver 
from .models import Customer, Delivered, MakeRequest, MakeRequestCash, Shopping
import requests


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance) # we want to run everytime a user is created

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.customer.save()

        
@receiver(post_save, sender=Delivered)
def Delivered_signals(sender, instance, created, **kwargs):
    if created:
        customer =Customer.objects.get(pk=instance.customer.id )
        cus = customer.delivered_set.all()

        print(instance.order_id)
        customer.delivered_set.filter(order_id = instance.order_id).update(
                                title = 'Delivered!',
                                Message= f"Hello {instance.customer} Your parcel with the following refrence Number '{instance.order_id}' has been Delivered, Thanks for using our service.")


@receiver(post_save, sender=MakeRequest)
def adminNotification(sender, instance, created, **kwargs):
    if created:
        customer = Customer.objects.get(pk=instance.customer.id )
        customer.adminnotification_set.filter(order_id = instance.order_id)
                        
@receiver(post_save, sender=MakeRequestCash)
def adminNotificationCash(sender, instance, created, **kwargs):
    if created:
        customer = Customer.objects.get(pk=instance.customer.id )
        customer.adminnotification_set.filter(order_id = instance.order_id)
        

@receiver(post_save, sender=Shopping)
def adminNotificationShopping(sender, instance, created, **kwargs):
    if created:
        customer = Customer.objects.get(pk=instance.customer.id )
        customer.adminnotification_set.filter(order_id = instance.order_id)