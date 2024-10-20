"""This module contains the URL configuration for the leetcode app."""

from django.urls import path

from . import views


urlpatterns = [
    path("rotate-array/", views.rotate_array_view, name="rotate_array"),
    path("kth-largest/", views.kth_largest_view, name="kth_largest"),
    path(
        "longest-increasing-path/",
        views.longest_increasing_path_view,
        name="longest_increasing_path",
    ),
]
