import pytest
from lc_001_two_sum_review import Solution
def test_recall():
    sol = Solution()
    assert sol.twoSum([2,7,11,15], 9) == [0,1]
    assert sol.twoSum([3,3], 6) == [0,1]