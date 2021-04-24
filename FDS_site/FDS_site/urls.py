
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

    path('success/<str:user>/', user_views.successPage, name='success'),

    path('requestForm_Online/<int:user>/', user_views.requestForm_Online, name='requestForm_Online'),

    path('requestForm_Cash/<int:user>/', user_views.requestForm_Cash, name='requestForm_Cash'),

    path('shopping/<str:user>/', user_views.ShoppingForm, name='shopping'),

    path('Initialize_requestForm/<int:user>/', user_views.Initialize_requestForm, name='Initialize_requestForm'),

    path('orderHistory/<str:user>/', user_views.orderHistory, name='orderHistory'),

    path('customers-list/', user_views.customers_list, name='customers-list'),

    path('adminDashboard/', user_views.AdminDashboard, name='adminDashboard'),

    path(r'<int:user>/', user_views.customerDashboardPage, name='dashboard'),

    path('updateRequest/<str:pk>/', user_views.updateRequestForm, name='updateRequest'),
    path('updateRequestCash/<str:pk>/', user_views.updateRequestFormCash, name='updateRequestCash'),
    path('updateRequestShopping/<str:pk>/', user_views.updateRequestFormShopping, name='updateRequestShopping'),

    path('cancelRequest/<str:pk>/', user_views.cancelRequest, name='cancelRequest'),
    path('cancelRequestCash/<str:pk>/', user_views.cancelRequestCash, name='cancelRequestCash'),
    path('cancelRequestShopping/<str:pk>/', user_views.cancelRequestShopping, name='cancelRequestShopping'),

    path('show_Notification/<str:user>/', user_views.Notifications_show, name='show_Notification'),
    path('delete_Notification/<str:pk>/', user_views.Notifications_delete, name='delete_Notification'),

    path('adminNotificationShow/', user_views.adminNotificationShow, name='adminNotificationShow'),
    path('adminNotificationDelete/<str:pk>/', user_views.adminNotificationDelete, name='adminNotificationDelete'),


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
]
 
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)