from django.db import models
# from django.db.models.fields import EmailField

# Create your models here.

class student(models.Model):
    stuid=models.IntegerField(primary_key=True)
    stuname=models.CharField(max_length=70)
    stuemail=models.EmailField(max_length=70)
    stupass=models.CharField(max_length=70)


   