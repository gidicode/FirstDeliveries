from django.db import models
from django.utils import timezone
from users.models import Customer
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
    ]
    
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL, verbose_name="STAFF")

    #Operations
    work_schedule = models.TextField(max_length=1000, verbose_name="Task Schedule", blank=True, null=True)
    Work_description = models.TextField(null=True, verbose_name="Main Report", blank=True, max_length=1000)
    extent_of_completion = models.CharField(null=True, verbose_name="Task Completed", blank=True, max_length=1000)
    time_taken = models.TextField(null=True, choices=TIME, max_length=200)    
    work_left = models.TextField(null=True, verbose_name="Task Left", blank=True, max_length=200)
    challenges = models.TextField(max_length=1000, blank=True, null=True)

    #Fleet
    Fleet_report_title = models.CharField(null=True, max_length=100)
    Fleet_report = models.TextField(null=True, max_length=300)
    Fleet_challenges =models.TextField(null=True, max_length=300, blank=True)
    Fleet_solutions = models.CharField(null=True, blank=True, max_length=100)
    
    #Marketing
    Marketing_report_title = models.CharField(null=True, max_length=100)
    Marketing_report = models.TextField(null=True, max_length=300)
    Marketting_challenges =models.TextField(null=True, max_length=300, blank=True)
    Marketing_solutions = models.CharField(null=True, blank=True, max_length=100)

    #Front_desk
    FrontDesk_report_Title = models.CharField(null=True, max_length=100)
    FrontDesk_report = models.TextField(null=True, max_length=300)
    Front_desk_total_rides = models.IntegerField(null=True, verbose_name='Total Rides Today')
    Front_desk_total_amount = models.IntegerField(null=True, verbose_name='Total Amount Today')
    FrontDesk_challenges =models.TextField(null=True, max_length=300, blank=True)
    FrontDesk_solutions = models.CharField(null=True, blank=True, max_length=100)

    #IWH
    Iwh_report_title = models.CharField(null=True, max_length=100)
    Iwh_report = models.TextField(null=True, max_length=500)
    Iwh_challenges = models.TextField(null=True, blank=True, max_length=500, verbose_name="Challenges")
    Iwh_solutions = models.CharField(null=True, blank=True, max_length=500, verbose_name="Solutions")    

    #TankFarm
    Tank_farm_report_title = models.CharField(null=True, max_length=100, verbose_name="Report Title")
    Tank_farm_report = models.TextField(null=True, max_length=500)
    Tank_farm_challenges = models.TextField(null=True, blank=True, max_length=500, verbose_name="Challenges")
    Tank_farm_solutions = models.CharField(null=True, blank=True, max_length=500, verbose_name="Solutions")

    #Runyi
    Runyi_report_Title = models.CharField(null=True, max_length=100)
    Runyi_report = models.TextField(null=True, max_length=300)
    Runyi_challenges = models.TextField(null=True, blank=True, max_length=300)
    Runyi_solutions = models.CharField(null=True, blank=True, max_length=100)

    #Manager_report
    Manager_report_title = models.CharField(null=True, max_length=100)
    Manager_report = models.TextField(null=True, max_length=300)
    Manager_challenges = models.TextField(null=True, blank=True, max_length=300)
    Manager_solutions = models.CharField(null=True, blank=True, max_length=100)   

    Ict_report_Title = models.CharField(null=True, max_length=100)
    Ict_report = models.TextField(null=True, max_length=300)
    Ict_challenges = models.TextField(null=True, blank=True, max_length=300)
    Ict_solutions = models.CharField(null=True, blank=True, max_length=100)   

    Categoty = models.CharField(null=True, choices=CATEGORY, max_length=100)

    feedback_chairman = models.CharField(null=True, max_length=100)
    feedback_operations = models.CharField(null=True, max_length=100)
    feedback_admin = models.CharField(null=True, max_length=100)
    feedback_manager = models.CharField(null=True, max_length=100)
    feedback_runyi = models.CharField(null=True, max_length=100)
    feedback_Manager_FLM = models.CharField(null=True, max_length=100)
    solutions = models.CharField(max_length=100, null=True)

    operations_seen = models.BooleanField(default=False)
    chairman_seen = models.BooleanField(default=False)
    admin_seen = models.BooleanField(default=False)
    manager_seen = models.BooleanField(default=False)
    runyi_seen = models.BooleanField(default=False)
    manager_flm_seen = models.BooleanField(default=False)

    attended_to = models.BooleanField(default=False)
    ticket_num = models.CharField(null=True, max_length=5)    
    date_created = models.DateTimeField(default=timezone.now, null=True)

    for_mangerFLLS = models.BooleanField(default=False)
    for_chairman_manager = models.BooleanField(default=False)
    for_manager_FLM = models.BooleanField(default=False)
    for_admin = models.BooleanField(default=False)
    for_operation = models.BooleanField(default=False)
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
    