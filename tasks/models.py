"""This module contains the Task model for the todo_manager application."""

from django.db import models


class Task(models.Model):
    """
    A model to represent a task.

    Attributes:
        title: The title of the task.
        description: The description of the task.
        due_date: The due date of the task.
        photo: The photo associated with the task.
    """

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, max_length=500)
    due_date = models.DateField(blank=True, null=True)
    photo = models.ImageField(blank=True, null=True, upload_to="images/")

    def __str__(self):
        """Return the title of the task."""
        return self.title
