from django.db import models
from django.contrib.auth.models import User

class Service(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User)

class Tag(models.Model):
    name = models.CharField(max_length=200)

class Incident(models.Model):
    title = models.CharField(max_length=2000)
    services = models.ManyToManyField(Service)
    prevention = models.TextField()
    tag = models.ManyToManyField(Tag)
    owner = models.ForeignKey(User)

class Update(models.Model):
    incident = models.ForeignKey(Incident)
    text = models.TextField()
    timestamp = models.DateField(auto_now=True)




# Create your models here.
