from django.db import models
from django.utils import timezone
from users.models import Customer
# Create your models here.

class OFFICE_REPORT(models.Model):
    COMPLETION = [
        (None, None),
        ('Just Started', 'Just Started'),
        ('Far From Completion', 'Far From Completion'),
        ('Almost Completed', 'Almost Completed'),
        ('Completed', 'Completed')
    ]

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
    ]
    
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL, verbose_name="STAFF")

    #Operations
    work_schedule = models.TextField(max_length=500, null=True)
    Work_description = models.CharField(null=True, max_length=100)
    extent_of_completion = models.CharField(null=True, choices= COMPLETION, max_length=100)
    time_taken = models.CharField(null=True, choices=TIME, max_length=100)    
    work_left = models.CharField(null=True, max_length=100)
    challenges = models.TextField(max_length=500, null=True)

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
    Iwh_report_= models.TextField(null=True, max_length=500)
    Iwh_challenges = models.TextField(null=True, blank=True, max_length=500, verbose_name="Challenges")
    Iwh_solutions = models.TextField(null=True, blank=True, max_length=500, verbose_name="Solutions")    

    #ICT    
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

    solutions = models.CharField(max_length=100, null=True)

    operations_seen = models.BooleanField(default=False)
    chairman_seen = models.BooleanField(default=False)
    admin_seen = models.BooleanField(default=False)
    manager_seen = models.BooleanField(default=False)
    runyi_seen = models.BooleanField(default=False)

    attended_to = models.BooleanField(default=False)
    ticket_num = models.CharField(null=True, max_length=5)
    submit = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self):
        return f'{self.customer}, Order ID:{self.Categoty}'

    class Meta:
        ordering = ('-date_created',)

class Management_Notification(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    notification_message = models.CharField(null=True, max_length=100)
    notification_ID = models.CharField(null=True, max_length=5)
    viewed = models.BooleanField(null=True, default=False)
    date_created = models.DateTimeField(default=timezone.now, null=True)
    