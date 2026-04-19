import pytest
from lc_217_contains_duplicate_optimal import Solution

# 1️⃣ Happy Path (LeetCode examples) → Standard inputs matching LeetCode examples
def test_contains_duplicate_happy_path():
    sol = Solution()
    assert sol.containsDuplicate([1, 2, 3, 1]) == True       # Duplicate exists
    assert sol.containsDuplicate([1, 2, 3, 4]) == False      # All unique
    assert sol.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True  # Multiple dups

# 2️⃣ Edge Cases & Boundaries
def test_contains_duplicate_edge_cases():
    sol = Solution()
    assert sol.containsDuplicate([1]) == False               # Minimum size (n=1)
    assert sol.containsDuplicate([1, 1]) == True             # Exact pair
    assert sol.containsDuplicate([0, -1, 2, -1, 3]) == True  # Negative numbers
    assert sol.containsDuplicate([10**5, 10**5]) == True     # Max constraint value

# 3️⃣ Parametrized (Optional but highly recommended for DSA)
@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 3, 1], True),
    ([1, 2, 3, 4], False),
    ([5], False),
    ([2, 2, 2, 2], True),
    ([-3, -2, -1, 0, 1, 2, 3], False),
])
def test_contains_duplicate_parametrized(nums, expected):
    sol = Solution()
    assert sol.containsDuplicate(nums) == expected