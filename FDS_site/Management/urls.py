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
    path('Runyi_Create_Report/<hashid:user>/', management_views.Runyi_Report, name='runyi_create_report'),
    path('IWH_Create_Report/<hashid:user>/', management_views.IWH_Report, name='iwh_create_report'),
    path('TANKFARM_Create_Report/<hashid:user>/', management_views.TANK_FARM_Report, name='tankfarm_create_report'),
    path('Manager_Create_Report/<hashid:user>/', management_views.Manager_Report, name='manager_create_report'),
    path('Commercial_Create_Report/<hashid:user>/', management_views.Commercial_Report, name='commercial_create_report'),
    path('Admin_Create_Report/<hashid:user>/', management_views.Admin_Report, name='admin_create_report'),
    path('Account_Create_Report/<hashid:user>/', management_views.Account_Report, name='account_create_report'),
    path('Maintenance_Create_Report/<hashid:user>/', management_views.MaintenanceAccount_Report, name='maintenance_create_report'),
    path('PH_Create_Report/<hashid:user>/', management_views.PortHatcourt_office_Report, name='ph_create_report'),

    path('Edit_Report/<hashid:pk>/', management_views.Edit_Report, name='edit_report'),
    path('Edit_Fleet_Report/<hashid:pk>/', management_views.Edit_Fleet_Report, name='edit_fleet_report'),
    path('Edit_Ict_Report/<hashid:pk>/', management_views.Edit_ict_Report, name='edit_ict_report'),
    path('Edit_Market_Report/<hashid:pk>/', management_views.Edit_market_Report, name='edit_market_report'),
    path('Edit_Front_Report/<hashid:pk>/', management_views.Edit_front_Report, name='edit_front_report'),
    path('Edit_Runyi_Report/<hashid:pk>/', management_views.Edit_Runyi_Report, name='edit_runyi_report'),
    path('Edit_Iwh_Report/<hashid:pk>/', management_views.Edit_IWH_Report, name='edit_iwh_report'),
    path('Edit_TankFarm_Report/<hashid:pk>/', management_views.Edit_Tank_Farm_Report, name='edit_tank_farm_report'),
    path('Edit_Manager_Report/<hashid:pk>/', management_views.Edit_Manager_Report, name='edit_manager_report'),
    path('Edit_Commercial_Report/<hashid:pk>/', management_views.Edit_Commercial_Report, name='edit_commercial_report'),
    path('Edit_admin_Report/<hashid:pk>/', management_views.Edit_admin_Report, name='edit_admin_report'),
    path('Edit_account_Report/<hashid:pk>/', management_views.Edit_account_Report, name='edit_account_report'),
    path('Edit_maintenance_Report/<hashid:pk>/', management_views.Edit_maintenance_Report, name='edit_maintenance_report'),
    path('Edit_ph_Report/<hashid:pk>/', management_views.Edit_portharcourt_office_Report, name='edit_ph_report'),

    path('Report_History/<hashid:user>/', management_views.Status_History, name='report_history'),

    path('History_Detail/<hashid:pk>/', management_views.History_details, name='history_detail'),

    path('Management_Report/<hashid:user>/', management_views.Management_view, name='management_report'),

    path('Chairman_response/<hashid:pk>/', management_views.Chairman_response, name='chairman_response'),
    path('Operation_response/<hashid:pk>/', management_views.Operations_response, name='operations_response'),
    path('Admin_response/<hashid:pk>/', management_views.Admin_response, name='admin_response'),
    path('Manager_response/<hashid:pk>/', management_views.Manager_response, name='manager_response'),
    path('Runyi_response/<hashid:pk>/', management_views.Runyi_Response, name='runyi_response'),
    path('FLM_response/<hashid:pk>/', management_views.FLM_Response, name='flm_response'),

    path('Management_view_List/<hashid:user>/', management_views.Chairman_report_list, name='management_list'),
    path('Management_view_details/<hashid:pk>/', management_views.History_details_management, name='management_list_details'),

    path('FLLS_Manager_view_list/<hashid:user>/', management_views.FLLS_manager_report_list, name='flls_manager_list'),
    path('FLM_Manager_view_list/<hashid:user>/', management_views.FLM_manager_report_list, name='flm_manager_list'),
    path('runyi_view_list/<hashid:user>/', management_views.Runyi_report_list, name='runyi_list'),
    path('operation_view_list/<hashid:user>/', management_views.Operations_report_list, name='operations_list'),
    path('admin_view_list/<hashid:user>/', management_views.Admin_report_list, name='admin_list'),

    path('logistics_page/<hashid:user>/', management_views.Logistics, name='Logistics'),
]