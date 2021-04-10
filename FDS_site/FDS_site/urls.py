"""FDS_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from users import views as user_views
from django.contrib.auth import views as auth_views #2nd
from django.conf import settings
from django.conf.urls.static import static
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('FDS_app.urls')),
    path('register/', user_views.register, name='register'),

    path('profileUpdate/<str:user>/', user_views.customerProfileUpdatePage, name='profileUpdate'),

    path('success/', user_views.successPage, name='success'),

    path('requestForm_Online/<int:user>/', user_views.requestForm_Online, name='requestForm_Online'),

    path('requestForm_Cash/<int:user>/', user_views.requestForm_Cash, name='requestForm_Cash'),

    path('shopping/<str:user>/', user_views.ShoppingForm, name='shopping'),

    path('Initialize_requestForm/<int:user>/', user_views.Initialize_requestForm, name='Initialize_requestForm'),

    path('orderHistory/<str:user>/', user_views.orderHistory, name='orderHistory'),

    path('adminDashboard/', user_views.AdminDashboard, name='adminDashboard'),

    path(r'<int:user>/', user_views.customerDashboardPage, name='dashboard'),

    path('updateRequest/<str:pk>/', user_views.updateRequestForm, name='updateRequest'),

    path('cancelRequest/<str:pk>/', user_views.cancelRequest, name='cancelRequest'),

    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/', 
        auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),

    path('password-reset/done/', 
        auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),

    path('password-reset-complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    path ('', include('FDS_app.urls',)),
]
 
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)