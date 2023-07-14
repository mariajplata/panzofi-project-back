import datetime

from django.db import models
from django.utils import timezone

class User(models.Model):
    username = models.CharField(max_length=80)
    password = models.CharField(max_length=80)
    is_admin = models.BooleanField()

class Session(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    counter_button1 = models.IntegerField(default=0)
    counter_button2 = models.IntegerField(default=0)
