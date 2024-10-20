"""This module contains the tests for the tasks app."""

from django.core.files.storage import default_storage
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from PIL import Image
from rest_framework.test import APITestCase
from rest_framework import status

from tasks.models import Task


class TaskListCreateTestCase(APITestCase):
    """This class defines the tests for the task list and create view."""

    def setUp(self) -> None:
        """Create a task object with the given data."""
        self.url = reverse("task-list-create")
        self.data = {
            "title": "Test task",
            "description": "Test description",
            "due_date": "2024-10-17",
        }

    def test_create_task(self) -> None:
        """Test creating a task."""
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        task = Task.objects.first()
        self.assertEqual(task.title, self.data["title"])
        self.assertEqual(task.description, self.data["description"])
        self.assertEqual(str(task.due_date), self.data["due_date"])

    def test_list_tasks(self) -> None:
        """Test listing tasks."""
        task = Task.objects.create(**self.data)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], task.title)
        self.assertEqual(response.data[0]["description"], task.description)
        self.assertEqual(response.data[0]["due_date"], str(task.due_date))

    def test_upload_photo(self) -> None:
        """Test creating a task with uploading a photo."""
        with open("tasks/tests/photos/testing_photo.jpg", "rb") as photo:
            image_data = SimpleUploadedFile(
                photo.name, photo.read(), content_type="image/jpeg"
            )
            self.data["photo"] = image_data
            response = self.client.post(
                self.url, self.data, format="multipart"
            )
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(Task.objects.count(), 1)
            task = Task.objects.first()
            self.assertTrue(task.photo)
            image = Image.open(task.photo)
            self.assertLessEqual(image.width, 800)
            self.assertLessEqual(image.height, 800)
            self.assertEqual(image.mode, "L")

    def tearDown(self) -> None:
        """Delete the photo files after the tests."""
        tasks = Task.objects.all()
        for task in tasks:
            if task.photo:
                if default_storage.exists(task.photo.path):
                    default_storage.delete(task.photo.path)


class TaskRetrieveUpdateDestroyTestCase(APITestCase):
    """
    Tests for the task retrieve, update, and destroy view.

    This class defines the tests for retrieving, updating, and deleting tasks.
    """

    def setUp(self) -> None:
        """Create a task object with the given data."""
        self.task = Task.objects.create(
            title="Test task",
            description="Test description",
            due_date="2024-10-17",
        )
        self.url = reverse(
            "task-retrieve-update-destroy", kwargs={"id": self.task.id}
        )
        self.data = {
            "title": "Updated task",
            "description": "Updated description",
            "due_date": "2024-10-18",
        }

    def test_retrieve_task(self) -> None:
        """Test retrieving a task."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.task.title)
        self.assertEqual(response.data["description"], self.task.description)
        self.assertEqual(response.data["due_date"], str(self.task.due_date))

    def test_update_task(self) -> None:
        """Test updating a task."""
        response = self.client.put(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        task = Task.objects.get(id=self.task.id)
        self.assertEqual(task.title, self.data["title"])
        self.assertEqual(task.description, self.data["description"])
        self.assertEqual(str(task.due_date), self.data["due_date"])

    def test_delete_task(self) -> None:
        """Test deleting a task."""
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)

    def test_update_photo(self) -> None:
        """Test updating a task with uploading a photo."""
        with open("tasks/tests/photos/testing_photo.jpg", "rb") as photo:
            image_data = SimpleUploadedFile(
                photo.name, photo.read(), content_type="image/jpeg"
            )
            self.data["photo"] = image_data
            response = self.client.put(self.url, self.data, format="multipart")
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.task.refresh_from_db()
            self.assertTrue(self.task.photo)
            image = Image.open(self.task.photo)
            self.assertLessEqual(image.width, 800)
            self.assertLessEqual(image.height, 800)
            self.assertEqual(image.mode, "L")

    def tearDown(self) -> None:
        """Delete the photo files after the tests."""
        if self.task.photo:
            if default_storage.exists(self.task.photo.path):
                default_storage.delete(self.task.photo.path)


class NearestDueDateTaskTestCase(APITestCase):
    """This class defines the tests for the nearest due date view."""

    def setUp(self) -> None:
        """Create the URL for the task with the nearest due date view."""
        self.url = reverse("task-nearest-due-date")

    def test_nearest_due_date(self) -> None:
        """Test retrieving the task with the nearest due date."""
        task1 = Task.objects.create(
            title="Test task 1",
            description="Test description 1",
            due_date="2024-10-17",
        )
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], task1.title)
        self.assertEqual(response.data["description"], task1.description)
        self.assertEqual(response.data["due_date"], str(task1.due_date))
