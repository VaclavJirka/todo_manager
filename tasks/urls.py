"""This module contains the URL configuration for the tasks app."""

from typing import List

from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns: List[URLPattern] = [
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
