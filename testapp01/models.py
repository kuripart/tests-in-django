from django.db import models
from django.db.models.fields import IntegerField

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    
    def __unicode__(self):
      return self.first_name + ' ' + self.last_name

class Customer(models.Model):
    name = models.CharField(max_length=30)
    email = models.TextField
    dob = models.DateField
    age = models.IntegerField
    extra = models.SlugField