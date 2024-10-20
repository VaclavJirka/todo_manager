"""This module defines the serialization of the Task model."""

from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """The TaskSerializer class defines the serialization of the Task model."""

    class Meta:
        """The Meta class defines the metadata of the TaskSerializer class."""

        model = Task
        fields = "__all__"
