import pytest
from lc_001_two_sum_v1 import Solution

def test_twoSum_happy_path():
    sol = Solution()
    assert sol.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert sol.twoSum([3, 2, 4], 6) == [1, 2]
    assert sol.twoSum([3, 3], 6) == [0, 1]

def test_twoSum_edge_cases():
    sol = Solution()
    assert sol.twoSum([-1, -2, -3, -4, -5], -8) == [2, 4]  # Negatives
    assert sol.twoSum([0, 4, 3, 0], 0) == [0, 3]           # Zeroes & duplicates
    assert sol.twoSum([1000000, 1000001], 2000001) == [0, 1]  # Large numbers