"""This module contains utility functions for the tasks app."""

import uuid

import cv2 as cv
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
import numpy as np


def change_dimensions(
    image_array: np.ndarray, max_width: int = 800, max_height: int = 800
) -> np.ndarray:
    """
    Change image dimensions if they exceed the maximum width or height.

    Args:
        image_array (numpy.ndarray): Image array.
        max_width (int): Maximum width.
        max_height (int): Maximum height.

    Returns:
        numpy.ndarray: Image array.
    """
    height, width = image_array.shape[:2]
    if height > max_height or width > max_width:
        if height > width:
            new_height = max_height
            new_width = int(width * (new_height / height))
        else:
            new_width = max_width
            new_height = int(height * (new_width / width))
        image_array = cv.resize(image_array, (new_width, new_height))
    return image_array


def change_to_black_and_white(image_array: np.ndarray) -> np.ndarray:
    """
    Change the image to black and white.

    Args:
        image_array (numpy.ndarray): Image array.

    Returns:
        numpy.ndarray: Image array.
    """
    return cv.cvtColor(image_array, cv.COLOR_BGR2GRAY)


def create_name() -> str:
    """
    Create a unique name for the image file.

    Returns:
        str: Unique name.
    """
    return str(uuid.uuid4())[:8] + ".jpg"


def convert(image: InMemoryUploadedFile) -> ContentFile:
    """
    Convert the image and return a ContentFile object.

    Args:
        image (InMemoryUploadedFile): Image file.

    Returns:
        django.core.files.base.ContentFile: Content file.
    """
    image_data = image.read()
    image_array = np.frombuffer(image_data, np.uint8)
    image = cv.imdecode(image_array, cv.IMREAD_UNCHANGED)
    image = change_dimensions(image)
    image = change_to_black_and_white(image)
    _, buffer = cv.imencode(".jpg", image)
    content_file = ContentFile(buffer.tobytes(), name=create_name())
    return content_file
