from django.db import models
from django.db.models.base import Model
from django.utils import timezone
from users.models import Customer
from tinymce import models as tinymce_models

# Create your models here.

class OFFICE_REPORT(models.Model):
    TIME = [
        (None, None),
        ('0-1HR', '0-1HR'),
        ('1-2HRS', '1-2HRS'),
        ('2-3HRS', '2-3HRS'),
        ('3-4HRS', '3-4HRS'),
        ('4-5HRS', '4-5HRS'),
    ]    

    CATEGORY = [
        ('Operations', 'Operations'),
        ('Fleet', 'Fleet'),        
        ('ICT', 'ICT'),
        ('Front', 'Front'),
        ('Market', 'Market'),
        ('Tank Farm', 'Tank Farm'),
        ('IWH', 'IWH'),
        ('RUNYI', 'RUNYI'),
        ('MANAGER', 'MANAGER'),
        ('COMMERCIAL', 'COMMERCIAL'),
        ('ADMIN', 'ADMIN'),
        ('ACCOUNT', 'ACCOUNT'),
        ('MAINTENANCE', 'MAINTENANCE'),
        ('MANAGER_PH', 'MANAGER_PH'),
    ]
    
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL, verbose_name="STAFF")

    #Operations
    work_schedule = tinymce_models.HTMLField(max_length=5000, verbose_name="Task Schedule", blank=True, null=True)
    Work_description = tinymce_models.HTMLField(null=True, verbose_name="Main Report", blank=True, max_length=5000)
    extent_of_completion = tinymce_models.HTMLField(null=True, verbose_name="Task Completed", blank=True, max_length=5000)
    time_taken = tinymce_models.HTMLField(null=True, choices=TIME, max_length=2000, blank=True )    
    work_left = tinymce_models.HTMLField(null=True, verbose_name="Task Left", blank=True, max_length=2000)
    solutions = tinymce_models.HTMLField(null=True, blank=True, max_length = 5000)
    challenges = tinymce_models.HTMLField(max_length=5000, blank=True, null=True)

    #Fleet
    Fleet_report_title = models.CharField(null=True, blank=True, max_length=100)
    Fleet_report = tinymce_models.HTMLField(null=True, blank=True, max_length=5000)
    Fleet_challenges = tinymce_models.HTMLField(null=True, blank=True, max_length=5000)
    Fleet_solutions = tinymce_models.HTMLField(null=True, blank=True, max_length = 5000)
    
    #Marketing
    Marketing_report_title = models.CharField(null=True, blank=True, max_length=100)
    Marketing_report = tinymce_models.HTMLField(null=True, blank=True, max_length=5000)
    Marketting_challenges = tinymce_models.HTMLField(null=True, blank=True, max_length=5000, )
    Marketing_solutions = tinymce_models.HTMLField(null=True, blank=True, max_length = 5000)

    #Front_desk
    FrontDesk_report_Title = models.CharField(null=True, blank=True, max_length=100)
    FrontDesk_report = tinymce_models.HTMLField(null=True, blank=True, max_length=5000)
    Front_desk_total_rides = models.IntegerField(null=True, blank=True, verbose_name='Total Rides Today')
    Front_desk_total_amount = models.IntegerField(null=True, blank=True, verbose_name='Total Amount Today')
    FrontDesk_challenges =tinymce_models.HTMLField(null=True, blank=True, max_length=5000,)
    FrontDesk_solutions = tinymce_models.HTMLField(null=True, blank=True, max_length = 5000)

    #IWH
    Iwh_report_title = models.CharField(null=True, blank=True, max_length=100)
    Iwh_report = tinymce_models.HTMLField(null=True, blank=True, max_length=5000)
    Iwh_challenges = tinymce_models.HTMLField(null=True, blank=True,  max_length=5000, verbose_name="Challenges")
    Iwh_solutions = tinymce_models.HTMLField(null=True, blank=True, max_length = 5000)

    #TankFarm
    Tank_farm_report_title = models.CharField(null=True, blank=True, max_length=100, verbose_name="Report Title")
    Tank_farm_report = tinymce_models.HTMLField(null=True, blank=True, max_length=5000)
    Tank_farm_challenges = tinymce_models.HTMLField(null=True, blank=True, max_length=5000, verbose_name="Challenges")
    Tank_farm_solutions = models.CharField(null=True, blank=True, max_length=5000, verbose_name="Solutions")

    #Runyi
    Runyi_report_Title = models.CharField(null=True, blank=True, max_length=100)
    Runyi_report = tinymce_models.HTMLField(null=True, blank=True, max_length=5000)
    Runyi_challenges = tinymce_models.HTMLField(null=True, blank=True, max_length=5000)
    Runyi_solutions = tinymce_models.HTMLField(null=True, blank=True, max_length = 5000)
                
    #Manager_report
    Manager_report_title = models.CharField(null=True, blank=True, max_length=100)
    Manager_report = tinymce_models.HTMLField(null=True, blank=True, max_length=5000)
    Manager_challenges = tinymce_models.HTMLField(null=True, blank=True, max_length=5000)
    Manager_solutions = tinymce_models.HTMLField(null=True, blank=True, max_length = 5000)

    Ict_report_Title = models.CharField(null=True, blank=True, max_length=100)
    Ict_report = tinymce_models.HTMLField(null=True, blank=True, max_length=5000)
    Ict_challenges = tinymce_models.HTMLField(null=True, blank=True, max_length=5000)
    Ict_solutions = tinymce_models.HTMLField(null=True, blank=True, max_length = 5000)

    Admin_report_title = models.CharField(null=True, blank=True, max_length=500)
    Admin_report_details = tinymce_models.HTMLField(null=True, blank=True, max_length = 5000)
    Admin_challenges = tinymce_models.HTMLField(null=True, blank=True, max_length = 5000)
    Admin_solutions = tinymce_models.HTMLField(null=True, blank=True, max_length = 5000)

    Account_report_title = models.CharField(null=True, blank=True, max_length=500)
    Account_report_details = tinymce_models.HTMLField(null=True, blank=True, max_length = 5000)
    Account_challenges = tinymce_models.HTMLField(null=True, blank=True, max_length = 5000)
    Account_solutions = tinymce_models.HTMLField(null=True, blank=True, max_length = 5000)

    Maintenance_report_title = models.CharField(null=True, blank=True, max_length=500)
    Maintenacne_report_details = tinymce_models.HTMLField(null=True, blank=True, max_length = 5000)
    Maintenance_challenges = tinymce_models.HTMLField(null=True, blank=True, max_length = 5000)
    Maintenance_solutions = tinymce_models.HTMLField(null=True, blank=True, max_length = 5000)

    Manager_report_title_PH = models.CharField(null=True, blank=True, max_length=200, verbose_name="Report Title")
    Manager_report_PH = tinymce_models.HTMLField(null=True, blank=True, max_length=5000, verbose_name="Report Details")
    Manager_challenges_PH = tinymce_models.HTMLField(null=True, blank=True, max_length=5000, verbose_name="Challenges")
    Manager_solutions_PH = tinymce_models.HTMLField(null=True, blank=True, max_length=5000, verbose_name="Solutions")

    Categoty = models.CharField(null=True, choices=CATEGORY, max_length=100)

    feedback_chairman = tinymce_models.HTMLField(null=True, blank=True, max_length=1000)

    feedback_operations = tinymce_models.HTMLField(null=True, blank=True, max_length=1000)
    feedback_admin = tinymce_models.HTMLField(null=True, blank=True, max_length=1000)
    feedback_manager = tinymce_models.HTMLField(null=True, blank=True, max_length=1000)
    feedback_runyi = tinymce_models.HTMLField(null=True, blank=True, max_length=1000)
    feedback_Manager_FLM = tinymce_models.HTMLField(null=True, blank=True, max_length=1000)

    #FEED BACK TIME
    timeOperation_feedback = models.DateTimeField(default=None, null = True, blank=True)
    timeAdmin_feedback = models.DateTimeField(default=None, null = True, blank=True)
    timeManagerFlls_feedback = models.DateTimeField(default=None, null = True, blank=True)
    timeGMadmin_feedback = models.DateTimeField(default=None, null = True, blank=True)
    timeChairman_feedback = models.DateTimeField(default=None, null = True, blank=True)
    timeGGM_feedback = models.DateTimeField(default=None, null = True, blank=True)    

    #IF FEEDBACK FROM MANAGEMENT
    operation_given = models.BooleanField(default=False)
    admin_given = models.BooleanField(default=False)
    fllsManager_given = models.BooleanField(default=False)
    managerAdmin_given = models.BooleanField(default=False)
    chairman_given = models.BooleanField(default=False)
    GGM_given = models.BooleanField(default=False)

    #to show when staff view management feedback.
    seen_operations_feedback = models.BooleanField(default=False)    
    seen_admin_feedback = models.BooleanField(default=False)
    seen_manager_flls = models.BooleanField(default=False)
    seen_runyi_feedback = models.BooleanField(default=False)
    seenn_GGM_feedback = models.BooleanField(default=False)  
    seenn_Chairman_feedback = models.BooleanField(default=False)    

    Commectial_Report_Title = models.CharField(null=True, blank=True, max_length=200)
    Commercial_Report = tinymce_models.HTMLField(null = True, blank = True, max_length = 5000, verbose_name = "Report Details")
    Commercial_Challenges = tinymce_models.HTMLField(null = True, blank = True, max_length = 5000, verbose_name = "Challenges")
    Commercial_Accomplishment = tinymce_models.HTMLField(null = True, blank = True, max_length = 5000, verbose_name = "Acomplishment")
    Commercial_Breakdown = tinymce_models.HTMLField(null = True, blank = True, max_length = 5000, verbose_name = "Break Down")
    Commercial_Balance = tinymce_models.HTMLField(null = True, blank = True, max_length = 5000, verbose_name = "Company GOV | Total truck out | Stock balance")

    operations_seen = models.BooleanField(default=False)
    chairman_seen = models.BooleanField(default=False)
    admin_seen = models.BooleanField(default=False)
    manager_seen = models.BooleanField(default=False)
    runyi_seen = models.BooleanField(default=False)
    manager_flm_seen = models.BooleanField(default=False)

    attended_to = models.BooleanField(default=False)
    ticket_num = models.CharField(null=True, max_length=5)    

    TimeSeenOperations_feedback = models.DateTimeField(default=None, null = True, blank=True)
    TimeSeenAdmin_feedback = models.DateTimeField(default=None, null = True, blank=True)
    TimeSeenManagerFlls_feedback = models.DateTimeField(default=None, null = True, blank=True)
    TimeSeenRunyi_feedback = models.DateTimeField(default=None, null = True, blank=True)
    TimeSeenGGM_feedback = models.DateTimeField(default=None, null = True, blank=True)
    TimeSeenChairman_feedback = models.DateTimeField(default=None, null = True, blank=True)

    date_created = models.DateTimeField(default=timezone.now, null=True)

    for_mangerFLLS = models.BooleanField(default=False)
    for_chairman_manager = models.BooleanField(default=False)
    for_manager_FLM = models.BooleanField(default=False, verbose_name="For GGM")
    for_admin = models.BooleanField(default=False, )
    for_operation = models.BooleanField(default=False, verbose_name="For Manager Operation")
    for_runyi = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.customer}, Order ID:{self.Categoty}, {self.ticket_num}'   

    class Meta:
        ordering = ('-date_created',)

class Management_Notification(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    notification_message = models.CharField(null=True, max_length=100)
    notification_ID = models.CharField(null=True, max_length=5)
    viewed = models.BooleanField(null=True, default=False)
    date_created = models.DateTimeField(default=timezone.now, null=True)

