from . import views
from django.urls import path
 

urlpatterns = [
    path('', views.index, name='fds-home'),
    path('about/', views.about, name='fds-about'),
    path('userRegpage/', views.userRegPage, name='fds-userRegpage'),
    path('billing/', views.billing, name='fds-billing'),
    path('error/', views.error, name='fds-error'),
    path('history/', views.history, name='fds-history'),
    path('notification/', views.notification, name='fds-notification'),
    path('order/', views.order, name='fds-order'),
    path('passReset/', views.passReset, name='fds-passReset'),
    path('payment_success/', views.payment_success, name='fds-payment_success'),
    path('pricing/', views.pricing, name='fds-pricing'),
    path('signup/', views.signup, name='fds-signup'),
    path('dashBase/', views.dashBase, name='dashbase'), 
    #path('password_reset/', views.password_reset, name='password_reset'),
] 