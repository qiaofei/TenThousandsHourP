from __future__ import unicode_literals

from django.db import models


# Create your models here.
class UserInfo(models.Model):
    user_name = models.CharField(max_length=10, default="anonymous")
    last_time = models.TimeField(max_length=30, default=0)
