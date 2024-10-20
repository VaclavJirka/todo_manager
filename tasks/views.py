"""This module contains the views for the tasks app."""

from typing import Optional

from rest_framework import generics
from rest_framework.serializers import BaseSerializer

from .models import Task
from .serializers import TaskSerializer
from .utils import convert


class ListCreateTaskAPIView(generics.ListCreateAPIView):
    """This class defines the view for listing and creating tasks."""

    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer: BaseSerializer) -> None:
        """
        Convert to maximum 800px width and height if needed.
        Convert it to black and white.

        Create a task object and save the uploaded photo if given.
        """
        uploaded_photo = self.request.FILES.get("photo")
        if uploaded_photo:
            content_file = convert(uploaded_photo)
            serializer.save(photo=content_file)
        else:
            serializer.save()


class RetrieveUpdateDestroyTaskAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Defines view for retrieving, updating, and deleting a task."""

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = "id"

    def perform_update(self, serializer: BaseSerializer) -> None:
        """
        Convert to maximum 800px width and height if needed.
        Convert it to black and white.

        Update the task object and save the uploaded photo if given.
        """
        uploaded_photo = self.request.FILES.get("photo")

        if uploaded_photo:
            content_file = convert(uploaded_photo)
            serializer.save(photo=content_file)
        else:
            serializer.save()

    def perform_destroy(self, instance: Task) -> None:
        """Delete the photo and the task object."""
        instance.photo.delete()
        instance.delete()


class NearestDueDateTaskAPIView(generics.RetrieveAPIView):
    """This class defines view for retrieving task with nearest due date."""

    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_object(self) -> Optional[Task]:
        """Return the task with the nearest due date."""
        return (
            Task.objects.filter(due_date__isnull=False)
            .order_by("due_date")
            .first()
        )
