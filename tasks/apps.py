"""This module contains the configuration of the tasks app."""

from django.apps import AppConfig


class TasksConfig(AppConfig):
    """The TasksConfig class defines the configuration of the tasks app."""

    default_auto_field: str = "django.db.models.BigAutoField"
    name: str = "tasks"
