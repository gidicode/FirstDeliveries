from django.urls import path, register_converter
from .  import views as management_views
from users.utils import HashIdConverter
register_converter(HashIdConverter, "hashid")

urlpatterns = [
    path('Management_Dashboard/<hashid:user>/', management_views.Front_page, name='management_dashboard'),

    path('Create_Profile/<hashid:user>/', management_views.Create_Profile_management, name='create_profile'),

    path('Create_Report/<hashid:user>/', management_views.Create_report, name='create_report'),
    path('Fleet_Create_Report/<hashid:user>/', management_views.Fleet_Report, name='fleet_create_report'),
    path('ICT_Create_Report/<hashid:user>/', management_views.ICT_Report, name='ict_create_report'),
    path('Market_Create_Report/<hashid:user>/', management_views.Marketing_Report, name='market_create_report'),
    path('Front_Create_Report/<hashid:user>/', management_views.Front_Desk_Report, name='front_create_report'),

    path('Edit_Report/<hashid:pk>/', management_views.Edit_Report, name='edit_report'),
    path('Edit_Fleet_Report/<hashid:pk>/', management_views.Edit_Fleet_Report, name='edit_fleet_report'),
    path('Edit_Ict_Report/<hashid:pk>/', management_views.Edit_ict_Report, name='edit_ict_report'),
    path('Edit_Market_Report/<hashid:pk>/', management_views.Edit_market_Report, name='edit_market_report'),
    path('Edit_Front_Report/<hashid:pk>/', management_views.Edit_front_Report, name='edit_front_report'),

    path('Report_History/<hashid:user>/', management_views.Status_History, name='report_history'),

    path('History_Detail/<hashid:pk>/', management_views.History_details, name='history_detail'),

    path('Management_Report/<hashid:user>/', management_views.Management_view, name='management_report'),

    path('Chairman_response/<hashid:pk>/', management_views.Chairman_response, name='chairman_response'),
    path('Operation_response/<hashid:pk>/', management_views.Operations_response, name='operations_response'),
    path('Admin_response/<hashid:pk>/', management_views.Admin_response, name='admin_response'),
    path('Manager_response/<hashid:pk>/', management_views.Manager_response, name='manager_response'),
    path('Runyi_response/<hashid:pk>/', management_views.Runyi_Response, name='runyi_response'),

    path('Management_view_List/<hashid:user>/', management_views.Management_report_list, name='management_list'),

    path('Management_view_details/<hashid:pk>/', management_views.History_details_management, name='management_list_details'),
]