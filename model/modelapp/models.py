from django.db import models


class Van(models.Model):
    vname = models.CharField(max_length=12,null=True,blank=True)
    vcost = models.IntegerField(null=True,blank=True)
    

class Person(models.Model):
    van = models.OneToOneField(Van,on_delete=models.CASCADE)
    name = models.CharField(max_length=12,null=True,blank=True)
    city = models.CharField(max_length=12,null=True,blank=True)
    phone = models.IntegerField(null=True,blank=True)
    
    def __str__(self):
        return self.van.vname