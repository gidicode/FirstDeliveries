from re import A
from django.db.models import fields
import django_filters
from django_filters import DateFilter

from.models import *
from BikeControl.models import RidersDeliveries

class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = MakeRequest
        model = MakeRequestCash
        model = Errand_service
        model = Shopping
        fields =['order_id',]

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

class BikeFilter(django_filters.FilterSet):

    cash_request__order_id = django_filters.CharFilter(lookup_expr='icontains')
    anonymous__order_id = django_filters.CharFilter(lookup_expr='icontains')
    shopping__order_id = django_filters.CharFilter(lookup_expr='icontains')
    e_payment_request__order_id = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = RidersDeliveries
        fields = ['rider', 'cash_request__order_id', 'anonymous__order_id', 'shopping__order_id', 'e_payment_request__order_id']

        