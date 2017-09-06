# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Todo, TinyTrackerReport

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title','text','created_at')
    search_fields = ['title']

admin.site.register(Todo,TodoAdmin)
admin.site.register(TinyTrackerReport)
