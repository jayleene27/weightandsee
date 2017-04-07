# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    userID = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    bodyWeight = models.IntegerField()
    squatMax = models.IntegerField(null=True)
    benchMax = models.IntegerField(null=True)
    deadliftMax = models.IntegerField(null=True)
    snatchMax = models.IntegerField(null=True)
    cleanMax = models.IntegerField(null=True)
    goals = models.CharField(max_length=240)
    
class Exercises(models.Model):
    exID = models.AutoField(primary_key=True)
    orderNum = models.IntegerField()
    purpose = models.CharField(max_length=240)
    main = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    alt1 = models.CharField(max_length=30)
    alt2 = models.CharField(max_length=30)
    alt3 = models.CharField(max_length=30)
    
class UserDoesExercise(models.Model):
    usr = models.ForiegnKey(User, on_delete=models.CASCADE)
    exercise = models.ForiegnKey(Exercises, on_delete=models.CASCADE)
    phase = models.IntegerField()
    date = models.DateField()
    exMax = models.IntegerField()
