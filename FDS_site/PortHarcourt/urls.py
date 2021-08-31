from django.urls import path, register_converter
from . import views as user_views
from users.utils import HashIdConverter
register_converter(HashIdConverter, "hashid")

urlpatterns = [    
    path('cash_request_ph/<hashid:user>/', user_views.requestForm_Cash_PH, name='cash_request_ph'),
    path('errand_menu_ph/<hashid:user>/', user_views.ErrandMenu_PH, name='errand_menu_ph'),
    path('fuel_errand_ph/<hashid:user>/', user_views.fuel_errand_ph, name='fuel_errand_ph'),
    path('gas_errand_ph/<hashid:user>/', user_views.gas_errand_ph, name='gas_errand_ph'),
    path('drugs_errand_ph/<hashid:user>/', user_views.drugs_errand_ph, name='drugs_errand_ph'),
    path('bread_errand_ph/<hashid:user>/', user_views.bread_errand_ph, name='bread_errand_ph'),
    path('sharwarma_errand_ph/<hashid:user>/', user_views.shawarma_errand_ph, name='sharwarmaerrand_ph'),  
    path('AdminDashboard_PH/', user_views.AdminDashboard_PH, name='adminDashboard_ph'),      
    
    ]