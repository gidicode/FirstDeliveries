from . import views
from django.urls import path
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import include, path
from django.views.generic.base import RedirectView
from django.conf import settings
 

urlpatterns = [
    path('', views.index, name='fds-home'),
    path('about/', views.about, name='fds-about'),
    path('userRegpage/', views.userRegPage, name='fds-userRegpage'),
    path('billing/', views.billing, name='fds-billing'),
    path('error/', views.error, name='fds-error'),
    path('search/', views.search, name='search'),
    path('notification/', views.notification, name='fds-notification'),
    path('order/', views.order, name='fds-order'),
    path('passReset/', views.passReset, name='fds-passReset'),
    path('payment_success/', views.payment_success, name='fds-payment_success'),
    path('pricing/', views.pricing, name='fds-pricing'),
    path('signup/', views.signup, name='fds-signup'),
    path('dashBase/<str:user>/', views.dashBase, name='dashBase'),
     path(
        "favicon.ico",
        RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),
    ), 
    #path('password_reset/', views.password_reset, name='password_reset'),
] 