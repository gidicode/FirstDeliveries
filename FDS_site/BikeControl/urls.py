from django.urls.conf import path
from . import views as user_views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('drivers_dashboard/', user_views.Riders_Dashboard, name='drivers_dashboard'),
    path('assigned_deliveries/', user_views.assigned_Del, name='assigned_deliveries'),
    path('update_assigned_deliveries/<str:pk>/', user_views.update_assigned_Del, name='update_assigned_deliveries'),
    path('all_Fleet/', user_views.all_Fleet, name='all_Fleet'),
    path('Riders_Profile/', user_views.Riders_identity, name='Riders_Profile'),
    path('assignedRides/', user_views.AssignedRides, name='assignedRides'),
    path('allRiderDeliveries/<str:rider>/', user_views.All_riders_deliveries, name="allRiderDeliveries")   
]