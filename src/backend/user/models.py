from django.db import models
import datetime
class User(models.Model):
    ID = models.IntegerField(primary_key=True)
    S_OP_IP_Cus = models.CharField(max_length=50, null=False)
    S_ME_CI_Nam = models.CharField(max_length=10, null=False)
    S_ME_CI_Sex = models.BooleanField()
    S_ME_CI_Bir = models.DateField()
    S_ME_CI_PW = models.CharField(max_length=20, null=False)
class Info(models.Model):
    S_OP_IP_Cus = models.CharField(max_length=50, null=False)
    S_OP_IP_Che = models.DateField(default=datetime.date)
    S_ME_CI_Nam = models.CharField(max_length=10, null=False)
    S_ME_CI_Sex = models.BooleanField()
    S_ME_CI_Bir = models.DateField()
    S_OP_IP_Bal = models.FloatField()
    S_OP_IP_Bal1 = models.FloatField()
    S_OP_IP_Axe = models.IntegerField()
    S_OP_IP_Axe1 = models.IntegerField()
    S_OP_IP_Pos = models.FloatField()
    S_OP_IP_Pos1 = models.FloatField()
    Eq_Degree = models.FloatField()
    Eq_Degree1 = models.FloatField()
    Age = models.IntegerField()
class Admin(models.Model):
    ID = models.IntegerField(primary_key=True)
    Admin_Name = models.CharField(max_length=10, null=False)
    Admin_PW = models.CharField(max_length=20, null=False)
class Prediction(models.Model):
    ID = models.CharField(max_length=40, primary_key=True, null=False)
    Age = models.IntegerField()
    year0left = models.CharField(max_length=10)
    year0right = models.CharField(max_length=10)
    year1left = models.CharField(max_length=10)
    year1right = models.CharField(max_length=10)
    year2left = models.CharField(max_length=10)
    year2right = models.CharField(max_length=10)
    year3left = models.CharField(max_length=10)
    year3right = models.CharField(max_length=10)
    year4left = models.CharField(max_length=10)
    year4right = models.CharField(max_length=10)
    year5left = models.CharField(max_length=10)
    year5right = models.CharField(max_length=10)
    year6left = models.CharField(max_length=10)
    year6right = models.CharField(max_length=10)
    year7left = models.CharField(max_length=10)
    year7right = models.CharField(max_length=10)
    year8left = models.CharField(max_length=10)
    year8right = models.CharField(max_length=10)
class Stat(models.Model):
    id = models.IntegerField(primary_key=True)
    female = models.IntegerField()
    male = models.IntegerField()
    age0to12 = models.IntegerField()
    age12to18 = models.IntegerField()
    age18to24 = models.IntegerField()
    age24to = models.IntegerField()