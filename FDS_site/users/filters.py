import django_filters
from django_filters import DateFilter

from.models import *

class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = MakeRequest
        fields =['reciever_name', 'status',]

class AdminFilter(django_filters.FilterSet):
    class Meta:
        model = MakeRequest
        model = MakeRequestCash
        model = Shopping
        fields =['id']

class AdminFilterUsers(django_filters.FilterSet):
    class Meta:
        model = Customer
        fields =['user']
        
        