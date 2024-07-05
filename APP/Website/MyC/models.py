from django.db import models

# Create your models here.
class Member(models.Model):
    
    name = models.CharField(max_length=300)

    MY_CHOICES =(

        ('a','Standard'),
        ('b','Premium'),
        ('a','Deluxe'),

    )

    membership_plan = models.CharField(max_length=1, choices= MY_CHOICES)

    unique_code = models.CharField(max_length=300)

class Agensi(models.Model):
    
    Email = models.CharField(max_length=300)

    Agensi_Choice=(

        ('a','JKDM'),
        ('b','JANM'),
        ('a','JPPH'),
        ('b','LADA'),
        ('a','PERB'),
       
    )

    agensi_plan = models.CharField(max_length=1, choices= Agensi_Choice)

    unique_code = models.CharField(max_length=300)
    
    