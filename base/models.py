from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
    
class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200,null=True,blank=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Tasks(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200,null=True,blank=True)
    project = models.ForeignKey(Project,on_delete=models.CASCADE,related_name="tasks")
    users = models.ManyToManyField(User)
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name   