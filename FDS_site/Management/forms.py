from .models import OFFICE_REPORT
from django import forms
from users.models import Customer
from django.forms import Textarea

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
        widgets = {
            'work_schedule':Textarea(attrs={'cols': 20, 'row':10}),
            'challenges':Textarea(attrs={'cols': 10, 'row':10}),
            }

class Edit_Report_Form(forms.ModelForm):    
    class Meta:
        model = OFFICE_REPORT
        fields = [
            'work_schedule', 'Work_description', 
            'extent_of_completion', 'work_left', 
            'challenges', 'solutions',
        ]
        widgets = {
            'work_schedule':Textarea(attrs={'cols': 20, 'row':10}),
            'challenges':Textarea(attrs={'cols': 10, 'row':10}),
            }

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
        widgets = {
            'Fleet_report':Textarea(attrs={'cols': 5, 'row':5}),
            'Fleet_challenges':Textarea(attrs={'cols': 5, 'row':5}),
            }

class ICT_Report_Form(forms.ModelForm):    
    class Meta:
        model = OFFICE_REPORT
        fields = [
            'work_schedule', 'work_left', 'Ict_report_Title', 
            'Ict_report', 'Ict_challenges', 'Ict_solutions', 
       ]
        widgets = {
            'Ict_report':Textarea(attrs={'cols': 5, 'row':5}),
            'Ict_challenges':Textarea(attrs={'cols': 5, 'row':5}),}

class EditICT_Report_Form(forms.ModelForm):    
    class Meta:
        model = OFFICE_REPORT
        fields = [
            'work_schedule', 'work_left', 
            'Ict_report_Title', 'Ict_report', 
            'Ict_challenges', 'Ict_solutions',         
       ]
        widgets = {
            'Ict_report':Textarea(attrs={'cols': 5, 'row':5}),
            'Ict_challenges':Textarea(attrs={'cols': 5, 'row':5}),}

class Front_Report_Form(forms.ModelForm):    
    class Meta:
        model = OFFICE_REPORT
        fields = [
            'work_schedule', 'work_left', 'FrontDesk_report_Title', 
            'FrontDesk_report', 'Front_desk_total_rides', 
            'Front_desk_total_amount', 'FrontDesk_challenges', 
            'FrontDesk_solutions', 
       ]
        widgets = {
            'FrontDesk_report':Textarea(attrs={'cols': 5, 'row':5}),
            'FrontDesk_challenges':Textarea(attrs={'cols': 5, 'row':5}),}

class Marketing_Report_Form(forms.ModelForm):    
    class Meta:
        model = OFFICE_REPORT
        fields = [
            'work_schedule', 'work_left', 
            'Marketing_report_title', 'Marketing_report', 
            'Marketting_challenges', 
            'Marketing_solutions',         
       ]
        widgets = {
            'Marketing_report':Textarea(attrs={'cols': 5, 'row':5}),
            'Marketting_challenges':Textarea(attrs={'cols': 5, 'row':5}),}

class IWH_Form(forms.ModelForm):    
    class Meta:
        model = OFFICE_REPORT
        fields = [
            'work_schedule', 'work_left', 
            'Iwh_report_title', 'Iwh_report', 
            'Iwh_challenges', 'Iwh_solutions',
       ]
        widgets = {
            'Iwh_report':Textarea(attrs={'cols': 5, 'row':5}),
            'Iwh_challenges':Textarea(attrs={'cols': 5, 'row':5}),
            }

class TANK_Form(forms.ModelForm):    
    class Meta:
        model = OFFICE_REPORT
        fields = [
            'work_schedule', 'work_left', 
            'Tank_farm_report_title', 'Tank_farm_report', 
            'Tank_farm_challenges', 'Tank_farm_solutions',
       ]
        widgets = {
            'Tank_farm_report':Textarea(attrs={'cols': 5, 'row':5}),
            'Tank_farm_challenges':Textarea(attrs={'cols': 5, 'row':5}),            
            }

class RUNYI_Form(forms.ModelForm):    
    class Meta:
        model = OFFICE_REPORT
        fields = [
            'work_schedule', 'work_left', 
            'Runyi_report_Title', 'Runyi_report', 
            'Runyi_challenges', 'Runyi_solutions',
       ]
        widgets = {
            'Runyi_report':Textarea(attrs={'cols': 5, 'row':5}),
            'Runyi_challenges':Textarea(attrs={'cols': 5, 'row':5}),
            }

class Manager_FLLS_report_Form(forms.ModelForm):    
    class Meta:
        model = OFFICE_REPORT
        fields = [
            'work_schedule', 'work_left',  'Manager_report_title',
            'Manager_report', 'Manager_challenges', 
            'Manager_solutions',
       ]
        widgets = {
            'Manager_report':Textarea(attrs={'cols': 5, 'row':5}),
            'Manager_challenges':Textarea(attrs={'cols': 5, 'row':5}),
        }


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