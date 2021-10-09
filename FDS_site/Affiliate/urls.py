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
    
]