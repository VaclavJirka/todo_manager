"""This module contains the URL configuration for the tasks app."""

from django.urls import path

from . import views

urlpatterns = [
    path("", views.ListCreateTaskAPIView.as_view(), name="task-list-create"),
    path(
        "<int:id>/",
        views.RetrieveUpdateDestroyTaskAPIView.as_view(),
        name="task-retrieve-update-destroy",
    ),
    path(
        "nearest-deadline/",
        views.NearestDueDateTaskAPIView.as_view(),
        name="task-nearest-due-date",
    ),
]
