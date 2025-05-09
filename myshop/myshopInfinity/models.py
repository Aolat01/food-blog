from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver 

# Create your models here.
class myshop (models.Model):
    title = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updatd_at = models.DateTimeField(auto_now=True)
    complete_payment = models.BooleanField(default=True)


    def __str__(self):
        return self.title