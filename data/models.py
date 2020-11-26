from django.db import models

# Create your models here
class Detail(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    date=models.CharField(max_length=10)
    time=models.CharField(max_length=10)
    problem=models.CharField(max_length=22)
    place=models.CharField(max_length=52)
    email=models.EmailField()

    def __str__(self):
        return "request from "+self.email+" by " +self.name   