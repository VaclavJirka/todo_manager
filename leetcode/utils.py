"""This module contains utility functions for the leetcode app."""

from typing import List


def reverse(arr: List[int], start: int, end: int) -> None:
    """
    Reverse a subarray of an array.

    Args:
        arr: List[int] - The array to reverse.
        start: int - The start index of the subarray.
        end: int - The end index of the subarray.
    """
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def partition(arr: List[int], left: int, right: int) -> int:
    """
    Partition an array around a pivot element.

    Args:
        arr: List[int] - The array to partition.
        left: int - The left index of the subarray.
        right: int - The right index of the subarray.

    Returns:
        int - The index of the pivot element after partitioning.
    """
    pivot_index = right
    pivot = arr[pivot_index]
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
    store_index = left
    for i in range(left, right):
        if arr[i] < pivot:
            arr[store_index], arr[i] = arr[i], arr[store_index]
            store_index += 1
    arr[right], arr[store_index] = arr[store_index], arr[right]
    return store_index


def rotate_array(nums: List[int], k: int) -> List[int]:
    """
    Rotate an array of integers to the right by k steps.

    Args:
        nums: List[int] - The array of integers.
        k: int - The number of steps to rotate the array.

    Returns:
        List[int] - The rotated array.
    """
    n = len(nums)
    k %= n
    reverse(nums, 0, n - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, n - 1)
    return nums


def kth_largest(arr: List[int], k: int) -> int:
    """
    Find the kth largest element in an array.

    Args:
        arr: List[int] - The array of integers.
        k: int - The kth largest element to find.

    Returns:
        int - The kth largest element.
    """
    k = len(arr) - k
    left, right = 0, len(arr) - 1
    while left <= right:
        pivot_index = partition(arr, left, right)
        if k == pivot_index:
            return arr[k]
        elif k < pivot_index:
            right = pivot_index - 1
        else:
            left = pivot_index + 1
    return -1


def longest_increasing_path(matrix: List[List[int]]) -> int:
    """
    Find the length of the longest increasing path in a matrix.

    Args:
        matrix: List[List[int]] - The matrix of integers.

    Returns:
        int - The length of the longest increasing path.
    """
    m, n = len(matrix), len(matrix[0])
    dp = [[0] * n for _ in range(m)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def dfs(i: int, j: int) -> int:
        if dp[i][j]:
            return dp[i][j]
        for dx, dy in directions:
            x, y = i + dx, j + dy
            if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                dp[i][j] = max(dp[i][j], dfs(x, y))
        dp[i][j] += 1
        return dp[i][j]

    for i in range(m):
        for j in range(n):
            dfs(i, j)
    return max(max(row) for row in dp)
