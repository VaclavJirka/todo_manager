"""This module contains the views for the leetcode app."""

from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from .serializers import (
    RotateArraySerializer,
    KthLargestSerializer,
    LongestIncreasingPathSerializer,
)
from .utils import rotate_array, kth_largest, longest_increasing_path


@api_view(["POST"])
def rotate_array_view(request: Request) -> Response:
    """Rotate an array of integers to the right by k steps."""
    serializer = RotateArraySerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    data = serializer.validated_data
    nums = data["nums"]
    k = data["k"]
    return Response({"result": rotate_array(nums, k)})


@api_view(["POST"])
def kth_largest_view(request: Request) -> Response:
    """Find the kth largest element in an unsorted array."""
    serializer = KthLargestSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    data = serializer.validated_data
    nums = data["nums"]
    k = data["k"]
    return Response({"result": kth_largest(nums, k)})


@api_view(["POST"])
def longest_increasing_path_view(request: Request) -> Response:
    """Find the length of the longest increasing path in a matrix."""
    serializer = LongestIncreasingPathSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    data = serializer.validated_data
    matrix = data["matrix"]
    return Response({"result": longest_increasing_path(matrix)})
