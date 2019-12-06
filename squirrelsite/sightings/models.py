from django.db import models

class squirrel_site(models.Model):
    Latitude=models.FloatField(max_length=100,)
    
    Longtitude=models.FloatField(max_length=100,)
    
    Unique_Squirrel_ID=models.CharField(max_length=20,primary_key=True,unique=True,)
    
    AM="AM"
    PM="PM"
    Shift_CHOICES=[(AM,"AM"),(PM,"PM"),]
    Shift=models.CharField(max_length=2,choices=Shift_CHOICES,default=AM,)
    
    Date=models.CharField(max_length=10,)
    
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

    Specific_location=models.TextField(max_length=500,)
    
    Running=models.BooleanField(default=True,)

    Chasing=models.BooleanField(default=True,)

    Climbing=models.BooleanField(default=True,)

    Eating=models.BooleanField(default=True,)

    Foraging=models.BooleanField(default=True,)

    Other_activities=models.TextField(max_length=500,)

    Kuks=models.BooleanField(default=True,)

    Quaas=models.BooleanField(default=True,)

    Moans=models.BooleanField(default=True,)

    Tail_flags=models.BooleanField(default=True,)

    Tail_twitches=models.BooleanField(default=True,)

    Approaches=models.BooleanField(default=True,)

    Indifferent=models.BooleanField(default=True,)

    Runs_from=models.BooleanField(default=True,)

    Other_interactions=models.TextField(max_length=500,)


# Create your models here.
