from django.db import models

# Create your models here.
class todo(models.Model):
    text=models.CharField(max_length= 100)

class question(models.Model):
    question_text=models.CharField(max_length=200)
    date_sub=models.DateTimeField()
    

class choice(models.Model):
    question=models.ForeignKey(question,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)




