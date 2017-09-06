# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

class TinyTrackerReport(models.Model):
    date = models.DateTimeField()
    value = models.TextField()
    state = models.TextField()

    def __str__(self):
        return "Value: " + self.value + ", State: " + self.state + ", Date: " + str(self.date)
