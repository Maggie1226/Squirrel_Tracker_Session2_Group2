from django.db import models

class squirrel_site(models.Model):
    Latitude=models.FloatField(max_length=100,)
    
    Longitude=models.FloatField(max_length=100,)
    
    Unique_Squirrel_ID=models.CharField(max_length=20,primary_key=True,unique=True,)
    
    AM="AM"
    PM="PM"
    Shift_CHOICES=[(AM,"AM"),(PM,"PM"),]
    Shift=models.CharField(max_length=2,choices=Shift_CHOICES,default=AM,)
    
    Date=models.DateField(auto_now=False,)
    
    Adult="Adult"
    Juvenile="Juvenile"
    Age_CHOICES=[(Adult,"Adult"),(Juvenile,"Juvenile"),]
    Age=models.CharField(max_length=10,choices=Age_CHOICES,default=Adult,)
    
    Gray="Gray"
    Cinnamon="Cinnamon"
    Black="Black"
    Fur_CHOICES=[(Gray,"Gray"),(Cinnamon,"Cinnamon"),(Black,"Black"),]
    Primary_fur_color=models.CharField(max_length=10,choices=Fur_CHOICES,default=Gray,)
    
    Ground_Plane="GP"
    Above_Ground="AG"
    Location_CHOICES=[(Ground_Plane,"Ground Plane"),(Above_Ground,"Above Ground"),]
    Location=models.CharField(max_length=20,choices=Location_CHOICES,default=Ground_Plane,)

    Specific_location=models.TextField(max_length=500,blank=True)
    
    Running=models.BooleanField(default=False,)

    Chasing=models.BooleanField(default=False,)

    Climbing=models.BooleanField(default=False,)

    Eating=models.BooleanField(default=False,)

    Foraging=models.BooleanField(default=False,)

    Other_activities=models.TextField(max_length=500,blank=True)

    Kuks=models.BooleanField(default=False,)

    Quaas=models.BooleanField(default=False,)

    Moans=models.BooleanField(default=False,)

    Tail_flags=models.BooleanField(default=False,)

    Tail_twitches=models.BooleanField(default=False,)

    Approaches=models.BooleanField(default=False,)

    Indifferent=models.BooleanField(default=False,)

    Runs_from=models.BooleanField(default=False,)

    Other_interactions=models.TextField(max_length=500,blank=True)


# Create your models here.
