"""This module contains the serializers for the LeetCode app."""

from rest_framework import serializers


class RotateArraySerializer(serializers.Serializer):
    """
    Serializer for rotating an array.

    Fields:
        nums: List of integers to be rotated.
        k: Number of steps to rotate the array.
    """

    nums = serializers.ListField(child=serializers.IntegerField())
    k = serializers.IntegerField()

    class Meta:
        """This class defines the metadata of the RotateArraySerializer class."""

        fields = ["nums", "k"]

    def validate(self, data):
        """
        Validate the input data.

        Ensures that k is non-negative and nums is not empty.
        """
        errors = {}
        if data["k"] < 0:
            errors["k"] = "k must be a non-negative integer."
        if len(data["nums"]) < 1:
            errors["nums"] = "nums must have at least one element."
        if errors:
            raise serializers.ValidationError(errors)
        return data


class KthLargestSerializer(serializers.Serializer):
    """
    Serializer for finding the kth largest element in an array.

    Fields:
        nums: List of integers.
        k: The kth largest element to find.
    """

    nums = serializers.ListField(child=serializers.IntegerField())
    k = serializers.IntegerField()

    class Meta:
        """This class defines the metadata of the KthLargestSerializer class."""

        fields = ["nums", "k"]

    def validate(self, data):
        """Validate the input data."""
        errors = {}
        if data["k"] < 1:
            errors["k"] = "k must be a positive integer."
        if len(data["nums"]) < 1:
            errors["nums"] = "nums must have at least one element."
        if data["k"] > len(data["nums"]):
            errors["k"] = "k must be less than or equal to the length of nums."
        if errors:
            raise serializers.ValidationError(errors)
        return data


class LongestIncreasingPathSerializer(serializers.Serializer):
    """
    Serializer for finding the length of the longest increasing path in a matrix.

    Fields:
        matrix: List of lists of integers
    """

    matrix = serializers.ListField(
        child=serializers.ListField(child=serializers.IntegerField())
    )

    class Meta:
        """This class defines the metadata of the LongestIncreasingPathSerializer class."""

        fields = ["matrix"]

    def validate(self, data):
        """Validate the input data."""
        errors = {}
        if len(data["matrix"]) < 1:
            errors["matrix"] = "matrix must have at least one row."
        if len(data["matrix"][0]) < 1:
            errors["matrix"] = "matrix must have at least one column."
        if errors:
            raise serializers.ValidationError(errors)
        return data
