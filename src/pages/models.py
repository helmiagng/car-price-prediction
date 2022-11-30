# Create your models here.
from django.db import models
from django.urls import reverse
import pandas as pd
import pickle

# Create your models here.
class PredictPrice(models.Model):

    fuel_types         = models.CharField(blank=False,max_length=120,null=True)  
    aspiration         = models.CharField(blank=False,max_length=120,null=True)
    carbody            = models.CharField(blank=False,max_length=120,null=True)
    drivewheel         = models.CharField(blank=False,max_length=120,null=True)
    enginelocation     = models.CharField(blank=False,max_length=120,null=True)
    enginetype         = models.CharField(blank=False,max_length=120,null=True)
    fuelsystem         = models.CharField(blank=False,max_length=120,null=True)                                         
   

    car_type          = models.CharField(blank=False,max_length=120)
    doornumber        = models.IntegerField(blank=False,null=True)
    wheelbase         = models.FloatField(blank=False,null=True)
    carlength         = models.FloatField(blank=False,null=True)
    carwidth          = models.FloatField(blank=False,null=True)
    carheight         = models.FloatField(blank=False,null=True)
    curbweight        = models.IntegerField(blank=False,null=True)
    cylindernumber    = models.IntegerField(blank=False,null=True)
    enginesize        = models.IntegerField(blank=False,null=True)
    boreratio         = models.FloatField(blank=False,null=True)
    stroke            = models.FloatField(blank=False,null=True)
    compressionratio  = models.FloatField(blank=False,null=True)
    horsepower        = models.IntegerField(blank=False,null=True)
    peakrpm           = models.IntegerField(blank=False,null=True)
    citympg           = models.IntegerField(blank=False,null=True)
    highwaympg        = models.IntegerField(blank=False,null=True)
    car_price         = models.FloatField(blank=True,null=True)

    