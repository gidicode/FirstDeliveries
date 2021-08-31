from django.contrib import admin
from .models import *

admin.site.register(Customer) #registring model
admin.site.register(MakeRequest) 
admin.site.register(MakeRequestCash) 
admin.site.register(ForPayments) 
admin.site.register(Shopping) 
admin.site.register(Delivered) 
admin.site.register(adminNotification) 
admin.site.register(Anonymous) 
admin.site.register(Errand_service)
admin.site.register(Front_desk)