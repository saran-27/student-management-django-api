from django.db import models

class StudentPerformance(models.Model):
    student_name=models.CharField(max_length=20)
    tamil=models.IntegerField()
    english=models.IntegerField()
    maths=models.IntegerField()
    science=models.IntegerField()
    computer=models.IntegerField()
    result=models.CharField(max_length=10)
    average=models.FloatField()
    total=models.IntegerField()
