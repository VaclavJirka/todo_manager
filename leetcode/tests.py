"""This module contains the tests for the leetcode application."""

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


class AlgorithmViewsTests(TestCase):
    """Tests for the views of the leetcode application."""

    def setUp(self) -> None:
        """Set up the client and the URLs for the tests."""
        self.client = APIClient()
        self.rotate_array_url = reverse("rotate_array")
        self.kth_largest_url = reverse("kth_largest")
        self.longest_increasing_path_url = reverse("longest_increasing_path")

    def test_rotate_array(self) -> None:
        """Test the rotate_array view."""
        data = {"nums": [1, 2, 3, 4, 5, 6, 7], "k": 3}
        response = self.client.post(self.rotate_array_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [5, 6, 7, 1, 2, 3, 4])

    def test_kth_largest(self) -> None:
        """Test the kth_largest view."""
        data = {"nums": [3, 2, 1, 5, 6, 4], "k": 2}
        response = self.client.post(self.kth_largest_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, 5)

    def test_longest_increasing_path(self) -> None:
        """Test the longest_increasing_path view."""
        data = {"matrix": [[9, 9, 4], [6, 6, 8], [2, 1, 1]]}
        response = self.client.post(
            self.longest_increasing_path_url, data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, 4)
