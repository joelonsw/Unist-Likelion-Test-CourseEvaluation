from django.db import models

# Create your models here.
class lecture(models.Model):
    prof = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    codeNum = models.CharField(max_length=20)


    def __str__(self):
        return self.name


class evaluation(models.Model):
    subject = models.CharField(default='주제', max_length=50)
    star = models.IntegerField(default=5)
    text = models.TextField()
    password = models.IntegerField(default= 0000, max_length=10)
