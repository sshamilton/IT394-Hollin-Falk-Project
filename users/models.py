from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.db import models

class Company(models.Model):
    shortname = models.CharField(max_length=1) #A, B, C, etc.
    longname = models.CharField(max_length=50) #Alpha, Bravo, Charlie etc.
    regiment = models.IntegerField() #1,2,3,4
    motto = models.CharField(max_length=100) #Go Buffs!  Go Greeks, etc.
    mascot = models.CharField(max_length=100) #Buffalos, Greeks.

    def __str__(self):
        return (self.shortname + "-" + str(self.regiment))

class Cadet(models.Model):
    first = models.CharField(max_length=200)
    last = models.CharField(max_length=200)
    xnumber = models.CharField(max_length=8)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=1)

    def name(self):
        return (self.last + ", " + self.first)
    def __str__(self):
        return (self.last + ", " + self.first)
