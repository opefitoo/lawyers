from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Avocat(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    job_position = models.CharField(max_length=20)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name + " " + self.first_name
    
class Assistant(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    job_position = models.CharField(max_length=20)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.user 

class Client(models.Model):
    first_name = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    address = models.TextField(max_length=30)
    zipcode = models.CharField(max_length=10)
    city = models.CharField(max_length= 30)
    phone_number = models.CharField(max_length=30)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name + " " + self.first_name
    
class Adversaire(models.Model):
    first_name = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    address = models.TextField(max_length=30)
    zipcode = models.CharField(max_length=10)
    city = models.CharField(max_length= 30)
    phone_number = models.CharField(max_length=30)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name + " " + self.first_name

class PartieAdverse(models.Model):
    name = models.CharField(max_length=30)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name
    
class Dossier(models.Model):
    TRIBUNAL_ADMINISTRATIF = 'ADM'
    CIVIL = 'CIV'
    TRIBUNAL_TRAVAIL = 'TRV'
    MATIERE_JURIDIQUE = (
        (TRIBUNAL_ADMINISTRATIF       , 'Tribunal administratif'),
        (CIVIL, 'Tribunal civil'),
        (TRIBUNAL_TRAVAIL, 'Tribunal du travail'),
    )
    
    client = models.ForeignKey(Client)
    partie_adverse = models.ForeignKey(PartieAdverse)
    adversaire = models.ForeignKey(Adversaire)
    date_ouverture = models.DateField()
    matiere =  models.CharField(max_length=2,
                                      choices=MATIERE_JURIDIQUE,
                                      default=CIVIL)
    type = models.CharField(max_length=15)
    avocat1 = models.ForeignKey(Avocat)
#     avocat2 = models.ForeignKey(Avocat)
    assistant = models.ForeignKey(Assistant)
    echeance = models.DateField()
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.client + "vs." + self.partie_adverse

