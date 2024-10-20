"""This module contains the configuration of the leetcode app."""

from django.apps import AppConfig


class LeetcodeConfig(AppConfig):
    """
    Configuration class for the LeetCode app.

    Attributes:
        default_auto_field: The default auto field for the app.
        name: The name of the app.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "leetcode"
