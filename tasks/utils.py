"""This module contains utility functions for the tasks app."""

import uuid

import cv2 as cv
from django.core.files.base import ContentFile
import numpy as np


def change_dimensions(image_array, max_width=800, max_height=800):
    """Change image dimensions if they exceed the maximum width or height."""
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


def change_to_black_and_white(image_array):
    """Change the image to black and white."""
    return cv.cvtColor(image_array, cv.COLOR_BGR2GRAY)


def create_name():
    """Create a unique name for the image file."""
    return str(uuid.uuid4())[:8] + ".jpg"


def convert(image):
    """Convert the image and return a ContentFile object."""
    name = image.name
    print(name)
    image = cv.imdecode(
        np.fromstring(image.read(), np.uint8), cv.IMREAD_UNCHANGED
    )
    image = change_dimensions(image)
    image = change_to_black_and_white(image)
    _, buffer = cv.imencode(".jpg", image)
    content_file = ContentFile(buffer.tobytes(), name=create_name())
    return content_file
