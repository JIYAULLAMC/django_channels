from django.db import models

# Create your models here.






class Group(models.Model):
    name = models.CharField(max_length=30, unique=True)






class Chat(models.Model):
    content = models.CharField(max_length=100)
    time_stamp = models.DateTimeField(auto_now=True)
    group = models.ForeignKey('Group', on_delete=models.CASCADE)



