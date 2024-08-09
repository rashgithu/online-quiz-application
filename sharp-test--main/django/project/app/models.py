from django.db import models
from django.contrib.auth.models import User

class Register(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = 'signup'




class Exam (models.Model):
        Question =models.CharField(max_length=255)
        option1=models.CharField(max_length=255)
        option2=models.CharField(max_length=255)
        option3=models.CharField(max_length=255)
        option4=models.CharField(max_length=255)
        correct=models.CharField(max_length=255)
        
        #class Meta:    
         #   db_table="exam"
class Gk (models.Model):
        Question =models.CharField(max_length=255)
        option1=models.CharField(max_length=255)
        option2=models.CharField(max_length=255)
        option3=models.CharField(max_length=255)
        option4=models.CharField(max_length=255)
        correct=models.CharField(max_length=255)
        marks=models.CharField(max_length=255)             


class Django (models.Model):
        Question =models.CharField(max_length=255)
        option1=models.CharField(max_length=255)
        option2=models.CharField(max_length=255)
        option3=models.CharField(max_length=255)
        option4=models.CharField(max_length=255)
        correct=models.CharField(max_length=255)
        marks=models.CharField(max_length=255) 


class Answer(models.Model):
        question =models.ForeignKey(Django,on_delete=models.CASCADE)     
        text=models.CharField(max_length=255)
        is_correct = models.BooleanField(default=False)  
        marks1=models.IntegerField(default=0) 

                               