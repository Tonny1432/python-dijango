from django.db import models
class loan(models.Model):
    name = models.CharField(max_length=100)
    age =models.IntegerField()
    job =models.CharField(max_length=100)
    hosuing_loan =models.CharField(max_length=50)
    personal_loan = models.CharField(max_length=50)
    camping = models.IntegerField()
    poutcomes =models.IntegerField()
# Create your models here.
