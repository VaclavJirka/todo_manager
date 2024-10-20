"""This module contains the views for the tasks app."""

from rest_framework import generics

from .models import Task
from .serializers import TaskSerializer
from .utils import convert


class ListCreateTaskAPIView(generics.ListCreateAPIView):
    """This class defines the view for listing and creating tasks."""

    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
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
    """This class defines the view for retrieving, updating, and deleting a task."""

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = "id"

    def perform_update(self, serializer):
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

    def perform_destroy(self, instance):
        """Delete the photo and the task object."""
        instance.photo.delete()
        instance.delete()


class NearestDueDateTaskAPIView(generics.RetrieveAPIView):
    """This class defines the view for retrieving the task with the nearest due date."""

    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_object(self):
        """Return the task with the nearest due date."""
        return Task.objects.order_by("due_date").first()
