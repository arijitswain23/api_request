from django.db import models

# Create your models here.
class School(models.Model):
    sname=models.CharField(max_length=100)
    sprincepal=models.CharField(max_length=100)
    slocation=models.CharField(max_length=100)
    
    def __str__(self):
        return self.sname