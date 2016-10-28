from __future__ import unicode_literals

from django.db import models
import json


# Create your models here.
class UserInfo(models.Model):
    user_name = models.CharField(max_length=10, default="anonymous")
    last_time = models.IntegerField(default=0)
    password = models.CharField(max_length=10)

    def toJSON(self):
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))
