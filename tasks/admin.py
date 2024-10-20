"""This module registers the Task model with the Django admin site."""

from django.contrib import admin

from .models import Task

admin.site.register(Task)
