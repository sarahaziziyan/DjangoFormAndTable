from django.db import models
import datetime

class PersonalInfo(models.Model):
    nationalCode = models.CharField(max_length=10,primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    genderType = ( ('M','Male') , ('F','Female') )
    gender = models.CharField(choices=genderType,default='M', max_length=1)    
    date_of_birth = models.DateField()