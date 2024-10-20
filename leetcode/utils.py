"""This module contains utility functions for the leetcode app."""


def reverse(arr, start, end):
    """Reverse a subarray of an array."""
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def partition(arr, left, right):
    """Partition an array around a pivot element."""
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


def rotate_array(nums, k):
    """Rotate an array of integers to the right by k steps."""
    n = len(nums)
    k %= n
    reverse(nums, 0, n - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, n - 1)
    return nums


def kth_largest(arr, k):
    """Find the kth largest element in an unsorted array."""
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
    return None


def longest_increasing_path(matrix):
    """Find the length of the longest increasing path in a matrix."""
    m, n = len(matrix), len(matrix[0])
    dp = [[0] * n for _ in range(m)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def dfs(i, j):
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
