"""This module contains the configuration of the leetcode app."""

from django.apps import AppConfig


class LeetcodeConfig(AppConfig):
    """Configuration class for the LeetCode app."""

    default_auto_field: str = "django.db.models.BigAutoField"
    name: str = "leetcode"
