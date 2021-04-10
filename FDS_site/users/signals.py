#signaling for new users profile
from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver 
from .models import Customer


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance) # we want to run everytime a user is created

@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    instance.customer.save()

        
#instance is the user