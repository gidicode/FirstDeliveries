from django.urls import path, register_converter
from .  import views as affiliate_views
from users.utils import HashIdConverter
register_converter(HashIdConverter, "hashid")

urlpatterns = [
    path('Join_Affiliate_FLLS/<hashid:user>/', affiliate_views.Affiliate_joinPage, name="join_affiliate"),    
    path('Welcome_page_FLLS/<hashid:user>/', affiliate_views.Creating_referal_code, name="welcome_affiliate"),
    path('Affiliate_Welcome_Page_FLLS/<hashid:user>/', affiliate_views.Welcome_page , name="welcome_page"),

    #Dashboard
    path('Affiliate_Dashboard_FLLS/<hashid:user>/', affiliate_views.Marketer_Dashboard , name="affiliate_dashboard"), 
    
    #Rquest_payout
    path('Payout_FLLS/<hashid:user>/', affiliate_views.Request_Payout_form, name="request_payout"), 
    path('Balance_FLLS/<hashid:user>/', affiliate_views.Balance_status, name="balance_status"), 

    #Add Bank details
    path('Add_Bank_Details_FLLS/<hashid:user>/', affiliate_views.Add_bank_account, name="add-bank"),     

    #Payout History
    path('Payout_History_FLLS/<hashid:user>/', affiliate_views.Payout_History_list, name="payout_history"),     
    path('Payout_History_Details_FLLS/<hashid:pk>/', affiliate_views.Payout_History_Details, name="payout_history_details"),     

    #deLETE BANK DETAILS
    path('Delete_Account_FLLS/<hashid:pk>/', affiliate_views.Delete_account, name="delete_account"),     

    path('Delivery_Details_FLLS/<hashid:pk>/', affiliate_views.Delivery_Details, name="delivery_details"),     
]