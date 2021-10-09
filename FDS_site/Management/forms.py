from .models import OFFICE_REPORT
from django import forms
from users.models import Customer
from django.forms import Textarea, fields, models

class Management_profile(forms.ModelForm):    
    class Meta:
        model = Customer
        fields = ['Department', 'Designation']

class Report_Form(forms.ModelForm):    
    class Meta:
        model = OFFICE_REPORT
        fields = [
            'work_schedule', 'Work_description', 
            'extent_of_completion', 'work_left', 
            'challenges', 'solutions',
            ]        

class Edit_Report_Form(forms.ModelForm):    
    class Meta:
        model = OFFICE_REPORT
        fields = [
            'work_schedule', 'Work_description', 
            'extent_of_completion', 'work_left', 
            'challenges', 'solutions',
        ]        

class Fleet_Report_Form(forms.ModelForm):    
    class Meta:
        model = OFFICE_REPORT
        fields = [
            'work_schedule', 'work_left', 'Fleet_report_title', 
            'Fleet_report', 'Fleet_challenges', 
            'Fleet_solutions', 
       ]    

class Edit_Fleet_Report_Form(forms.ModelForm):    
    class Meta:
        model = OFFICE_REPORT
        fields = [
            'work_schedule', 'work_left',  'Fleet_report_title', 
            'Fleet_report', 'Fleet_challenges', 
            'Fleet_solutions', 
       ]
        

class ICT_Report_Form(forms.ModelForm):    
    class Meta:
        model = OFFICE_REPORT
        fields = [
            'work_schedule', 'work_left', 'Ict_report_Title', 
            'Ict_report', 'Ict_challenges', 'Ict_solutions', 
       ]

class EditICT_Report_Form(forms.ModelForm):    
    class Meta:
        model = OFFICE_REPORT
        fields = [
            'work_schedule', 'work_left', 
            'Ict_report_Title', 'Ict_report', 
            'Ict_challenges', 'Ict_solutions',         
       ]
       

class Front_Report_Form(forms.ModelForm):    
    class Meta:
        model = OFFICE_REPORT
        fields = [
            'work_schedule', 'work_left', 'FrontDesk_report_Title', 
            'FrontDesk_report', 'Front_desk_total_rides', 
            'Front_desk_total_amount', 'FrontDesk_challenges', 
            'FrontDesk_solutions', 
       ]
        
class Marketing_Report_Form(forms.ModelForm):    
    class Meta:
        model = OFFICE_REPORT
        fields = [
            'work_schedule', 'work_left', 
            'Marketing_report_title', 'Marketing_report', 
            'Marketting_challenges', 
            'Marketing_solutions',         
       ]

class IWH_Form(forms.ModelForm):    
    class Meta:
        model = OFFICE_REPORT
        fields = [
            'work_schedule', 'work_left', 
            'Iwh_report_title', 'Iwh_report', 
            'Iwh_challenges', 'Iwh_solutions',
       ]        

class TANK_Form(forms.ModelForm):    
    class Meta:
        model = OFFICE_REPORT
        fields = [
            'work_schedule', 'work_left', 
            'Tank_farm_report_title', 'Tank_farm_report', 
            'Tank_farm_challenges', 'Tank_farm_solutions',
       ]    

class TANK_Form(forms.ModelForm):    
    class Meta:
        model = OFFICE_REPORT
        fields = [
            'work_schedule', 'work_left', 
            'Tank_farm_report_title', 'Tank_farm_report', 
            'Tank_farm_challenges', 'Tank_farm_solutions',
       ]    

class RUNYI_Form(forms.ModelForm):    
    class Meta:
        model = OFFICE_REPORT
        fields = [
            'work_schedule', 'work_left', 
            'Runyi_report_Title', 'Runyi_report', 
            'Runyi_challenges', 'Runyi_solutions',
            'for_operation', 'for_manager_FLM',
       ]
 
class Manager_FLLS_report_Form(forms.ModelForm): 
    
    class Meta:
        model = OFFICE_REPORT
        fields = [
            'work_schedule', 'work_left',  'Manager_report_title',
            'Manager_report', 'Manager_challenges', 
            'Manager_solutions',
       ]        

class Commercial_report_Form(forms.ModelForm):     
    class Meta:
        model = OFFICE_REPORT
        fields = [
            'Commectial_Report_Title', 'work_schedule', 
            'Commercial_Report', 'Commercial_Breakdown', 
            'Commercial_Balance', 'Commercial_Challenges', 
       ]   

class Admin_report_form(forms.ModelForm):
    class Meta:
        model = OFFICE_REPORT
        fields = [
            'work_schedule', 'work_left', 
            'Admin_report_title', 'Admin_report_details',
            'Admin_challenges', 'Admin_solutions',
        ]

class Account_report_form(forms.ModelForm):
    class Meta:
        model = OFFICE_REPORT
        fields = [
            'work_schedule', 'work_left', 
            'Account_report_title', 'Account_report_details',
            'Account_challenges', 'Account_solutions',
        ]

class Maintenance_report_form(forms.ModelForm):
    class Meta:
        model = OFFICE_REPORT
        fields = [
            'work_schedule', 'work_left', 
            'Maintenance_report_title', 'Maintenacne_report_details',
            'Maintenance_challenges', 'Maintenance_solutions',
        ]

class PH_report_form(forms.ModelForm):
    class Meta:
        model = OFFICE_REPORT
        fields = [
            'work_schedule', 'work_left', 
            'Manager_report_title_PH', 'Manager_report_PH',
            'Manager_challenges_PH', 'Manager_solutions_PH',
        ]

class Chairman_Response_Form(forms.ModelForm):    
    class Meta:
        model = OFFICE_REPORT
        fields = ['feedback_chairman']

class Operations_Response_Form(forms.ModelForm):    
    class Meta:
        model = OFFICE_REPORT
        fields = ['feedback_operations']    

class Admin_Response_Form(forms.ModelForm):    
    class Meta:
        model = OFFICE_REPORT
        fields = ['feedback_admin']

class Manager_Response_Form(forms.ModelForm):    
    class Meta:
        model = OFFICE_REPORT
        fields = ['feedback_manager']

class Runyi_Response_Form(forms.ModelForm):    
    class Meta:
        model = OFFICE_REPORT
        fields = ['feedback_runyi']

class FLLM_Manager_Response_Form(forms.ModelForm):    
    class Meta:
        model = OFFICE_REPORT
        fields = ['feedback_Manager_FLM']