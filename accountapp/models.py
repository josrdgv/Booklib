from django.db import models

# Create your models here.
class userReg(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    password1=models.CharField(max_length=200)
    def __str__(self):
        return '{}'.format(self.username)
class loginuser(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    password1 = models.CharField(max_length=200)
    type=models.CharField(max_length=200)
    def __str__(self):
        return '{}'.format(self.username)