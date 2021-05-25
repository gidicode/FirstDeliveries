from re import A
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
        fields ={
            'order_id',
            'status',
        }
        filter_overrides = {
            models.CharField: {
                'filter_class':django_filters.CharFilter,
                'extra': lambda f:{
                    'lookup_expr': 'icontains',
                },
            },
        }

class AdminFilterUsers(django_filters.FilterSet):
    class Meta:
        model = Customer
        fields =['user']

class AnonFilters(django_filters.FilterSet):
    class Meta:
        model = Anonymous
        fields =['order_id']
        
        