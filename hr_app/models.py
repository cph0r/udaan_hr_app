from django.db import models

# Create your models here.
from django.forms import forms


class UserInfo(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    photo = models.ImageField(upload_to='images/')

    TYPES = (
        ('Employed', 'Employed'),
        ('Unemployed', 'Unemployed'),
        ('Student', 'Student')
    )
    type = models.CharField(max_length=11, choices=TYPES)
    status = models.CharField(max_length=20, default='Pending')

    employed_count = models.IntegerField(default= 0)
    unemployed_count = models.IntegerField(default=0)
    student_count = models.IntegerField(default=0)
