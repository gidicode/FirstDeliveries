from django.contrib import admin
from .models import *

admin.site.register(Customer) #registring model
admin.site.register(MakeRequest) 
admin.site.register(MakeRequestCash) 
admin.site.register(ForPayments) 
admin.site.register(Shopping) 

