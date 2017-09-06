# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Todo, TinyTrackerReport

admin.site.register(Todo)
admin.site.register(TinyTrackerReport)

# Register your models here.
