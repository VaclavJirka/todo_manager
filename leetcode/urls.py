"""This module contains the URL configuration for the leetcode app."""

from typing import List

from django.urls import path
from django.urls.resolvers import URLPattern

from . import views


urlpatterns: List[URLPattern] = [
    path("rotate-array/", views.rotate_array_view, name="rotate_array"),
    path("kth-largest/", views.kth_largest_view, name="kth_largest"),
    path(
        "longest-increasing-path/",
        views.longest_increasing_path_view,
        name="longest_increasing_path",
    ),
]
