from django.db import models
class students(models.Model):  #models.Model is the base class & students is the child class
     name = models.CharField(max_length=50)
     age = models.IntegerField()
     department =models.CharField(max_length=50)
     reg_no = models.IntegerField()

class subject(models.Model):
     cs = models.IntegerField()
     emf =models.IntegerField()
     vlsi = models.IntegerField()
     trlf = models.IntegerField()
     
     
