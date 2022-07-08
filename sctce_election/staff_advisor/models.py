from unicodedata import name
from django.db import models

# Create your models here.


class student_detail(models.Model):
    gender_choices = (
        ('F', 'female'),
        ('M', 'male'),
        ('O', 'others')
    ),

    name = models.CharField(max_length = 30, null = True)
    roll_no = models.IntegerField()
    adm_no  = models.IntegerField()
    department = models.CharField(max_length = 30)
    year = models.IntegerField()
    gender = models.CharField(max_length = 10)

    def __str__(self):
        return self.name + ' (' +str(self.roll_no)+', '+self.department +')'