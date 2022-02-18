
from django.conf.urls import handler404

from django.contrib import admin
from django.urls import include, path, register_converter
from users import views as user_views
from django.contrib.auth import views as auth_views #2nd
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from users.views import LoginView
from users.utils import HashIdConverter
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
register_converter(HashIdConverter, "hashid")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('FDS_app.urls')),

    path('', include('BikeControl.urls')), 

    path('', include('PortHarcourt.urls')),

    path('', include('Management.urls')),

    path('', include('Affiliate.urls')),

    path('tinymce/', include('tinymce.urls')),

    path('404/', user_views.response_error_handler),

    path('register/', user_views.register, name='register'),

    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),

    path('profileUpdate/<hashid:user>/', user_views.customerProfileUpdatePage, name='profileUpdate'),

    path('passwordChange/<hashid:user>/', user_views.PasswordChange, name='passwordchange'),

    path('success/<str:user>/', user_views.successPage, name='success'),

    path('requestForm_Online/<hashid:user>/',  user_views.requestForm_Online, name='requestForm_Online'),

    path('requestForm_Cash/<hashid:user>/', user_views.requestForm_Cash, name='requestForm_Cash'),

    path('shopping/<hashid:user>/', user_views.ShoppingForm, name='shopping'),    

    path('orderHistory/<hashid:user>/', user_views.orderHistory, name='orderHistory'),

    path('customers-list/', user_views.customers_list, name='customers-list'),

    path('adminDashboard/', user_views.AdminDashboard, name='adminDashboard'),

    path('e-request/', user_views.allE_request, name='e-request'),

    path('cash-request/', user_views.allCash_Request, name='cash-request'),

    path('shopping-request/', user_views.allShopping_Request, name='shopping-request'),

    path('allErrand-request/', user_views.allE_errand, name='allerrand-request'),

    path('allFront-request/', user_views.allFront_Desk, name='allfront-request'),

    path('anonymous-request/', user_views.allAnonymous_Request, name='anonymous-request'),

    path('dashboard/<hashid:user>/', user_views.customerDashboardPage, name='dashboard'),

    path('updateRequest/<hashid:pk>/', user_views.updateRequestForm, name='updateRequest'),
    path('updateRequestCash/<hashid:pk>/', user_views.updateRequestFormCash, name='updateRequestCash'),
    path('updateRequestShopping/<hashid:pk>/', user_views.updateRequestFormShopping, name='updateRequestShopping'),
    path('updateRequestAnon/<hashid:pk>/', user_views.updateRequestAnon, name='updateRequestAnon'),
    path('updateRequestErand/<hashid:pk>/', user_views.Update_Errand_Form, name='updateRequestErrand'),
    path('updateRequestFrontDesk/<hashid:pk>/', user_views.Update_Front_Fesk_Form, name='updateRequestFront'),

    path('cancelRequestErrand/<hashid:pk>/', user_views.cancelRequestErrand, name='cancelRequestErrand'),
    path('cancelRequestFront/<hashid:pk>/', user_views.cancelRequestFront, name='cancelRequestFront'),
    path('cancelRequest/<hashid:pk>/', user_views.cancelRequest, name='cancelRequest'),
    path('cancelRequestCash/<hashid:pk>/', user_views.cancelRequestCash, name='cancelRequestCash'),
    path('cancelRequestShopping/<hashid:pk>/', user_views.cancelRequestShopping, name='cancelRequestShopping'),
    path('cancelRequestAnon/<hashid:pk>/', user_views.cancelRequestAnon, name='cancelRequestAnon'),

    path('show_Notification/<hashid:user>/', user_views.Notifications_show, name='show_Notification'),
    path('delete_Notification/<hashid:pk>/', user_views.Notifications_delete, name='delete_Notification'),

    path('adminNotificationShow/', user_views.adminNotificationShow, name='adminNotificationShow'),
    path('adminNotificationDelete/<hashid:pk>/', user_views.adminNotificationDelete, name='adminNotificationDelete'),

    path('Errand_Menu/<hashid:user>/', user_views.ErrandMenu, name='errandmenu'),
    path('Fuel_Errand/<hashid:user>/', user_views.fuel_errand, name='fuelerrand'),
    path('Gas_Errand/<hashid:user>/', user_views.gas_errand, name='gaserrand'),
    path('Drugs_Errand/<hashid:user>/', user_views.drugs_errand, name='drugserrand'),
    path('Bread_Errand/<hashid:user>/', user_views.bread_errand, name='breaderrand'),
    path('Shawarma_Errand/<hashid:user>/', user_views.shawarma_errand, name='shawarmaerrand'),
    path('Pizza_Errand/<hashid:user>/', user_views.pizza_errand, name='pizzaerrand'),
    path('Fruits_Errand/<hashid:user>/', user_views.fruits_errand, name='fruitserrand'),
    path('Icecream_Errand/<hashid:user>/', user_views.icecream_errand, name='icecreamerrand'),
    path('Food_Errand/<hashid:user>/', user_views.food_errand, name='fooderrand'),
    path('Other_Errand/<hashid:user>/', user_views.other_errand, name='othererrand'),

    path('Front_desk/<hashid:user>/', user_views.front_desk, name='frontdesk'),
    path('Front_deskForm/<hashid:user>/', user_views.PickDrop, name='frontdeskform'),
    path('Front_desk_Errand_Form/<hashid:user>/', user_views.FrontErrand, name='frontdeskerrand'),

    path('FleetManager/<hashid:user>/', user_views.FleetManager, name='fleetManager'),

    path('Cashier/<hashid:user>/', user_views.Cashier, name='cashier'),
    path('CashierUpdateE/<hashid:pk>/', user_views.CashierUpdateE_RequestForm, name='cashierupdate_e'),
    path('CashierUpdateCash/<hashid:pk>/', user_views.CashierUpdateCash_RequestForm, name='cashierupdate_c'),
    path('CashierUpdateS/<hashid:pk>/', user_views.CashierUpdateShoppingForm, name='cashierupdate_s'),
    path('CashierUpdateA/<hashid:pk>/', user_views.CashierUpdateAnonForm, name='cashierupdate_a'),
    path('CashierUpdateErr/<hashid:pk>/', user_views.CashierUpdateErrandForm, name='cashierupdate_err'),
    path('CashierUpdateF/<hashid:pk>/', user_views.CashierUpdateFrontForm, name='cashierupdate_f'),

    path('FleetManagerE/<hashid:pk>/', user_views.UpdateEForm, name='fleetE'),
    path('FleetManagerC/<hashid:pk>/', user_views.UpdateCForm, name='fleetC'),
    path('FleetManagerS/<hashid:pk>/', user_views.UpdateSForm, name='fleetS'),
    path('FleetManagerErr/<hashid:pk>/', user_views.UpdateErrForm, name='fleetErr'),
    path('FleetManagerA/<hashid:pk>/', user_views.UpdateAForm, name='fleetA'),
    path('FleetManagerF/<hashid:pk>/', user_views.UpdateFForm, name='fleetF'),

    path('SearchId/', user_views.Inhousesearch, name='searchid'),

    path('redirecting_user/', user_views.redirectView, name='redirecting_user'),

    path('UpdateLocation/<hashid:user>/', user_views.locationChange, name='update_location'),

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/', 
        auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),

    path('password-reset/done/', 
        auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),

    path('password-reset-complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
]
 
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'users.views.response_error_handler'